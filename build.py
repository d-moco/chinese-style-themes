import json,html,os,subprocess,sys
ROOT = os.path.dirname(os.path.abspath(__file__))
def theme_path(theme_id, *parts):
    return os.path.join(ROOT, "themes", theme_id, *parts)
def lum(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    c=[x/12.92 if x<=.03928 else ((x+.055)/1.055)**2.4 for x in c]
    return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a,b):
    l=sorted([lum(a[:7]),lum(b[:7])]);return (l[1]+.05)/(l[0]+.05)
def build(T):
    p=T; d=p['dark']; os.makedirs(theme_path(p['id'], "themes"),exist_ok=True)
    for k in "fg fg2 kw str num fn type deco param prop comment".split():
        r=cr(p[k],p['bg']); print(p['id'],k,p[k],round(r,2), "" if r>=4.5 else "  <<< LOW")
    A=p['ansi']  # black red green yellow blue magenta cyan white + bright 8
    on=p['accentFg']
    c={"focusBorder":p['accent']+"99","foreground":p['fg'],"descriptionForeground":p['fg2'],"errorForeground":p['err'],"icon.foreground":p['fg2'],"widget.shadow":"#00000055" if d else "#00000022","selection.background":p['sel'],
"editor.background":p['bg'],"editor.foreground":p['fg'],"editorLineNumber.foreground":p['lineno'],"editorLineNumber.activeForeground":p['accent'],"editorCursor.foreground":p['accent'],
"editor.selectionBackground":p['sel'],"editor.inactiveSelectionBackground":p['sel']+"88","editor.selectionHighlightBackground":p['hl'],"editor.wordHighlightBackground":p['hl'],"editor.wordHighlightStrongBackground":p['sel']+"AA",
"editor.findMatchBackground":p['find']+"99","editor.findMatchHighlightBackground":p['find']+"44","editor.lineHighlightBackground":p['line'],"editor.lineHighlightBorder":"#00000000",
"editorIndentGuide.background1":p['border'],"editorIndentGuide.activeBackground1":p['lineno'],"editorWhitespace.foreground":p['border'],"editorRuler.foreground":p['border'],
"editorBracketMatch.background":p['hl'],"editorBracketMatch.border":p['accent']+"88","editorBracketHighlight.foreground1":p['kw'],"editorBracketHighlight.foreground2":p['fn'],"editorBracketHighlight.foreground3":p['str'],"editorBracketHighlight.foreground4":p['num'],
"editorError.foreground":p['err'],"editorWarning.foreground":p['warn'],"editorInfo.foreground":p['fn'],"editorLink.activeForeground":p['fn'],
"editorGutter.addedBackground":p['add'],"editorGutter.modifiedBackground":p['mod'],"editorGutter.deletedBackground":p['err'],
"editorWidget.background":p['bg2'],"editorWidget.border":p['border'],"editorSuggestWidget.background":p['bg2'],"editorSuggestWidget.border":p['border'],"editorSuggestWidget.selectedBackground":p['sel'],"editorSuggestWidget.highlightForeground":p['accent'],
"editorHoverWidget.background":p['bg2'],"editorHoverWidget.border":p['border'],"editorGroupHeader.tabsBackground":p['bg2'],"editorGroup.border":p['border'],
"tab.activeBackground":p['bg'],"tab.activeForeground":p['fg'],"tab.activeBorderTop":p['accent'],"tab.inactiveBackground":p['bg2'],"tab.inactiveForeground":p['dim'],"tab.border":p['border'],"tab.hoverBackground":p['line'],
"titleBar.activeBackground":p['title'],"titleBar.activeForeground":p['titleFg'],"titleBar.inactiveBackground":p['title'],"titleBar.inactiveForeground":p['dim'],"titleBar.border":p['border'],
"activityBar.background":p['bg3'],"activityBar.foreground":p['accent'] if d else p['fg'],"activityBar.inactiveForeground":p['dim'],"activityBar.activeBorder":p['accent'],"activityBarBadge.background":p['accent'],"activityBarBadge.foreground":on,"activityBar.border":p['border'],
"sideBar.background":p['bg2'],"sideBar.foreground":p['fg'],"sideBar.border":p['border'],"sideBarTitle.foreground":p['fg2'],"sideBarSectionHeader.background":p['bg3'],"sideBarSectionHeader.foreground":p['fg'],
"list.activeSelectionBackground":p['sel'],"list.activeSelectionForeground":p['fg'],"list.inactiveSelectionBackground":p['line'],"list.hoverBackground":p['line'],"list.focusOutline":p['accent']+"88","list.highlightForeground":p['accent'],"list.errorForeground":p['err'],"list.warningForeground":p['warn'],
"statusBar.background":p['status'],"statusBar.foreground":p['statusFg'],"statusBar.border":p['status'],"statusBar.noFolderBackground":p['status'],"statusBar.debuggingBackground":p['accent'],"statusBar.debuggingForeground":on,"statusBarItem.remoteBackground":p['accent'],"statusBarItem.remoteForeground":on,"statusBarItem.hoverBackground":p['line'],
"panel.background":p['bg2'],"panel.border":p['border'],"panelTitle.activeForeground":p['fg'],"panelTitle.activeBorder":p['accent'],"panelTitle.inactiveForeground":p['dim'],
"terminal.background":p['bg2'],"terminal.foreground":p['fg'],"terminalCursor.foreground":p['accent'],"terminal.selectionBackground":p['sel'],
"gitDecoration.addedResourceForeground":p['add'],"gitDecoration.untrackedResourceForeground":p['add'],"gitDecoration.modifiedResourceForeground":p['mod'],"gitDecoration.deletedResourceForeground":p['err'],"gitDecoration.conflictingResourceForeground":p['deco'],"gitDecoration.ignoredResourceForeground":p['dim'],
"button.background":p['accent'],"button.foreground":on,"button.hoverBackground":p['kw'],"button.secondaryBackground":p['bg3'],"button.secondaryForeground":p['fg'],
"input.background":p['input'],"input.foreground":p['fg'],"input.border":p['border'],"input.placeholderForeground":p['dim'],"inputOption.activeBorder":p['accent'],"dropdown.background":p['input'],"dropdown.border":p['border'],"checkbox.background":p['input'],"checkbox.border":p['border'],
"badge.background":p['accent'],"badge.foreground":on,"progressBar.background":p['accent'],"scrollbarSlider.background":p['fg2']+"33","scrollbarSlider.hoverBackground":p['fg2']+"55","scrollbarSlider.activeBackground":p['fg2']+"77",
"menu.background":p['bg2'],"menu.foreground":p['fg'],"menu.selectionBackground":p['sel'],"menu.border":p['border'],"quickInput.background":p['bg2'],"quickInputList.focusBackground":p['sel'],
"textLink.foreground":p['fn'],"textLink.activeForeground":p['accent'],"textBlockQuote.background":p['bg2'],"textCodeBlock.background":p['bg2'],"breadcrumb.foreground":p['dim'],"breadcrumb.focusForeground":p['fg'],
"minimap.background":p['bg'],"notifications.background":p['bg2'],"notifications.border":p['border'],"peekView.border":p['accent'],"peekViewEditor.background":p['bg2'],"peekViewResult.background":p['bg2'],"peekViewTitle.background":p['bg3'],
"diffEditor.insertedTextBackground":p['add']+"26","diffEditor.removedTextBackground":p['err']+"26"}
    c.update(p.get("over",{}))
    for i,n in enumerate("Black Red Green Yellow Blue Magenta Cyan White".split()):
        c["terminal.ansi"+n]=A[i]; c["terminal.ansiBright"+n]=A[i+8]
    def t(scope,fg,fs=None):
        s={"foreground":fg}; 
        if fs:s["fontStyle"]=fs
        return {"scope":scope,"settings":s}
    tok=[t(["comment","punctuation.definition.comment","string.comment"],p['comment'],"italic"),
t(["keyword","storage.type","storage.modifier","keyword.control","keyword.operator.new","keyword.operator.expression","keyword.operator.logical.python"],p['kw'],p.get('kwStyle')),
t(["keyword.operator","punctuation.separator","punctuation.terminator","meta.brace","punctuation"],p['fg2']),
t(["string","string.quoted","string.template","punctuation.definition.string"],p['str']),
t(["constant.character.escape","string.regexp"],p['type']),
t(["constant.numeric","constant.language","constant.other","support.constant","variable.other.constant","variable.other.enummember"],p['num']),
t(["entity.name.function","support.function","meta.function-call entity.name.function","variable.function"],p['fn']),
t(["entity.name.type","entity.name.class","support.class","support.type","entity.other.inherited-class","storage.type.primitive","entity.name.namespace"],p['type']),
t(["variable","variable.other.readwrite","meta.definition.variable"],p['fg']),t(["variable.parameter"],p['param'],"italic"),
t(["variable.language","variable.language.this","variable.language.self"],p['deco'],"italic"),t(["entity.name.tag"],p['kw']),t(["entity.other.attribute-name"],p['num'],"italic"),
t(["meta.decorator","entity.name.function.decorator","punctuation.decorator"],p['deco']),
t(["support.type.property-name","meta.object-literal.key","variable.other.property","variable.other.object.property"],p['prop']),
t(["markup.heading","entity.name.section"],p['kw'],"bold"),t(["markup.bold"],p['fg'],"bold"),t(["markup.italic"],p['fg'],"italic"),t(["markup.inline.raw","markup.fenced_code"],p['str']),
t(["markup.underline.link"],p['fn'],"underline"),t(["markup.inserted"],p['add']),t(["markup.deleted"],p['err']),t(["markup.changed"],p['mod']),t(["invalid"],p['err'],"underline")]
    sem={"keyword":p['kw'],"string":p['str'],"number":p['num'],"regexp":p['type'],"comment":{"foreground":p['comment'],"italic":True},"function":p['fn'],"method":p['fn'],"macro":p['deco'],
"class":p['type'],"interface":p['type'],"enum":p['type'],"struct":p['type'],"type":p['type'],"typeParameter":{"foreground":p['type'],"italic":True},"namespace":p['type'],
"parameter":{"foreground":p['param'],"italic":True},"variable":p['fg'],"variable.readonly":p['num'],"property":p['prop'],"enumMember":p['num'],"decorator":p['deco'],"*.deprecated":{"strikethrough":True},"selfKeyword":{"foreground":p['deco'],"italic":True}}
    fn=f"{p['id']}-color-theme.json"
    json.dump({"name":p['name'],"type":"dark" if d else "light","semanticHighlighting":True,"colors":c,"tokenColors":tok,"semanticTokenColors":sem},open(theme_path(p['id'], "themes", fn),"w"),ensure_ascii=False,indent=2)
    json.dump({"name":p['id'],"displayName":p['name'],"description":p['desc'],"version":p.get("ver","0.1.0"),"publisher":"moco","license":"MIT","engines":{"vscode":"^1.70.0"},"categories":["Themes"],"keywords":["theme","chinese","中国风","dark" if d else "light"],
"contributes":{"themes":[{"label":p['name'],"uiTheme":"vs-dark" if d else "vs","path":f"./themes/{fn}"}]}},open(theme_path(p['id'], "package.json"),"w"),ensure_ascii=False,indent=1)
    open(theme_path(p['id'], "LICENSE"),"w").write(open(os.path.join(ROOT, "LICENSE")).read())
    open(theme_path(p['id'], ".vscodeignore"),"w").write("*.vsix\n")
    rows="\n".join(f"| {a} | `{p[b]}` |" for a,b in [("编辑器底色","bg"),("侧栏 / 面板","bg2"),("正文","fg"),("强调色","accent"),("关键字","kw"),("字符串","str"),("函数","fn"),("类型","type"),("数字 / 常量","num"),("注释（斜体）","comment"),("状态栏","status")])
    open(theme_path(p['id'], "README.md"),"w").write(f"""# {p['name']}

{p['desc']}主要文字对比度均达到 WCAG AA。

![{p['name']}](preview.png)

## 安装（Cursor / VS Code）

1. 打开扩展面板（Extensions）。
2. 点击面板右上角的 `...` 菜单，选择 **Install from VSIX...**。
3. 选择 `{p['id']}-{p.get('ver','0.1.0')}.vsix` 文件。
4. 打开命令面板，执行 **Preferences: Color Theme**，选择 **{p['name']}**。

## 色板

| 用途 | 颜色 |
|---|---|
{rows}
""")
    render(p,c)
def render(p,c):
    K,S,N,F,T,C,PU,PA,PR,O,V=p['kw'],p['str'],p['num'],p['fn'],p['type'],p['comment'],p['deco'],p['param'],p['prop'],p['fg2'],p['fg']
    def s(t,col,it=False):return f'<span style="color:{col};{"font-style:italic;" if it else ""}{"font-weight:600;" if col==K and p.get("kwStyle")=="bold" else ""}">{html.escape(t)}</span>'
    c1,c2,c3=p['comments']
    L=[[s("# "+c1,C,1)],[s("from",K),s(" dataclasses ",V),s("import",K),s(" dataclass",V)],[s("from",K),s(" typing ",V),s("import",K),s(" ",V),s("Iterator",T)],[],
[s("@dataclass",PU)],[s("class",K),s(" ",V),s("Verse",T),s(":",O)],[s('    """'+c2+'"""',S)],[s("    title",PR),s(": ",O),s("str",T)],[s("    lines",PR),s(": ",O),s("list",T),s("[",O),s("str",T),s("]",O)],[s("    rhyme",PR),s(": ",O),s("float",T),s(" = ",O),s("0.618",N)],[],
[s("    ",V),s("def",K),s(" ",V),s("recite",F),s("(",O),s("self",PU,1),s(", ",O),s("tempo",PA,1),s(": ",O),s("int",T),s(" = ",O),s("72",N),s(") -> ",O),s("Iterator",T),s("[",O),s("str",T),s("]:",O)],
[s("        ",V),s("# "+c3,C,1)],[s("        ",V),s("for",K),s(" i, line ",V),s("in",K),s(" ",V),s("enumerate",F),s("(",O),s("self",PU,1),s(".",O),s("lines",PR),s(", ",O),s("start",PA,1),s("=",O),s("1",N),s("):",O)],
[s("            ",V),s("if",K),s(" ",V),s("not",K),s(" line.",V),s("strip",F),s("():",O)],[s("                ",V),s("continue",K)],
[s("            ",V),s("yield",K),s(" ",V),s('f"',S),s("{",O),s("i",V),s(":02d}",O),s(" · ",S),s("{",O),s("line",V),s("}",O),s('"',S)],[],
[s("poem",V),s(" = ",O),s("Verse",T),s("(",O),s("title",PA,1),s("=",O),s(repr(p['poem'][0]).replace("'",'"'),S),s(", ",O),s("lines",PA,1),s("=[",O),s(f'"{p["poem"][1]}"',S),s(", ",O),s(f'"{p["poem"][2]}"',S),s("])",O)],
[s("for",K),s(" verse ",V),s("in",K),s(" poem.",V),s("recite",F),s("(",O),s("tempo",PA,1),s("=",O),s("60",N),s("):",O)],[s("    ",V),s("print",F),s("(verse, ",O),s("None",N),s(", ",O),s("True",N),s(")",O)]]
    CUR=16
    code="".join(f'<div class="ln{" cur" if i==CUR else ""}"><span class="no" style="color:{c["editorLineNumber.activeForeground"] if i==CUR else c["editorLineNumber.foreground"]}">{i+1}</span>{"".join(l)}</div>' for i,l in enumerate(L))
    tree=[("▾ "+p['proj'].upper(),0,c["sideBarSectionHeader.foreground"],0,""),("▾ poems",1,V,0,""),("verse.py",2,c["gitDecoration.modifiedResourceForeground"],1,"M"),("rhyme.py",2,c["gitDecoration.addedResourceForeground"],0,"A"),("__init__.py",2,V,0,""),("▸ assets",1,V,0,""),("README.md",1,V,0,""),("pyproject.toml",1,V,0,""),(".gitignore",1,c["gitDecoration.ignoredResourceForeground"],0,"")]
    tr="".join(f'<div class="ti" style="padding-left:{14+d*14}px;color:{col};{"background:"+c["list.activeSelectionBackground"] if sel else ""}">{n}<b style="float:right;margin-right:12px">{m}</b></div>' for n,d,col,sel,m in tree)
    A=p['ansi']
    term=f'''<div><span style="color:{A[2]}">moco@{p['host']}</span> <span style="color:{A[4]}">~/{p['proj']}</span> <span style="color:{A[1]}">$</span> python verse.py</div>
<div style="color:{p['fg']}">01 · {p['poem'][1]}</div><div style="color:{p['fg']}">02 · {p['poem'][2]}</div>
<div><span style="color:{A[2]}">✔</span> 吟诵完毕 <span style="color:{A[3]}">2 lines</span> · <span style="color:{A[5]}">0.42s</span> · <span style="color:{A[6]}">utf-8</span></div>'''
    H=f'''<html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1600px;height:1000px;overflow:hidden;font-family:"Noto Sans CJK SC",sans-serif;font-size:13px;background:{p['bg']};color:{p['fg']};display:flex;flex-direction:column;position:relative;border:{p['frame']}}}
.mono{{font-family:"DejaVu Sans Mono","Noto Sans CJK SC",monospace}}
.title{{height:36px;background:{p['title']};color:{p['titleFg']};border-bottom:1px solid {c["titleBar.border"]};display:flex;align-items:center;justify-content:center;position:relative;letter-spacing:1px}}
.dots{{position:absolute;left:14px;display:flex;gap:8px}}.dots i{{width:12px;height:12px;border-radius:6px;display:block}}
.main{{flex:1;display:flex;min-height:0}}.act{{width:52px;background:{p['bg3']};border-right:1px solid {p['border']};padding-top:8px}}
.ai{{height:48px;display:flex;align-items:center;justify-content:center;font-size:20px;color:{c['activityBar.inactiveForeground']}}}
.side{{width:270px;background:{p['bg2']};border-right:1px solid {p['border']}}}.st{{padding:10px 14px;font-size:11px;letter-spacing:1px;color:{c['sideBarTitle.foreground']}}}.ti{{height:24px;line-height:24px}}
.ed{{flex:1;display:flex;flex-direction:column;min-width:0;position:relative}}.tabs{{height:38px;background:{p['bg2']};display:flex;border-bottom:1px solid {p['border']}}}
.tab{{padding:0 18px;line-height:37px;border-right:1px solid {p['border']};color:{p['dim']}}}.tab.a{{background:{p['bg']};color:{p['fg']};border-top:2px solid {p['accent']};line-height:35px;height:38px}}
.bc{{padding:4px 20px;font-size:12px;color:{p['dim']}}}.code{{flex:1;padding-top:6px;font-size:15px;line-height:24px;overflow:hidden;position:relative;z-index:2}}.ln{{white-space:pre;height:24px}}.ln.cur{{background:{p['line']}}}
.no{{display:inline-block;width:58px;text-align:right;padding-right:22px}}
.panel{{height:190px;background:{p['bg2']};border-top:1px solid {p['border']};padding:0 20px;position:relative;z-index:2}}.ph{{display:flex;gap:22px;font-size:11px;letter-spacing:1px;height:34px;align-items:center;color:{p['dim']}}}
.ph .a{{color:{p['fg']};border-bottom:1px solid {p['accent']};padding-bottom:4px}}.term{{font-size:14px;line-height:23px}}
.status{{height:26px;background:{p['status']};color:{p['statusFg']};display:flex;align-items:center;font-size:12px}}.status span{{padding:0 12px}}.rem{{background:{p['accent']};color:{p['accentFg']};height:26px;line-height:26px}}
.deco{{position:absolute;pointer-events:none;z-index:1}}
{p.get('css','')}{p.get('css2','')}
</style></head><body>
<div class="title"><div class="dots"><i style="background:{A[1]}"></i><i style="background:{A[3]}"></i><i style="background:{A[2]}"></i></div>verse.py — {p['proj']} — {html.escape(p['name'])}</div>
<div class="main"><div class="act" style="background:{c['activityBar.background']}"><div class="ai" style="color:{c["activityBar.foreground"]};border-left:2px solid {p['accent']}">❐</div><div class="ai">⌕</div><div class="ai" style="position:relative">⑂<b style="position:absolute;right:9px;top:26px;background:{p['accent']};color:{p['accentFg']};font-size:9px;border-radius:7px;padding:0 4px">2</b></div><div class="ai">▷</div><div class="ai">⊞</div></div>
<div class="side"><div class="st">资源管理器 EXPLORER</div>{tr}</div>
<div class="ed"><div class="tabs" style="background:{c['editorGroupHeader.tabsBackground']}"><div class="tab">rhyme.py</div><div class="tab a">verse.py</div><div class="tab">README.md</div></div><div class="bc">poems › verse.py › Verse › recite</div>
{p['deco_html']}<div class="code mono">{code}</div>
<div class="panel"><div class="ph"><span>问题</span><span>输出</span><span class="a">终端 TERMINAL</span></div><div class="term mono">{term}</div></div></div></div>
<div class="status"><span class="rem" style="background:{c['statusBarItem.remoteBackground']};color:{c['statusBarItem.remoteForeground']}">⟩⟨ {p['host']}</span><span>⑂ main*</span><span>⊗ 0 ⚠ 0</span><span style="margin-left:auto">行 17，列 24</span><span>UTF-8</span><span>Python</span></div>
</body></html>'''
    f=f"/tmp/{p['id']}.html";open(f,"w").write(H)
    shot=theme_path(p['id'], "preview.png")
    subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--window-size=1600,1000",f"--screenshot={shot}","file://"+f],capture_output=True)
if __name__=="__main__":
    sys.path.insert(0, ROOT)
    from palettes import THEMES
    for t in THEMES:
        if len(sys.argv)<2 or t['id'] in sys.argv[1:]: build(t)
