import json
P=dict(bg="#F5EEDC",bg2="#EDE4CC",bg3="#E4D9BC",line="#EFE6D0",border="#D8CBA8",
fg="#2B2622",fg2="#5A5048",ink="#1E1B18",cream="#F5EEDC",
red="#B0301F",redHi="#C0392B",jade="#2E6B4F",gold="#86600F",blue="#2F4A78",teal="#1F5C6B",
purple="#6B3E6E",comment="#76695A",selR="#E8C4B0",selJ="#CFE0CC")
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
"activityBar.background":p['bg3'],"activityBar.foreground":p['ink'],"activityBar.inactiveForeground":"#8F8370","activityBar.activeBorder":p['redHi'],"activityBarBadge.background":p['redHi'],"activityBarBadge.foreground":"#FFF8EC","activityBar.border":p['border'],
"sideBar.background":p['bg2'],"sideBar.foreground":p['fg'],"sideBar.border":p['border'],"sideBarTitle.foreground":p['fg2'],"sideBarSectionHeader.background":p['bg3'],"sideBarSectionHeader.foreground":p['fg'],
"list.activeSelectionBackground":p['selR'],"list.activeSelectionForeground":p['ink'],"list.inactiveSelectionBackground":p['bg3'],"list.hoverBackground":"#E6DCC2","list.focusOutline":p['redHi']+"88","list.highlightForeground":p['red'],"list.errorForeground":p['red'],"list.warningForeground":"#9A6512",
"statusBar.background":p['ink'],"statusBar.foreground":p['cream'],"statusBar.border":p['ink'],"statusBar.noFolderBackground":"#3A2E28","statusBar.debuggingBackground":p['redHi'],"statusBar.debuggingForeground":"#FFF8EC","statusBarItem.remoteBackground":p['redHi'],"statusBarItem.remoteForeground":"#FFF8EC","statusBarItem.hoverBackground":"#3A342E",
"panel.background":p['bg2'],"panel.border":p['border'],"panelTitle.activeForeground":p['ink'],"panelTitle.activeBorder":p['redHi'],"panelTitle.inactiveForeground":"#8A7E6E",
"terminal.background":p['bg2'],"terminal.foreground":p['fg'],"terminalCursor.foreground":p['redHi'],"terminal.selectionBackground":p['selR'],
"terminal.ansiBlack":"#2B2622","terminal.ansiRed":p['red'],"terminal.ansiGreen":p['jade'],"terminal.ansiYellow":p['gold'],"terminal.ansiBlue":p['blue'],"terminal.ansiMagenta":p['purple'],"terminal.ansiCyan":p['teal'],"terminal.ansiWhite":"#8A7E6E",
"terminal.ansiBrightBlack":"#5A5048","terminal.ansiBrightRed":p['redHi'],"terminal.ansiBrightGreen":"#3F8A66","terminal.ansiBrightYellow":"#A57A1C","terminal.ansiBrightBlue":"#3F62A0","terminal.ansiBrightMagenta":"#8A5590","terminal.ansiBrightCyan":"#2B7A8C","terminal.ansiBrightWhite":"#B3A68A",
"gitDecoration.addedResourceForeground":p['jade'],"gitDecoration.untrackedResourceForeground":"#3F8A66","gitDecoration.modifiedResourceForeground":p['blue'],"gitDecoration.deletedResourceForeground":p['red'],"gitDecoration.conflictingResourceForeground":p['purple'],"gitDecoration.ignoredResourceForeground":"#A89C86",
"button.background":p['redHi'],"button.foreground":"#FFF8EC","button.hoverBackground":p['red'],"button.secondaryBackground":p['bg3'],"button.secondaryForeground":p['fg'],
"input.background":"#FAF5E8","input.foreground":p['fg'],"input.border":p['border'],"input.placeholderForeground":"#A0947E","inputOption.activeBorder":p['redHi'],
"dropdown.background":"#FAF5E8","dropdown.border":p['border'],"checkbox.background":"#FAF5E8","checkbox.border":p['border'],
"badge.background":p['redHi'],"badge.foreground":"#FFF8EC","progressBar.background":p['redHi'],"scrollbarSlider.background":"#BFAF8A55","scrollbarSlider.hoverBackground":"#BFAF8A88","scrollbarSlider.activeBackground":"#A8976E99",
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
json.dump({"name":"水墨 Ink & Vermilion","type":"light","semanticHighlighting":True,"colors":colors,"tokenColors":tok,"semanticTokenColors":sem},open("themes/ink-vermilion-color-theme.json","w"),ensure_ascii=False,indent=2)
json.dump(p,open("/tmp/pal.json","w"))
