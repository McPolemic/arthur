from datetime import date
#import arthur
#print arthur
from arthur.settings_defaults import *

global_conf = {
	'number': '11111',
}

#Set revision date to today
program_specs['revision_history'][0]['last_update'] = date.today().strftime('%m/%d/%Y')

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

# The pairs are "file to be generated" and "template file"
files = {
    'Program Specifications': {
        'template_name': 'Program Specifications.html',
        'settings_dict': program_specs,
        'output': './output/%s - Program Specifications.html' % global_conf['number']
    }
}
