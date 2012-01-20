#!/usr/bin/python
from markdown import markdown as md

global_conf = {
	'number': '15135',
}

program_specs = {
    "title": "Program Specifications",
    "container_id": "spec",
    "revision_history": [{
        "last_update": "10/28/2011",
        "author": "Adam Lukens",
        "description": "Initial Creation"
    }],

    "assumptions": "Document any assumptions made during the design of the program.",

    "program_specs_intro": """Program Specifications description goes here.""",
    
    "modules": [
        {
            "name": "clmsub92.sc",
            "purpose": "Main UB92 claims function",
            "prerequisites": "N\A",
            "input": "",
            "output": "",
            "system_parms": "",
            "function": "ub92Main()",
            "description":
"""<pre>Line 1967
    if (!is_ch_encounter())
        dp_claim(clmStatus);

    <span class="light-blue">/* DF 6368: Moved call higher in execution for if statement */
    get_uh_indDRGPriced(indDRGPriced);</span>

    /* OH 741 apply TPL before co-pay */
    <span class="red"><s>/* Co-Ordination of Benefit Plans */
    /*DF 6582*/
    if (is_ch_payOnOneProgram() || indDRGPriced[0] == 'Y')
    {
       xref_bp_cobProcessing();
    }
    else
    {
       xref_bp_dtlCobProcessing();
    }</s></span>

    /* TPL Deductions -  Reverse Payer Order */
    if(cdeClmType[0] == 'A' || cdeClmType[0] == 'L' ||  /* For inpatient, part A and C, and LTC claims
       cdeClmType[0] == 'I' || cdeClmType[0] == 'C')    /* apply the TPL amount at the header level.
    {                                                   /* - CO 2835, DFC 5436, 5917
       xref_applyTpl();
    }
    else
    {
       xref_dtlApplyTpl();
    }</pre>"""
        }
    ]
}

unit_test = {
    "title": "Testing Document",
    "container_id": "test",
    "revision_history": [{
        "last_update": "10/28/2011",
        "author": "Adam Lukens",
        "description": "Initial Creation"
    }],

    "approach": "Verify the current and new functionality works according to the specifications.",
    "summary": [{
        "number": "1.",
        "requirement": "",
        "title": "Original Defect Claim",
        "description": "Check the claim is now paying an amount."        
    }],
    #Already sure this is going to have to be re-written.
    #I like the idea of having an array of details, with subarrays for each subtest.
    # 1.1
    # 1.2
    # 1.3
    # ----
    # 2.1 (etc.)
    "details": [{
        "number": "1.1",
        "condition": "Run claim through system with applied changes",
        "input": "Tester's claim AutomatedTxns/Traci/TC_006777-Edit_303__IP_Bypass.xml",
        "expected": "Claim pays an amount greater than $0.00",
        "actual": """As expected. See <a href="https://itrace.ohxix.slg.eds.com/Ohio42/Subsystem/Claims/Change%20Orders/6368/Testing/6368-prior.xml">6368-prior.xml</a>,
  <a href="https://itrace.ohxix.slg.eds.com/Ohio42/Subsystem/Claims/Change%20Orders/6368/Testing/6368-post.xml">6368-post.xml</a>,
  and <a href="https://itrace.ohxix.slg.eds.com/Ohio42/Subsystem/Claims/Change%20Orders/6368/Testing/6368-diff.html">6368-diff.html"""
    }]
}

implementation = {
    "title": "Implementation Plan",
    "container_id": "implement",
    "revision_history": [{
        "last_update": "10/28/2011",
        "author": "Adam Lukens",
        "description": "Initial Creation"
    }],
    "summary": """<<Program specification goes here>>.""",
    "tasks": {
        "file": {
            "name": "",
            "promotion_list": """<pre>clmsub92.sc        1.85</pre>""",
            "mo": "",
            "prod": "",
        },
        "module": {
            "name": "",
            "promotion_list": """<pre>libclmub92.so      1.160</pre>""",
            "mo": "",
            "prod": "",
        }
    }
}

#The pairs are "file to be generated" and "template file"
files = {
    'Implementation Plan': {
        'template_name': 'Implementation Plan.htm',
        'settings_dict': implementation,
        'output': './output/Implementation Plan.html'
    },
    'Program Specifications': {
        'template_name': 'Program Specifications.htm',
        'settings_dict': program_specs,
        'output': './output/Program Specifications.html'
    },
    'Unit Testing': {
        'template_name': 'Unit Testing.htm',
        'settings_dict': unit_test,
        'output': './output/Unit Testing.html'
    }
}