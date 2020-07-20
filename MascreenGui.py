from flexx import flx

class Example(flx.Widget):

    def init(self):
        flx.Button(text='Display Lip motion')
        flx.Button(text='Express Emotion')
        flx.Button(text='Speech To Text')
        flx.Button(text='Translation')

app = flx.App(Example)
app.export('example.html', link=0)
app.launch('browser')
flx.run()