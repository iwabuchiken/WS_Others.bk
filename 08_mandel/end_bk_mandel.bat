set cmd_1=C:\WORKS_2\a.bat && pushd C:\WORKS_2\WS\WS_Others.bk && git add -A && git commit -m ^"(bk : mandel) periodical updates^" && e && git push origin master
set cmd_2=C:\WORKS_2\a.bat && pushd C:\Users\iwabuchiken\Desktop\shortcuts_docs && git add -A && git commit -m ^"(shortcut_docs / bk : mandel) periodical updates^" && e && git push origin master

%cmd_1% && %cmd_2%


pause
