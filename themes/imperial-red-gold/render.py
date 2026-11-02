import json,html
th=json.load(open("themes/imperial-red-gold-color-theme.json"));c=th["colors"];p=json.load(open("/tmp/pal.json"))
K,S,N,F,T,C,V,PU,PA,PR=p['red'],p['jade'],p['gold'],p['blue'],p['teal'],p['comment'],p['fg'],p['purple'],"#E8C9A0","#E6D3B0"
O=p['fg2']
def s(t,col,it=False):return f'<span style="color:{col};{"font-style:italic;" if it else ""}">{html.escape(t)}</span>'
L=[
[s("// 紫禁城 · 太和殿 —— 天下之中",C,1)],
[s("import",K),s(" { ",O),s("Tile",V),s(", ",O),s("Hall",V),s(" } ",O),s("from",K),s(" ",V),s("'./palace'",S),s(";",O)],
[],
[s("/** 宫殿营造则例 */",C,1)],
[s("export",K),s(" ",V),s("interface",K),s(" ",V),s("Palace",T),s(" {",O)],
[s("  title",PR),s(": ",O),s("string",T),s(";",O)],
[s("  dynasty",PR),s(": ",O),s("'明'",S),s(" | ",O),s("'清'",S),s(" | ",O),s("'清'",S),s(";",O)],
[s("  halls",PR),s(": ",O),s("number",T),s(";",O)],
[s("}",O)],
[],
[s("const",K),s(" ",V),s("MAX_TILES",N),s(" = ",O),s("9999",N),s(";",O)],
[],
[s("export",K),s(" ",V),s("class",K),s(" ",V),s("Forbidden",T),s(" ",V),s("extends",K),s(" ",V),s("Hall",T),s(" {",O)],
[s("  private",K),s(" ",V),s("tiles",PR),s(" = ",O),s("0",N),s(";",O)],
[],
[s("  async",K),s(" ",V),s("build",F),s("(",O),s("site",PA,1),s(": ",O),s("Palace",T),s(", ",O),s("gilded",PA,1),s(" = ",O),s("true",N),s("): ",O),s("Promise",T),s("<",O),s("void",T),s("> {",O)],
[s("    ",V),s("if",K),s(" (",O),s("this",PU,1),s(".",O),s("tiles",PR),s(" >= ",O),s("MAX_TILES",N),s(") ",O),s("return",K),s(";",O)],
[s("    ",V),s("// 琉璃瓦五色：黄、绿、蓝、黑、紫",C,1)],
[s("    ",V),s("const",K),s(" ",V),s("rank",V),s(" = ",O),s("site",PA,1),s(".",O),s("halls",PR),s(" > ",O),s("72",N),s(" ? ",O),s("'皇'",S),s(" : ",O),s("'王'",S),s(";",O)],
[s("    ",V),s("await",K),s(" ",V),s("Tile",T),s(".",O),s("lay",F),s("(",O),s("`${",S),s("site",PA,1),s(".",O),s("title",PR),s("}",S),s(" · ",S),s("${",S),s("rank",V),s("}`",S),s(", { ",O),s("gilded",PR),s(" });",O)],
[s("    ",V),s("this",PU,1),s(".",O),s("tiles",PR),s(" += ",O),s("gilded",PA,1),s(" ? ",O),s("2",N),s(" : ",O),s("1",N),s(";",O)],
[s("  }",O)],
[s("}",O)],
[],
[s("new",K),s(" ",V),s("Forbidden",T),s("().",O),s("build",F),s("({ ",O),s("title",PR),s(": ",O),s("'太和殿'",S),s(", ",O),s("dynasty",PR),s(": ",O),s("'清'",S),s(", ",O),s("halls",PR),s(": ",O),s("9999",N),s(" });",O)],
]
code="".join(f'<div class="ln{" cur" if i==18 else ""}"><span class="no" style="color:{c["editorLineNumber.activeForeground"] if i==18 else c["editorLineNumber.foreground"]}">{i+1}</span>{"".join(l)}</div>' for i,l in enumerate(L))
tree=[("▾ FORBIDDEN-CITY",0,c["sideBarSectionHeader.foreground"],0),("▾ src",1,V,0),("tiles.ts",2,c["gitDecoration.modifiedResourceForeground"],0),("palace.ts",2,c["gitDecoration.addedResourceForeground"],1),("hall.ts",2,V,0),("▸ assets",1,V,0),("README.md",1,V,0),("package.json",1,V,0),(".gitignore",1,c["gitDecoration.ignoredResourceForeground"],0)]
tr="".join(f'<div class="ti" style="padding-left:{14+d*14}px;color:{col};{"background:"+c["list.activeSelectionBackground"] if sel else ""}">{n}{" <b style=\"float:right;margin-right:12px;color:"+col+"\">M</b>" if n=="tiles.ts" else ""}{" <b style=\"float:right;margin-right:12px;color:"+col+"\">A</b>" if n=="palace.ts" else ""}</div>' for n,d,col,sel in tree)
term=f'''<div><span style="color:{p['jade']}">moco@紫禁城</span> <span style="color:{p['blue']}">~/forbidden-city</span> <span style="color:{p['red']}">$</span> npm run build</div>
<div style="color:{p['fg2']}">&gt; tsc -p . &amp;&amp; node dist/index.js</div>
<div><span style="color:{p['jade']}">✔</span> 编译成功 <span style="color:{p['gold']}">3 files</span> in <span style="color:{p['gold']}">412ms</span> · <span style="color:{p['red']}">0 errors</span></div>'''
H=f'''<html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1600px;height:1000px;font-family:"Noto Sans CJK SC","Noto Serif CJK SC",sans-serif;font-size:13px;background:{c["editor.background"]};color:{c["foreground"]};display:flex;flex-direction:column}}
.mono{{font-family:"DejaVu Sans Mono","Noto Sans CJK SC",monospace}}
.title{{height:36px;background:{c["titleBar.activeBackground"]};color:{c["titleBar.activeForeground"]};border-bottom:1px solid {c["titleBar.border"]};display:flex;align-items:center;justify-content:center;position:relative}}
.dots{{position:absolute;left:14px;display:flex;gap:8px}}.dots i{{width:12px;height:12px;border-radius:6px;display:block}}
.main{{flex:1;display:flex;min-height:0}}.act{{width:52px;background:{c["activityBar.background"]};border-right:1px solid {c["activityBar.border"]};padding-top:8px}}
.ai{{height:48px;display:flex;align-items:center;justify-content:center;font-size:20px;color:{c["activityBar.inactiveForeground"]}}}
.side{{width:270px;background:{c["sideBar.background"]};border-right:1px solid {c["sideBar.border"]}}}
.st{{padding:10px 14px;font-size:11px;letter-spacing:1px;color:{c["sideBarTitle.foreground"]}}}.ti{{height:24px;line-height:24px;font-size:13px}}
.ed{{flex:1;display:flex;flex-direction:column;min-width:0}}.tabs{{height:38px;background:{c["editorGroupHeader.tabsBackground"]};display:flex;border-bottom:1px solid {c["tab.border"]}}}
.tab{{padding:0 18px;line-height:37px;border-right:1px solid {c["tab.border"]};background:{c["tab.inactiveBackground"]};color:{c["tab.inactiveForeground"]}}}
.tab.a{{background:{c["tab.activeBackground"]};color:{c["tab.activeForeground"]};border-top:2px solid {c["tab.activeBorderTop"]};line-height:35px;height:38px}}
.bc{{padding:4px 20px;font-size:12px;color:{c["breadcrumb.foreground"]}}}
.code{{flex:1;padding-top:6px;font-size:15px;line-height:24px;overflow:hidden}}.ln{{white-space:pre;height:24px}}.ln.cur{{background:{c["editor.lineHighlightBackground"]}}}
.no{{display:inline-block;width:58px;text-align:right;padding-right:22px}}
.panel{{height:190px;background:{c["panel.background"]};border-top:1px solid {c["panel.border"]};padding:0 20px}}
.ph{{display:flex;gap:22px;font-size:11px;letter-spacing:1px;height:34px;align-items:center}}.ph span{{color:{c["panelTitle.inactiveForeground"]}}}
.ph .a{{color:{c["panelTitle.activeForeground"]};border-bottom:1px solid {c["panelTitle.activeBorder"]};padding-bottom:4px}}
.term{{font-size:14px;line-height:23px;color:{c["terminal.foreground"]}}}
.status{{height:26px;background:{c["statusBar.background"]};color:{c["statusBar.foreground"]};display:flex;align-items:center;font-size:12px}}
.status span{{padding:0 12px}}.rem{{background:{c["statusBarItem.remoteBackground"]};color:{c["statusBarItem.remoteForeground"]};height:26px;line-height:26px}}
.seal{{position:absolute;right:46px;top:96px;width:70px;height:70px;background:#9E1C1C;border:2px solid #E0B04A;box-shadow:inset 0 0 0 3px #9E1C1C,inset 0 0 0 4px #E0B04A88;color:#F3D58A;font-family:"Noto Serif CJK SC";font-size:24px;line-height:26px;text-align:center;padding-top:4px;opacity:.92;border-radius:4px;font-weight:700}}
body{{border:2px solid #B8862B}}
.title{{background:linear-gradient(#8E1C1C,#741414)!important;border-bottom:2px solid #B8862B!important;letter-spacing:1px}}
.status{{border-top:1px solid #B8862B}}
.cloud{{position:absolute;right:0;bottom:200px;width:420px;height:260px;opacity:.10;pointer-events:none}}
</style></head><body>
<div class="title"><div class="dots"><i style="background:#E0604A"></i><i style="background:#E0B04A"></i><i style="background:#5FA57A"></i></div>palace.ts — forbidden-city — 故宫 Imperial Red &amp; Gold</div>
<div class="main"><div class="act"><div class="ai" style="color:{c["activityBar.foreground"]};border-left:2px solid {c["activityBar.activeBorder"]}">❐</div><div class="ai">⌕</div><div class="ai" style="position:relative">⑂<b style="position:absolute;right:9px;top:26px;background:{c["activityBarBadge.background"]};color:{c["activityBarBadge.foreground"]};font-size:9px;border-radius:7px;padding:0 4px">2</b></div><div class="ai">▷</div><div class="ai">⊞</div></div>
<div class="side"><div class="st">资源管理器 EXPLORER</div>{tr}</div>
<div class="ed" style="position:relative"><div class="tabs"><div class="tab">tiles.ts</div><div class="tab a">palace.ts</div><div class="tab">README.md</div></div>
<div class="bc">src › palace.ts › Forbidden › build</div>
<div class="code mono">{code}</div><svg class="cloud" viewBox="0 0 420 260" fill="none" stroke="#E0B04A" stroke-width="3"><g id="c"><path d="M40 200 q0-40 40-40 q10-40 50-30 q20-30 55 0 q40-5 40 35 q30 5 25 35 z"/><path d="M90 180 q10-20 30-10 q15-20 35 0"/><circle cx="130" cy="150" r="10"/></g><use href="#c" x="170" y="-90"/><use href="#c" x="150" y="40" transform="scale(.9)"/></svg><div class="seal">故宫<br>御制</div>
<div class="panel"><div class="ph"><span>问题</span><span>输出</span><span class="a">终端 TERMINAL</span></div><div class="term mono">{term}</div></div></div></div>
<div class="status"><span class="rem">⟩⟨ 紫禁城</span><span>⑂ main*</span><span>⊗ 0 ⚠ 0</span><span style="margin-left:auto">行 19，列 32</span><span>UTF-8</span><span>TypeScript</span><span style="color:{p['redHi']}">●</span></div>
</body></html>'''
open("/tmp/preview.html","w").write(H)
