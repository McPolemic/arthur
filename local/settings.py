from datetime import date
#import arthur
#print arthur
from arthur.settings_defaults import *

global_conf = {
	'number': '11111',
}

#Set revision date to today
for i in (program_specs, unit_test, implementation):
	i['revision_history'][0]['last_update'] = date.today().strftime('%m/%d/%Y')

## Default settings ##
# global_conf = {
# 	'number': '15135',
# }

# program_specs = {
#     "title": "Program Specifications",
#     "container_id": "spec",

#     "revision_history": [{
#         "last_update": "10/28/2011",
#         "author": "Adam Lukens",
#         "description": "Initial Creation"
#     }],

#     "assumptions": "Document any assumptions made during the design of the program.",

#     "program_specs_intro": """Program Specifications description goes here.""",
    
#     "modules": [
#         Opt({
#             "name": "clmsub92.sc",
#             "purpose": "Main UB92 claims function",
#             "prerequisites": "N\A",
#             "function": "ub92Main()",
#             "description": md("""This is a **multi-line**

# string""")
#         }),
#         Opt({
#             "name": "clmsub92.sc",
#             "purpose": "Main UB92 claims function",
#             "prerequisites": "N\A",
#             "input": "",
#             "output": "",
#             "system_parms": "",
#             "function": "ub92Main()",
#             "description":
# """<pre>Line 1967
#     if (!is_ch_encounter())
#         dp_claim(clmStatus);

#     <span class="light-blue">/* DF 6368: Moved call higher in execution for if statement */
#     get_uh_indDRGPriced(indDRGPriced);</span>

#     /* OH 741 apply TPL before co-pay */
#     <span class="red"><s>/* Co-Ordination of Benefit Plans */
#     /*DF 6582*/
#     if (is_ch_payOnOneProgram() || indDRGPriced[0] == 'Y')
#     {
#        xref_bp_cobProcessing();
#     }
#     else
#     {
#        xref_bp_dtlCobProcessing();
#     }</s></span>

#     /* TPL Deductions -  Reverse Payer Order */
#     if(cdeClmType[0] == 'A' || cdeClmType[0] == 'L' ||  /* For inpatient, part A and C, and LTC claims
#        cdeClmType[0] == 'I' || cdeClmType[0] == 'C')    /* apply the TPL amount at the header level.
#     {                                                   /* - CO 2835, DFC 5436, 5917
#        xref_applyTpl();
#     }
#     else
#     {
#        xref_dtlApplyTpl();
#     }</pre>"""
#         }),
#     ]
# }

# unit_test = {
#     "title": "Testing Document",
#     "container_id": "test",

#     "revision_history": [{
#         "last_update": "10/28/2011",
#         "author": "Adam Lukens",
#         "description": "Initial Creation"
#     }],

#     "approach": "Verify the current and new functionality works according to the specifications.",
#     "summary": [{
#         "number": "1.",
#         "requirement": "",
#         "title": "Original Defect Claim",
#         "description": "Check the claim is now paying an amount.",

#         "details": [{
#             "number": "1.1",
#             "condition": "Run claim through system with applied changes",
#             "input": "Tester's claim AutomatedTxns/Traci/TC_006777-Edit_303__IP_Bypass.xml",
#             "expected": "Claim pays an amount greater than $0.00",
#             "actual": 
# md("""As expected. See [6368-prior.xml][prior], [6368-post.xml][post], and [6368-diff.html][diff]

# [prior]: https://itrace.ohxix.slg.eds.com/Ohio42/Subsystem/Claims/Change%20Orders/6368/Testing/6368-prior.xml
# [post]:  https://itrace.ohxix.slg.eds.com/Ohio42/Subsystem/Claims/Change%20Orders/6368/Testing/6368-post.xml
# [diff]:  https://itrace.ohxix.slg.eds.com/Ohio42/Subsystem/Claims/Change%20Orders/6368/Testing/6368-diff.html""")
#     }],

#     }]
# }

# implementation = {
#     "title": "Implementation Plan",
#     "container_id": "implement",

#     "revision_history": [{
#         "last_update": "10/28/2011",
#         "author": "Adam Lukens",
#         "description": "Initial Creation"
#     }],
#     "summary": """Program specification goes here.""",
#     "tasks": {
#         "file": {
#             "name": "",
#             "promotion_list": """<pre>clmsub92.sc        1.85</pre>""",
#             "mo": "",
#             "prod": "",
#         },
#         "module": {
#             "name": "",
#             "promotion_list": """<pre>libclmub92.so      1.160</pre>""",
#             "mo": "",
#             "prod": "",
#         },
#         "autosys": {
#             "name": "",
#             "promotion_list": "",
#             "mo": "",
#             "prod": "",
#         },
#         "deleted": {
#             "name": "",
#             "promotion_list": "",
#             "mo": "",
#             "prod": "",
#         },
#     },
#     'database': {
#         'table': {
#             'name': '',
#             'location': ''
#         },
#         'xml': {
#             'name': '',
#             'location': ''
#         },
#         'updates': {
#             'name': '',
#             'location': ''
#         }
#     }
# }

# The pairs are "file to be generated" and "template file"
files = {
    'Implementation Plan': {
        'template_name': 'Implementation Plan.html',
        'settings_dict': implementation,
        'output': './output/%s - Implementation Plan.html' % global_conf['number']
    },
    'Program Specifications': {
        'template_name': 'Program Specifications.html',
        'settings_dict': program_specs,
        'output': './output/%s - Program Specifications.html' % global_conf['number']
    },
    'Unit Testing': {
        'template_name': 'Unit Testing.html',
        'settings_dict': unit_test,
        'output': './output/%s - Unit Testing.html' % global_conf['number']
    }
}
