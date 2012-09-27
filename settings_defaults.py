#!/usr/bin/python
from markdown import markdown as md

class Opt(dict):
    """A dictionary that returns a blank string if an attribute isn't found"""
    def __init__(self, dict=None, **kwargs):
        self.data = {}
        if dict is not None:
            self.update(dict)
        if len(kwargs):
            self.update(kwargs)
    
    def update(self, dict=None, **kwargs):
        if dict is None:
            pass
        elif isinstance(dict, Opt):
            self.data.update(dict.data)
        elif isinstance(dict, type({})) or not hasattr(dict, 'items'):
            self.data.update(dict)
        else:
            for k, v in dict.items():
                self[k] = v
        if len(kwargs):
            self.data.update(kwargs)

    def __repr__(self): return repr(self.data)
    def __len__(self): return len(self.data)
    def __getitem__(self, key): return self.data[key] if key in self.data else ''
    def __setitem__(self, key, item): self.data[key] = item
    def __delitem__(self, key): del self.data[key]
    def __contains__(self, key): return key in self.data
    def __getattr__(self, key): return self.__getitem__(key)
    def clear(self): self.data.clear()
    def keys(self): return self.data.keys()
    def items(self): return self.data.items()
    def values(self): return self.data.values()
    def iteritems(self): return self.data.iteritems()
    def iterkeys(self): return self.data.iterkeys()
    def itervalues(self): return self.data.itervalues()

## GLOBAL SETTINGS ##
global_conf = {
	'number': '91214',
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
        Opt({
            "name": "network_server.c",
            "purpose": "Server wrapping code",
            "prerequisites": "N/A",
            "function": "handle_new_connection()",
            "description": 
md(r"""
<pre>void handle_new_connection() {
    int listnum;    /* Current item in connectlist for for loops */
    int connection; /* Socket file descriptor for incoming connections */

    /* We have a new connection coming in!  We'll
    try to find a spot for it in connectlist. */
    connection = accept(sock, NULL, NULL);

    if (connection < 0) {
        <span class="addition">perror("accept");</span>
        exit(EXIT_FAILURE);
    }

    setnonblocking(connection);

    for (listnum = 0; (listnum < 5) && (connection != -1); listnum++)
        if (connectlist[listnum] == 0) {
            <span class="addition">printf("\nConnection accepted:   FD=%d; Slot=%d\n",
                connection,listnum);</span>
            <span class="deletion">printf("\nConnection accepted:   FD=%d\n",
                connection,listnum);</span>
            connectlist[listnum] = connection;
            connection = -1;
        }

    if (connection != -1) {
        /* No room left in the queue! */
        printf("\nNo room left for new client.\n");
        sock_puts(connection,"Sorry, this server is too busy.  "
                    Try again later!\r\n");
        close(connection);
    }
}</pre>
""")
        }),
        Opt({
            "name": "network_client.java",
            "purpose": "Client wrapping code",
            "prerequisites": "N\A",
            "input": "",
            "output": "",
            "system_parms": "",
            "function": "client_connect()",
            "description":
            r"""<pre>// Create a socket without a timeout
    try {
        InetAddress addr = InetAddress.getByName("java.sun.com");
        <span class="addition">int port = 80;</span>

        // This constructor will block until the connection succeeds
        <span class="deletion">Socket socket = new Socket(addr, 80);</span>
        <span class="addition">Socket socket = new Socket(addr, port);</span>
    } catch (UnknownHostException e) {
    } catch (IOException e) {
    }

    // Create a socket with a timeout
    try {
        InetAddress addr = InetAddress.getByName("java.sun.com");
        <span class="addition">int port = 80;</span>
        <span class="deletion">SocketAddress sockaddr = new InetSocketAddress(addr, 80);</span>
        <span class="addition">SocketAddress sockaddr = new InetSocketAddress(addr, port);</span>

        // Create an unbound socket
        Socket sock = new Socket();

        // This method will block no more than timeoutMs.
        // If the timeout occurs, SocketTimeoutException is thrown.
        int timeoutMs = 2000;   // 2 seconds
        sock.connect(sockaddr, timeoutMs);
    } catch (UnknownHostException e) {
    } catch (SocketTimeoutException e) {
    } catch (IOException e) {
    }"""
        }),
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

    "approach": "Run tests against the Test database and record the output.",
    "summary": [{
        "number": "1.",
        "requirement": "",
        "title": "Server Timing Issues",
        "description": "Check the claim is now paying an amount.",

        "details": [{
            "number": "1.1",
            "condition": "Run claim through system with applied changes",
            "input": "Tester's claim AutomatedTxns/Traci/TC_006777-Edit_303__IP_Bypass.xml",
            "expected": "Claim pays an amount greater than $0.00",
            "actual": 
md("""As expected. See [6368-prior.xml][prior], [6368-post.xml][post], and [6368-diff.html][diff]

[prior]: https://itrace.ohxix.slg.eds.com/Ohio42/Subsystem/Claims/Change%20Orders/6368/Testing/6368-prior.xml
[post]:  https://itrace.ohxix.slg.eds.com/Ohio42/Subsystem/Claims/Change%20Orders/6368/Testing/6368-post.xml
[diff]:  https://itrace.ohxix.slg.eds.com/Ohio42/Subsystem/Claims/Change%20Orders/6368/Testing/6368-diff.html""")
    }],

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
    "summary": """Program specification goes here.""",
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
        },
        "autosys": {
            "name": "",
            "promotion_list": "",
            "mo": "",
            "prod": "",
        },
        "deleted": {
            "name": "",
            "promotion_list": "",
            "mo": "",
            "prod": "",
        },
    },
    'database': {
        'table': {
            'name': '',
            'location': ''
        },
        'xml': {
            'name': '',
            'location': ''
        },
        'updates': {
            'name': '',
            'location': ''
        }
    }
}

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
