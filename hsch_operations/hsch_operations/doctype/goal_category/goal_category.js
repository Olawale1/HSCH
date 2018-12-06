// Copyright (c) 2018, HSCH and contributors
// For license information, please see license.txt

cur_frm.cscript.refresh = function(doc, cdt, cdn) {
	cur_frm.cscript.set_root_readonly(doc);
}

cur_frm.cscript.set_root_readonly = function(doc) {
	// read-only for root goal category
	if(!doc.parent_goal_category) {
		cur_frm.set_read_only();
		cur_frm.set_intro(__("This is a root goal category and cannot be edited."));
	} else {
		cur_frm.set_intro(null);
	}
}

//get query select Goal Category
cur_frm.fields_dict['parent_goal_category'].get_query = function(doc,cdt,cdn) {
	return {
		filters: {
			'is_group': 1
		}
	}
}
