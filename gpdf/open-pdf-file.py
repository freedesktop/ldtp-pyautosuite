#To open existing file
selectmenuitem ('PDFViewer', 'mnuFile;mnuOpen')
click ('dlgLoadfile', 'tbtnHome')
selectrow ('dlgLoadfile', 'tblFiles', 'sample.pdf')
click ('dlgLoadfile', 'btnOpen')
#To test the scroll actions
scrolldown ('PDFViewer', 'scrollBar')
scrollup ('PDFViewer', 'scrollBar')
scrollright ('PDFViewer', 'scrollBar')
scrolleft ('PDFViewer', 'scrollBar')
onedown ('PDFViewer', 'scrollBar', 2)
oneup ('PDFViewer', 'scrollBar', 2)
oneright ('PDFViewer', 'scrollBar', 1)
oneleft ('PDFViewer', 'scrollBar', 1)
