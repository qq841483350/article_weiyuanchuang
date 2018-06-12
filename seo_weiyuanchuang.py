#coding:utf8
#SEO文章伪原创工具 开发者：李亚涛
import wx,requests,re,hashlib,time,md5,threading
salt=int(time.time())
appid=XXX  #这个需要自己到百度申请
miyao='XXX'  #百度翻译密钥，这个需要自己到百度申请
def fanyi(text):
    sign='%s%s%s%s'%(appid,str(text),salt,miyao)
    sign=md5.md5(sign)  #MD5加密
    text=str(text)
    print text
    url='http://api.fanyi.baidu.com/api/trans/vip/translate?q=%s&from=auto&to=en&appid=20160727000025884&salt=%s&sign=%s'%(text,salt,sign)
    html=requests.get(url).content
    text=re.findall('"dst":"([\s\S]*?)"',html)[0].decode('utf8')

    if text:
        sign='%s%s%s%s'%(appid,str(text),salt,miyao)
        sign=md5.md5(sign)
        url_fy='http://api.fanyi.baidu.com/api/trans/vip/translate?q=%s&from=auto&to=zh&appid=20160727000025884&salt=%s&sign=%s'%(text,salt,sign)
        html_fy=requests.get(url_fy).content.decode('utf8')
        result=re.findall('"dst":"([\s\S]*?)"}]}',html_fy)[0].decode("unicode-escape")
        if result:
            contents2.AppendText(result+'\n\n')
            # print result
            # contents2.SetValue(result)   #设置contents里的内容
        else:
            wx.MessageBox(u"出错了，请确认网络连接是否正常")
    else:
        wx.MessageBox(u"出错了，请确认网络连接是否正常")
def wyc(event):
    contents2.Clear()  #清空内容
    text=contents1.GetValue()  #获取contents1里的内容
    if text:
        text1=text+"\n"
        text_list=re.findall('(.*?)\s+',text1)
        for text in text_list:
            fanyi(text)

    else:
        wx.MessageBox(u"错误提示，检测内容为空，请填入需要伪原创的文章内容")


if __name__=="__main__":

    app = wx.App()
    win = wx.Frame(None,title = "SEO文章伪原创工具（左侧填入内容>点击开始执行伪原创>右侧显示伪原创后的内容）---开发者：李亚涛微信841483350".decode('utf8'), size=(1200,800))
    icon = wx.Icon('favicon.ico', wx.BITMAP_TYPE_ICO)
    win.SetIcon(icon)
    win.Show()
    contents1 = wx.TextCtrl(win, pos = (5,5),size = (500,600), style = wx.TE_MULTILINE | wx.TE_RICH)
    contents2 = wx.TextCtrl(win, pos = (650,5),size = (500,600), style = wx.TE_MULTILINE | wx.TE_RICH)
    loadButton = wx.Button(win, label = '开始执行伪原创>>'.decode('utf8'),pos = (515,310),size = (120,40))
    loadButton.Bind(wx.EVT_BUTTON,wyc)  #这个按钮绑定 wyc 这个函数
    app.MainLoop()
    wyc()
