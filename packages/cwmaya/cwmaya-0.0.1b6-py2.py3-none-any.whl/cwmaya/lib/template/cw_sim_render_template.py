# -*- coding: utf-8 -*-

import pymel.core as pm

from cwmaya.lib.tabs import simple_tab, job_tab, frames_tab
from cwmaya.lib.template import template_utils


def bind(node, dialog):

    dialog.clear_tabs()

    pm.setParent(dialog.tabLayout)
    dialog.tabs["frames_tab"] = frames_tab.FramesTab()
    pm.setParent(dialog.tabLayout)
    dialog.tabs["sim_tab"] = simple_tab.SimpleTab()
    pm.setParent(dialog.tabLayout)
    dialog.tabs["render_tab"] = simple_tab.SimpleTab()
    pm.setParent(dialog.tabLayout)
    dialog.tabs["quicktime_tab"] = simple_tab.SimpleTab()
    pm.setParent(dialog.tabLayout)
    dialog.tabs["job_tab"] = job_tab.JobTab()
    pm.setParent(dialog.tabLayout)

    dialog.tabLayout.setTabLabel((dialog.tabs["frames_tab"], "Frames"))
    dialog.tabLayout.setTabLabel((dialog.tabs["sim_tab"], "Sim task"))
    dialog.tabLayout.setTabLabel((dialog.tabs["render_tab"], "Render task"))
    dialog.tabLayout.setTabLabel((dialog.tabs["quicktime_tab"], "Quicktime task"))
    
    dialog.tabLayout.setTabLabel((dialog.tabs["job_tab"], "Job"))

    dialog.tabs["frames_tab"].bind(node)
    dialog.tabs["sim_tab"].bind(node, "sim")
    dialog.tabs["render_tab"].bind(node, "rnd")
    dialog.tabs["quicktime_tab"].bind(node, "qtm")
    dialog.tabs["job_tab"].bind(node)
    dialog.tabLayout.setSelectTabIndex(1)

    template_utils.setDialogTitle(dialog, node)
