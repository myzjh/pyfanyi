# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"逗比语音翻译", pos = wx.DefaultPosition, size = wx.Size( 432,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetIcon(wx.Icon(u'D:\Java\eclipse_neon\workspace\pyfanyi\img\icon.png'))
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer5.SetMinSize( wx.Size( -1,25 ) ) 
        self.input = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.input.SetMinSize( wx.Size( 300,25 ) )
        
        bSizer5.Add( self.input, 0, wx.ALL, 5 )
        
        self.go = wx.Button( self.m_panel3, wx.ID_ANY, u"go", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.go.SetMinSize( wx.Size( -1,26 ) )
        
        bSizer5.Add( self.go, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer5 )
        self.m_panel3.Layout()
        bSizer5.Fit( self.m_panel3 )
        bSizer4.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer6.SetMinSize( wx.Size( -1,220 ) ) 
        self.text = wx.StaticText( self.m_panel4, wx.ID_ANY, u"翻译：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text.Wrap( -1 )
        bSizer6.Add( self.text, 0, wx.ALL, 5 )
        
        self.richText = wx.richtext.RichTextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
        self.richText.SetMinSize( wx.Size( 500,-1 ) )
        self.richText.SetMaxSize( wx.Size( 500,-1 ) )
        
        bSizer6.Add( self.richText, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer6 )
        self.m_panel4.Layout()
        bSizer6.Fit( self.m_panel4 )
        bSizer4.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer4 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.onClose )
        self.go.Bind( wx.EVT_BUTTON, self.got )
    
    def __del__( self ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def onClose( self, event ):
        import sys
        sys.exit()
    
    def got( self, event ):
        import fanyi
        print 'go'
        tran = fanyi.Tran()
        keyword = self.input.GetValue()
        if keyword:
            result = tran.translate(keyword)
            self.richText.SetValue(result)
            tran.speak(result)
    

app = wx.App(False)
panel = MyFrame3(None)
panel.Show()
app.MainLoop()

