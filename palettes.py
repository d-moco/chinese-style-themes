import os
_ROOT = os.path.dirname(os.path.abspath(__file__))
def seal(txt,bg,fg,right=40,top=20,extra=""):
    return f'<div class="deco" style="right:{right}px;top:{top}px;width:62px;height:62px;background:{bg};color:{fg};font-family:Noto Serif CJK SC;font-weight:700;font-size:22px;line-height:25px;text-align:center;padding-top:5px;border-radius:5px;z-index:3;{extra}">{txt}</div>'
mountains='''<svg class="deco" style="right:0;bottom:190px;z-index:1" width="900" height="380" viewBox="0 0 900 380">
<defs><linearGradient id="m" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9A9A92" stop-opacity=".22"/><stop offset="1" stop-color="#9A9A92" stop-opacity="0"/></linearGradient>
<linearGradient id="m2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C8C6BC" stop-opacity=".12"/><stop offset="1" stop-color="#C8C6BC" stop-opacity="0"/></linearGradient></defs>
<path d="M300 380 L420 170 Q450 120 480 160 L560 240 Q600 140 650 90 Q690 60 720 120 L800 230 Q840 190 900 200 L900 380Z" fill="url(#m2)"/>
<path d="M150 380 Q260 300 340 250 Q380 230 420 260 Q520 190 600 220 Q680 250 740 210 Q820 170 900 260 L900 380Z" fill="url(#m)"/></svg>'''
cloud_ribbon='''<svg class="deco" style="right:-20px;top:30px;z-index:1;opacity:.28" width="760" height="460" viewBox="0 0 760 460" fill="none" stroke-linecap="round">
<path d="M760 60 C620 20 560 160 430 120 S250 40 170 130 S60 200 20 170" stroke="#3E8FA8" stroke-width="10"/>
<path d="M760 90 C640 70 580 200 450 170 S270 100 200 180" stroke="#4FA07A" stroke-width="6"/>
<path d="M760 130 C660 130 600 250 480 230 S320 170 260 240 S180 300 140 280" stroke="#E0A848" stroke-width="3"/>
<g stroke="#E0A848" stroke-width="3"><path d="M560 330 q20-40 60-20 q20-30 55 0 q35 0 30 35 q-40 15-145-15z"/><path d="M600 330 q12-15 28-5"/><path d="M380 400 q15-30 45-15 q15-22 42 0 q25 0 22 25 q-30 12-109-10z"/></g></svg>'''
porcelain='''<svg class="deco" style="right:18px;top:0;z-index:1;opacity:.55" width="90" height="760" viewBox="0 0 90 760" fill="none" stroke="#2E5BA8" stroke-width="2">
<line x1="8" y1="0" x2="8" y2="760"/><line x1="82" y1="0" x2="82" y2="760"/><line x1="13" y1="0" x2="13" y2="760" stroke-width="1"/><line x1="77" y1="0" x2="77" y2="760" stroke-width="1"/>
<g id="u"><path d="M45 20 c-25 10 -25 40 0 50 c25 10 25 40 0 50" /><path d="M45 45 q-12 -6 -18 6 q6 12 18 6"/><path d="M45 95 q12 -6 18 6 q-6 12 -18 6"/><circle cx="45" cy="70" r="3" fill="#2E5BA8"/></g>
<use href="#u" y="100"/><use href="#u" y="200"/><use href="#u" y="300"/><use href="#u" y="400"/><use href="#u" y="500"/><use href="#u" y="600"/></svg>
<svg class="deco" style="right:140px;bottom:210px;z-index:1;opacity:.22" width="260" height="200" viewBox="0 0 260 200" fill="none" stroke="#2E5BA8" stroke-width="3">
<path d="M130 180 C90 140 90 80 130 40 C170 80 170 140 130 180Z"/><path d="M130 180 C70 160 40 110 50 70 C100 80 125 130 130 180Z"/><path d="M130 180 C190 160 220 110 210 70 C160 80 135 130 130 180Z"/><path d="M130 180 C60 185 10 160 0 130 C50 120 100 150 130 180Z"/><path d="M130 180 C200 185 250 160 260 130 C210 120 160 150 130 180Z"/></svg>'''
jiangnan='''<svg class="deco" style="right:0;bottom:190px;z-index:1;opacity:.5" width="760" height="300" viewBox="0 0 760 300">
<defs><linearGradient id="f" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff" stop-opacity="0"/><stop offset="1" stop-color="#ffffff" stop-opacity=".7"/></linearGradient></defs>
<g fill="#5E6670" opacity=".22"><path d="M180 200 L230 170 L330 170 L380 200Z"/><rect x="200" y="200" width="160" height="60" fill="#E4E6E2" stroke="#5E6670"/>
<path d="M360 170 L420 130 L560 130 L620 170Z"/><rect x="385" y="170" width="210" height="90" fill="#E4E6E2" stroke="#5E6670"/><rect x="470" y="200" width="30" height="40"/>
<path d="M590 210 L630 185 L720 185 L760 210Z"/><rect x="605" y="210" width="140" height="50" fill="#E4E6E2" stroke="#5E6670"/></g>
<path d="M0 270 Q380 250 760 275 L760 300 L0 300Z" fill="#7F9C8C" opacity=".18"/><rect width="760" height="300" fill="url(#f)"/></svg>
<svg class="deco" style="right:30px;top:0;z-index:1;opacity:.45" width="300" height="320" viewBox="0 0 300 320" fill="none" stroke="#6F9A62" stroke-width="1.6" stroke-linecap="round">
<path d="M280 0 Q240 120 250 300"/><path d="M200 0 Q170 100 185 230"/><path d="M240 0 Q200 90 215 190"/>
<g fill="#8DB07A" stroke="none" opacity=".7"><ellipse cx="248" cy="80" rx="3" ry="9" transform="rotate(20 248 80)"/><ellipse cx="243" cy="140" rx="3" ry="9" transform="rotate(-15 243 140)"/><ellipse cx="247" cy="200" rx="3" ry="9" transform="rotate(20 247 200)"/><ellipse cx="180" cy="70" rx="3" ry="9" transform="rotate(-20 180 70)"/><ellipse cx="178" cy="150" rx="3" ry="9" transform="rotate(15 178 150)"/><ellipse cx="210" cy="110" rx="3" ry="9" transform="rotate(25 210 110)"/><ellipse cx="208" cy="170" rx="3" ry="9" transform="rotate(-10 208 170)"/></g></svg>'''
cyber='''<div class="deco" style="right:60px;top:40px;z-index:1;font-family:Noto Serif CJK SC;font-weight:900;font-size:78px;line-height:84px;writing-mode:vertical-rl;color:transparent;-webkit-text-stroke:1.5px #FF3B5C;text-shadow:0 0 18px #FF3B5C88;opacity:.55">赛博国潮</div>
<svg class="deco" style="right:180px;top:30px;z-index:1;opacity:.8" width="90" height="170" viewBox="0 0 90 170" style="filter:drop-shadow(0 0 12px #FF3B5C)">
<line x1="45" y1="0" x2="45" y2="20" stroke="#FFC94D" stroke-width="2"/><rect x="28" y="18" width="34" height="8" rx="2" fill="#FFC94D"/>
<ellipse cx="45" cy="70" rx="38" ry="44" fill="#E0284A" opacity=".85" style="filter:drop-shadow(0 0 14px #FF3B5C)"/>
<g stroke="#FF8A9C" stroke-width="1.2" fill="none" opacity=".8"><ellipse cx="45" cy="70" rx="24" ry="44"/><ellipse cx="45" cy="70" rx="10" ry="44"/></g>
<text x="45" y="80" text-anchor="middle" font-family="Noto Serif CJK SC" font-weight="900" font-size="28" fill="#FFE29A">福</text>
<rect x="28" y="112" width="34" height="8" rx="2" fill="#FFC94D"/><g stroke="#FFC94D" stroke-width="1.5"><line x1="38" y1="120" x2="38" y2="160"/><line x1="45" y1="120" x2="45" y2="166"/><line x1="52" y1="120" x2="52" y2="160"/></g></svg>
<div class="deco" style="left:0;right:0;bottom:190px;height:2px;background:linear-gradient(90deg,transparent,#22E3C3,#FF3B5C,transparent);box-shadow:0 0 12px #22E3C3;z-index:3"></div>'''
THEMES=[
dict(id="ink-night",name="水墨·夜 Ink Night",dark=True,desc="水墨夜色深色主题：墨黑底、墨分五色的层层灰阶、象牙白正文，仅以一枚朱砂印红作关键字点睛，玉白与银灰写字符串。",
bg="#17181A",bg2="#121314",bg3="#0D0E0F",line="#202226",border="#2A2C30",input="#0D0E0F",fg="#E6E1D3",fg2="#9C9A92",dim="#6E6C66",lineno="#4A4A48",
accent="#D2483A",accentFg="#F5EFE2",kw="#E0594A",str="#A9C4B4",num="#D8CFB8",fn="#E6E1D3",type="#B8B6AE",deco="#C8A89A",param="#C9C3B4",prop="#BEB9AC",comment="#878580",
kwStyle=None,sel="#3A2A28",hl="#2E3432",find="#8A6A3A",err="#E0594A",warn="#C9A96A",add="#8FB09C",mod="#9AA4B0",title="#0D0E0F",titleFg="#B8B4A8",status="#0D0E0F",statusFg="#A8A498",
ansi=["#17181A","#D2483A","#9AB8A6","#C9B98A","#8E9CAA","#B79A9A","#9AB4B4","#C8C4B8","#5A5A56","#E66A5C","#B6D0C0","#E0D2A4","#AAB8C6","#D0B4B4","#B4CECE","#F0EADB"],
comments=("月落乌啼霜满天，江枫渔火对愁眠","墨分五色：焦、浓、重、淡、清","留白处，自有山水"),poem=("枫桥夜泊","姑苏城外寒山寺","夜半钟声到客船"),proj="ink-night",host="寒山",frame="none",
css=".code{font-weight:400}",deco_html=mountains+seal("墨<br>夜","#B8372B","#F5EFE2",extra="opacity:.9;box-shadow:inset 0 0 0 2px #B8372B,inset 0 0 0 3px #F5EFE266")),
dict(id="blue-white-porcelain",name="青花瓷 Blue & White Porcelain",dark=False,desc="青花瓷浅色主题：冷白瓷底、浓淡多层的青花蓝写代码，墨色正文，偶以釉里红点缀。",
bg="#F7F9FB",bg2="#EDF1F6",bg3="#E3E9F1",line="#E8EEF6",border="#CCD7E6",input="#FFFFFF",fg="#1C2430",fg2="#4A5668",dim="#6A7688",lineno="#9AA8BC",
accent="#1F4FA0",accentFg="#FFFFFF",kw="#1B3F8F",str="#3A6FB8",num="#B03A3A",fn="#1F5E9E",type="#28507E",deco="#6A4FA0",param="#3F4F6A",prop="#2F3F58",comment="#5E6E84",
kwStyle="bold",sel="#C9DAF2",hl="#DDE8F7",find="#E0B040",err="#B03A3A",warn="#9A6A10",add="#2E7A56",mod="#2E5BA8",title="#E3E9F1",titleFg="#1C2430",status="#1F3F7A",statusFg="#F2F6FC",
ansi=["#1C2430","#B03A3A","#2E7A56","#8A6A10","#1F4FA0","#6A4FA0","#1F6E8A","#6A7688","#4A5668","#C84A4A","#3A9068","#A07E20","#3A6FC0","#8466B8","#2E86A4","#9AA8BC"],
comments=("素胚勾勒出青花，笔锋浓转淡","瓶身描绘的牡丹，一如你初妆","釉色渲染仕女图，韵味被私藏"),poem=("青花瓷","天青色等烟雨","而我在等你"),proj="porcelain",host="景德镇",frame="3px double #2E5BA8",
css=".title{border-bottom:2px solid #2E5BA8!important}.status{border-top:2px solid #2E5BA8}",deco_html=porcelain+seal("青<br>花","#B03A3A","#FFF6F0",right=130,top=18,extra="opacity:.85")),
dict(id="dunhuang",name="敦煌 Dunhuang",dark=True,desc="敦煌壁画风深色主题：赭褐土色底，石青、石绿、朱砂、土黄与金色交织，取莫高窟飞天之色。",
bg="#2B1E16",bg2="#241912",bg3="#1D140E",line="#36271C",border="#47352A",input="#1D140E",fg="#F0E2C8",fg2="#C4AE90",dim="#8E7A64",lineno="#6E5A48",
accent="#E0A848",accentFg="#2B1E16",kw="#EF8A5A",str="#7DC4A0",num="#E8C070",fn="#6FB4D6",type="#9FD0C0",deco="#D8A0B0",param="#E4CCA8",prop="#DCCAB0",comment="#A88E70",
kwStyle=None,sel="#5A3E28",hl="#3E3424",find="#B07A28",err="#F07060",warn="#E8C070",add="#7DC4A0",mod="#6FB4D6",title="#5C2A1A",titleFg="#F0D49A",status="#3E5E6A",statusFg="#F6EAD2",
ansi=["#1D140E","#E0604A","#6FB48E","#E0A848","#5FA4C8","#C88AA0","#7CC0B4","#E0D0B4","#6E5A48","#F08A70","#90D0AE","#F0C470","#8AC4E0","#E0A8BC","#A0D8CC","#FFF2DA"],
comments=("飞天衣袂，绕梁三日","石青石绿，朱砂土黄","千年壁画，色不褪"),poem=("莫高窟","大漠孤烟直","长河落日圆"),proj="mogao",host="莫高窟",frame="2px solid #8A5A30",
css=".title{border-bottom:2px solid #E0A848!important}.status{border-top:2px solid #E0A848}",deco_html=cloud_ribbon+seal("敦<br>煌","#B8402A","#F6E2B0",top=360,extra="box-shadow:inset 0 0 0 2px #B8402A,inset 0 0 0 3px #E0A848")),
dict(id="jiangnan-mist",name="江南烟雨 Jiangnan Mist",dark=False,desc="江南烟雨浅色主题：粉墙黛瓦、烟灰青绿、柳绿、荷粉与黛蓝，低饱和而清晰可读。",
bg="#F2F3EF",bg2="#E8EAE5",bg3="#DDE0DA",line="#E8EBE5",border="#CDD2CB",input="#FAFBF8",fg="#2C3236",fg2="#555E62",dim="#737C7E",lineno="#A2AAA8",
accent="#4E6E86",accentFg="#FFFFFF",kw="#4E6382",str="#46703F",num="#A8506A",fn="#3E6A7A",type="#5E6A4A",deco="#8A5A78",param="#4E5A5E",prop="#3E4A4E",comment="#646D67",
kwStyle=None,sel="#D4DFDA",hl="#E2E8E0",find="#D8B46A",err="#A8445A",warn="#8A6A20",add="#4E7A4A",mod="#4E6E86",title="#DDE0DA",titleFg="#3A4246",status="#3A4246",statusFg="#E8EAE5",
ansi=["#2C3236","#A8445A","#4E7A4A","#8A6A20","#4E6382","#8A5A78","#3E6A7A","#737C7E","#555E62","#C0607A","#6A9662","#A88638","#6A80A0","#A47494","#5A8696","#A2AAA8"],
comments=("小楼一夜听春雨，深巷明朝卖杏花","粉墙黛瓦，烟雨朦胧","杨柳岸，晓风残月"),poem=("江南","江南好，风景旧曾谙","日出江花红胜火"),proj="jiangnan",host="乌镇",frame="none",
css="",deco_html=jiangnan+seal("烟<br>雨","#A8506A","#FBF2F4",top=330,right=60,extra="opacity:.75")),
dict(id="cyber-guochao",name="赛博国潮 Cyber Guochao",dark=True,desc="赛博国潮深色主题：近黑藏青底，霓虹中国红、霓虹金与青玉辉光，红灯笼与霓虹书法之感，亮而不刺眼。",
bg="#0E1220",bg2="#0A0D18",bg3="#070912",line="#161C30",border="#1E2640",input="#070912",fg="#E4E8F4",fg2="#9AA4C4",dim="#6A7498",lineno="#3E4870",
accent="#FF3B5C",accentFg="#0E1220",kw="#FF5C78",str="#3EE6C4",num="#FFC94D",fn="#5CC8FF",type="#FF9A5C",deco="#C88CFF",param="#E8C8D8",prop="#C4CCE4",comment="#7A84A8",
kwStyle=None,sel="#3A1A30",hl="#16304A",find="#FFC94D",err="#FF5C78",warn="#FFC94D",add="#3EE6C4",mod="#5CC8FF",title="#070912",titleFg="#FFC94D",status="#1A0A18",statusFg="#FFC94D",
ansi=["#0E1220","#FF3B5C","#3EE6C4","#FFC94D","#5CC8FF","#C88CFF","#22E3C3","#C4CCE4","#3E4870","#FF6A84","#7AF0D8","#FFDA80","#8AD8FF","#DAAAFF","#6AF0DA","#FFFFFF"],
comments=("霓虹映长安，灯笼照不夜城","红墙金瓦 × 赛博朋克","今夜，长安不眠"),poem=("不夜城","火树银花合","星桥铁锁开"),proj="neon-changan",host="长安",frame="1px solid #FF3B5C",
css=f".code span{{text-shadow:0 0 4px color-mix(in srgb,currentColor 55%,transparent)}}.code .no{{text-shadow:none}}.title{{border-bottom:1px solid #FF3B5C!important;box-shadow:0 0 12px #FF3B5C66;text-shadow:0 0 8px #FFC94D}}.status{{border-top:1px solid #FFC94D;box-shadow:0 0 12px #FFC94D55}}.tab.a{{box-shadow:0 -2px 10px #FF3B5C88}}",
deco_html=cyber),
]
_p=[t for t in THEMES if t['id']=="blue-white-porcelain"][0]
_p.update(ver="0.2.0",bg="#F7F9FD",bg2="#EAF0F9",bg3="#16388A",line="#E3ECF9",border="#B9CBE6",fg="#141C2E",fg2="#34466A",dim="#5A6C8E",lineno="#8DA2C6",
accent="#1A47B8",kw="#0B2F8F",str="#1C5BC4",num="#B4261C",fn="#0A54A8",type="#123E8A",deco="#5A2CA0",param="#2C3F72",prop="#1E2E58",comment="#4F6690",
sel="#BCD2F4",hl="#D6E4FA",title="#16388A",titleFg="#F2F6FF",status="#16388A",statusFg="#F2F6FF",
over={"activityBar.foreground":"#FFFFFF","activityBar.inactiveForeground":"#A9BEE8","activityBar.activeBorder":"#FFFFFF","activityBarBadge.background":"#C8342A","activityBarBadge.foreground":"#FFFFFF","activityBar.border":"#16388A",
"titleBar.inactiveBackground":"#2A4E9E","titleBar.inactiveForeground":"#C9D6F2","titleBar.border":"#0E2A70",
"sideBarSectionHeader.background":"#D3E0F5","sideBarSectionHeader.foreground":"#0B2F8F","sideBarTitle.foreground":"#0B2F8F","sideBar.border":"#B9CBE6",
"tab.activeBorderTop":"#1A47B8","tab.activeBorder":"#00000000","tab.activeForeground":"#0B2F8F","editorGroupHeader.tabsBackground":"#DCE6F6","tab.inactiveBackground":"#DCE6F6",
"statusBar.border":"#0E2A70","statusBarItem.remoteBackground":"#C8342A","statusBarItem.remoteForeground":"#FFFFFF","statusBarItem.hoverBackground":"#2A4E9E","statusBar.debuggingBackground":"#C8342A","statusBar.debuggingForeground":"#FFFFFF",
"panelTitle.activeForeground":"#0B2F8F","panelTitle.activeBorder":"#1A47B8","list.activeSelectionForeground":"#0B2F8F","editorLineNumber.activeForeground":"#1A47B8","focusBorder":"#1A47B8"},
css=".title{border-bottom:2px solid #0E2A70!important}",
deco_html=f'<img class="deco" src="file://{_ROOT}/decorations/images/porcelain-editor-corner.png" style="right:0;bottom:190px;opacity:.3;z-index:3">')
