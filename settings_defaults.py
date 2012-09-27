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

# The pairs are "file to be generated" and "template file"
files = {
    'Program Specifications': {
        'template_name': 'Program Specifications.html',
        'settings_dict': program_specs,
        'output': './output/%s - Program Specifications.html' % global_conf['number']
    }
}
