import wx
def load(event):
    file=open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()
def save(event):
    file=open(filename.GetValue(),'w')
    file.write(contents.GetValue())
    file.close()

app=wx.App()
win=wx.Frame(None,title="dPAD",size=(500,500))
panel=wx.Panel(win)
loadbutton=wx.Button(panel,label='Open')
loadbutton.Bind(wx.EVT_BUTTON,load)
savebutton=wx.Button(panel,label='Save')
savebutton.Bind(wx.EVT_BUTTON,save)

filename=wx.TextCtrl(panel)
contents=wx.TextCtrl(panel,style=wx.TE_MULTILINE|wx.HSCROLL)

hbox=wx.BoxSizer()
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(loadbutton,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(savebutton,proportion=0,flag=wx.LEFT,border=5)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
panel.SetSizer(vbox)

win.Show()
app.MainLoop()
