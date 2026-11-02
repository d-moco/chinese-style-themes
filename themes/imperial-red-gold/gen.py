import json
P=dict(bg="#2E1010",bg2="#240B0B",bg3="#1C0808",line="#3A1616",border="#4A1E1A",
fg="#F3E6C8",fg2="#C9B48E",ink="#FFF4DA",cream="#F3D58A",
red="#E8B547",redHi="#E0B04A",jade="#8CC7A1",gold="#F2A285",blue="#7FB2E0",teal="#7CC4BC",
purple="#D9A0C8",comment="#A88B6A",selR="#6B2A1E",selJ="#4A3A1A")
def lum(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    c=[x/12.92 if x<=.03928 else ((x+.055)/1.055)**2.4 for x in c]
    return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a,b):
    l=sorted([lum(a),lum(b)]);return (l[1]+.05)/(l[0]+.05)
for k in "fg fg2 red jade gold blue teal purple comment".split(): print(k,P[k],round(cr(P[k],P['bg']),2))
p=P
colors={
"focusBorder":p['redHi']+"99","foreground":p['fg'],"descriptionForeground":p['fg2'],"errorForeground":p['red'],"icon.foreground":p['fg2'],"widget.shadow":"#00000022","selection.background":p['selR'],
"editor.background":p['bg'],"editor.foreground":p['fg'],"editorLineNumber.foreground":"#B3A68A","editorLineNumber.activeForeground":p['red'],
"editorCursor.foreground":p['redHi'],"editor.selectionBackground":p['selR']+"CC","editor.inactiveSelectionBackground":p['selR']+"77","editor.selectionHighlightBackground":p['selJ']+"AA",
"editor.wordHighlightBackground":p['selJ']+"99","editor.wordHighlightStrongBackground":p['selR']+"99","editor.findMatchBackground":"#E9B44C88","editor.findMatchHighlightBackground":"#E9B44C44",
"editor.lineHighlightBackground":p['line'],"editor.lineHighlightBorder":"#00000000","editorIndentGuide.background1":"#E0D5B8","editorIndentGuide.activeBackground1":"#C2B28C",
"editorWhitespace.foreground":"#D4C8A8","editorRuler.foreground":"#E0D5B8","editorBracketMatch.background":p['selJ'],"editorBracketMatch.border":p['jade']+"88",
"editorBracketHighlight.foreground1":p['red'],"editorBracketHighlight.foreground2":p['blue'],"editorBracketHighlight.foreground3":p['jade'],"editorBracketHighlight.foreground4":p['gold'],
"editorError.foreground":p['redHi'],"editorWarning.foreground":"#B7791F","editorInfo.foreground":p['blue'],"editorLink.activeForeground":p['blue'],
"editorGutter.addedBackground":"#5E9C76","editorGutter.modifiedBackground":"#5B7DB1","editorGutter.deletedBackground":p['redHi'],
"editorWidget.background":p['bg2'],"editorWidget.border":p['border'],"editorSuggestWidget.background":p['bg2'],"editorSuggestWidget.border":p['border'],"editorSuggestWidget.selectedBackground":p['selR'],"editorSuggestWidget.highlightForeground":p['red'],
"editorHoverWidget.background":p['bg2'],"editorHoverWidget.border":p['border'],"editorGroupHeader.tabsBackground":p['bg2'],"editorGroup.border":p['border'],
"tab.activeBackground":p['bg'],"tab.activeForeground":p['ink'],"tab.activeBorderTop":p['redHi'],"tab.inactiveBackground":p['bg2'],"tab.inactiveForeground":"#7A6E60","tab.border":p['border'],"tab.hoverBackground":p['line'],
"titleBar.activeBackground":p['bg3'],"titleBar.activeForeground":p['fg'],"titleBar.inactiveBackground":p['bg2'],"titleBar.inactiveForeground":"#8A7E6E","titleBar.border":p['border'],
"activityBar.background":p['bg3'],"activityBar.foreground":p['ink'],"activityBar.inactiveForeground":"#8F8370","activityBar.activeBorder":p['redHi'],"activityBarBadge.background":p['redHi'],"activityBarBadge.foreground":"#2A0E0E","activityBar.border":p['border'],
"sideBar.background":p['bg2'],"sideBar.foreground":p['fg'],"sideBar.border":p['border'],"sideBarTitle.foreground":p['fg2'],"sideBarSectionHeader.background":p['bg3'],"sideBarSectionHeader.foreground":p['fg'],
"list.activeSelectionBackground":p['selR'],"list.activeSelectionForeground":p['ink'],"list.inactiveSelectionBackground":p['bg3'],"list.hoverBackground":"#E6DCC2","list.focusOutline":p['redHi']+"88","list.highlightForeground":p['red'],"list.errorForeground":p['red'],"list.warningForeground":"#9A6512",
"statusBar.background":p['ink'],"statusBar.foreground":p['cream'],"statusBar.border":p['ink'],"statusBar.noFolderBackground":"#3A2E28","statusBar.debuggingBackground":p['redHi'],"statusBar.debuggingForeground":"#2A0E0E","statusBarItem.remoteBackground":p['redHi'],"statusBarItem.remoteForeground":"#2A0E0E","statusBarItem.hoverBackground":"#3A342E",
"panel.background":p['bg2'],"panel.border":p['border'],"panelTitle.activeForeground":p['ink'],"panelTitle.activeBorder":p['redHi'],"panelTitle.inactiveForeground":"#8A7E6E",
"terminal.background":p['bg2'],"terminal.foreground":p['fg'],"terminalCursor.foreground":p['redHi'],"terminal.selectionBackground":p['selR'],
"terminal.ansiBlack":"#2B2622","terminal.ansiRed":p['red'],"terminal.ansiGreen":p['jade'],"terminal.ansiYellow":p['gold'],"terminal.ansiBlue":p['blue'],"terminal.ansiMagenta":p['purple'],"terminal.ansiCyan":p['teal'],"terminal.ansiWhite":"#8A7E6E",
"terminal.ansiBrightBlack":"#5A5048","terminal.ansiBrightRed":p['redHi'],"terminal.ansiBrightGreen":"#3F8A66","terminal.ansiBrightYellow":"#A57A1C","terminal.ansiBrightBlue":"#3F62A0","terminal.ansiBrightMagenta":"#8A5590","terminal.ansiBrightCyan":"#2B7A8C","terminal.ansiBrightWhite":"#B3A68A",
"gitDecoration.addedResourceForeground":p['jade'],"gitDecoration.untrackedResourceForeground":"#3F8A66","gitDecoration.modifiedResourceForeground":p['blue'],"gitDecoration.deletedResourceForeground":p['red'],"gitDecoration.conflictingResourceForeground":p['purple'],"gitDecoration.ignoredResourceForeground":"#A89C86",
"button.background":p['redHi'],"button.foreground":"#2A0E0E","button.hoverBackground":p['red'],"button.secondaryBackground":p['bg3'],"button.secondaryForeground":p['fg'],
"input.background":"#FAF5E8","input.foreground":p['fg'],"input.border":p['border'],"input.placeholderForeground":"#A0947E","inputOption.activeBorder":p['redHi'],
"dropdown.background":"#FAF5E8","dropdown.border":p['border'],"checkbox.background":"#FAF5E8","checkbox.border":p['border'],
"badge.background":p['redHi'],"badge.foreground":"#2A0E0E","progressBar.background":p['redHi'],"scrollbarSlider.background":"#BFAF8A55","scrollbarSlider.hoverBackground":"#BFAF8A88","scrollbarSlider.activeBackground":"#A8976E99",
"menu.background":p['bg2'],"menu.foreground":p['fg'],"menu.selectionBackground":p['selR'],"menu.border":p['border'],"quickInput.background":p['bg2'],"quickInputList.focusBackground":p['selR'],
"textLink.foreground":p['blue'],"textLink.activeForeground":p['red'],"textBlockQuote.background":p['bg2'],"textCodeBlock.background":p['bg2'],"breadcrumb.foreground":"#7A6E60","breadcrumb.focusForeground":p['ink'],
"minimap.background":p['bg'],"notifications.background":p['bg2'],"notifications.border":p['border'],"peekView.border":p['redHi'],"peekViewEditor.background":"#F8F2E4","peekViewResult.background":p['bg2'],"peekViewTitle.background":p['bg3'],
"diffEditor.insertedTextBackground":"#2E6B4F22","diffEditor.removedTextBackground":"#C0392B22"}
def t(scope,fg,fs=None):
    s={"foreground":fg}
    if fs: s["fontStyle"]=fs
    return {"scope":scope,"settings":s}
tok=[t(["comment","punctuation.definition.comment","string.comment"],p['comment'],"italic"),
t(["keyword","storage.type","storage.modifier","keyword.control","keyword.operator.new","keyword.operator.expression","keyword.operator.logical.python"],p['red']),
t(["keyword.operator","punctuation.separator","punctuation.terminator","meta.brace","punctuation"],p['fg2']),
t(["string","string.quoted","string.template","punctuation.definition.string"],p['jade']),
t(["constant.character.escape","string.regexp"],p['teal']),
t(["constant.numeric","constant.language","constant.other","support.constant","variable.other.constant","variable.other.enummember"],p['gold']),
t(["entity.name.function","support.function","meta.function-call entity.name.function","variable.function"],p['blue']),
t(["entity.name.type","entity.name.class","support.class","support.type","entity.other.inherited-class","storage.type.primitive","entity.name.namespace"],p['teal']),
t(["variable","variable.other.readwrite","meta.definition.variable"],p['fg']),
t(["variable.parameter"],"#5C4630","italic"),
t(["variable.language","variable.language.this","variable.language.self"],p['purple'],"italic"),
t(["entity.name.tag"],p['red']),t(["entity.other.attribute-name"],p['gold'],"italic"),
t(["meta.decorator","entity.name.function.decorator","punctuation.decorator"],p['purple']),
t(["support.type.property-name","meta.object-literal.key","variable.other.property","variable.other.object.property"],"#4A3F36"),
t(["markup.heading","entity.name.section"],p['red'],"bold"),t(["markup.bold"],p['ink'],"bold"),t(["markup.italic"],p['fg'],"italic"),
t(["markup.inline.raw","markup.fenced_code"],p['jade']),t(["markup.underline.link"],p['blue'],"underline"),
t(["markup.inserted"],p['jade']),t(["markup.deleted"],p['red']),t(["markup.changed"],p['blue']),t(["invalid"],p['redHi'],"underline")]
sem={"keyword":p['red'],"string":p['jade'],"number":p['gold'],"regexp":p['teal'],"comment":{"foreground":p['comment'],"italic":True},
"function":p['blue'],"method":p['blue'],"macro":p['purple'],"class":p['teal'],"interface":p['teal'],"enum":p['teal'],"struct":p['teal'],"type":p['teal'],"typeParameter":{"foreground":p['teal'],"italic":True},
"namespace":p['teal'],"parameter":{"foreground":"#5C4630","italic":True},"variable":p['fg'],"variable.readonly":p['gold'],"property":"#4A3F36","enumMember":p['gold'],"decorator":p['purple'],"*.deprecated":{"strikethrough":True},"selfKeyword":{"foreground":p['purple'],"italic":True}}
colors.update({
"editorLineNumber.foreground":"#7A5A48","editorLineNumber.activeForeground":"#E0B04A","editorIndentGuide.background1":"#43201A","editorIndentGuide.activeBackground1":"#7A5A3A","editorWhitespace.foreground":"#4A2A22","editorRuler.foreground":"#43201A",
"editorGutter.addedBackground":"#5FA57A","editorGutter.modifiedBackground":"#5E8FC0","editorGutter.deletedBackground":"#E0604A","editorError.foreground":"#FF7A66","editorWarning.foreground":"#E8B547","editorInfo.foreground":"#7FB2E0",
"editor.findMatchBackground":"#B8862B88","editor.findMatchHighlightBackground":"#B8862B44",
"tab.inactiveForeground":"#A88E6E","tab.hoverBackground":"#3A1414","titleBar.activeBackground":"#7E1616","titleBar.activeForeground":"#F3D58A","titleBar.inactiveBackground":"#5A1010","titleBar.inactiveForeground":"#C9A86A","titleBar.border":"#5A1010",
"activityBar.foreground":"#E0B04A","activityBar.inactiveForeground":"#9A7A5E","activityBarBadge.foreground":"#2A0E0E","list.hoverBackground":"#3A1616","list.warningForeground":"#E8B547","list.errorForeground":"#FF7A66",
"statusBar.background":"#7E1616","statusBar.foreground":"#F3D58A","statusBar.border":"#5A1010","statusBar.noFolderBackground":"#5A1010","statusBar.debuggingBackground":"#B8862B","statusBar.debuggingForeground":"#1C0808","statusBarItem.remoteBackground":"#E0B04A","statusBarItem.remoteForeground":"#2A0E0E","statusBarItem.hoverBackground":"#9A2222",
"panelTitle.inactiveForeground":"#A88E6E","terminal.ansiBlack":"#1C0808","terminal.ansiRed":"#F07A62","terminal.ansiWhite":"#D8C8A8","terminal.ansiBrightBlack":"#7A5A48","terminal.ansiBrightRed":"#FF9A82","terminal.ansiBrightGreen":"#A8DDB8","terminal.ansiBrightYellow":"#F8D27A","terminal.ansiBrightBlue":"#A0CAF0","terminal.ansiBrightMagenta":"#EBB8DA","terminal.ansiBrightCyan":"#9AD8D0","terminal.ansiCyan":"#7CC4BC","terminal.ansiYellow":"#E8B547","terminal.ansiBrightWhite":"#FFF4DA",
"gitDecoration.addedResourceForeground":"#8CC7A1","gitDecoration.untrackedResourceForeground":"#A8DDB8","gitDecoration.modifiedResourceForeground":"#E8C46A","gitDecoration.deletedResourceForeground":"#FF7A66","gitDecoration.ignoredResourceForeground":"#7A6050","gitDecoration.conflictingResourceForeground":"#D9A0C8",
"button.background":"#E0B04A","button.foreground":"#2A0E0E","button.hoverBackground":"#F0C35E","button.secondaryBackground":"#4A1E1A","button.secondaryForeground":"#F3E6C8","badge.foreground":"#2A0E0E",
"input.background":"#1C0808","input.placeholderForeground":"#8A6E58","dropdown.background":"#1C0808","checkbox.background":"#1C0808","scrollbarSlider.background":"#E0B04A22","scrollbarSlider.hoverBackground":"#E0B04A44","scrollbarSlider.activeBackground":"#E0B04A66",
"textLink.activeForeground":"#F0C35E","breadcrumb.foreground":"#A88E6E","peekViewEditor.background":"#250C0C","widget.shadow":"#00000066","focusBorder":"#E0B04A99",
"diffEditor.insertedTextBackground":"#5FA57A26","diffEditor.removedTextBackground":"#E0604A30","editorBracketHighlight.foreground1":"#E0B04A","editorBracketHighlight.foreground3":"#8CC7A1","editorBracketHighlight.foreground4":"#F2A285"})
for x in tok:
    if x["settings"]["foreground"]=="#5C4630": x["settings"]["foreground"]="#E8C9A0"
    if x["settings"]["foreground"]=="#4A3F36": x["settings"]["foreground"]="#E6D3B0"
sem["parameter"]["foreground"]="#E8C9A0"; sem["property"]="#E6D3B0"
json.dump({"name":"故宫 Imperial Red & Gold","type":"dark","semanticHighlighting":True,"colors":colors,"tokenColors":tok,"semanticTokenColors":sem},open("themes/imperial-red-gold-color-theme.json","w"),ensure_ascii=False,indent=2)
json.dump(p,open("/tmp/pal.json","w"))
