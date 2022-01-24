# 1. ^ 表示需要在行的开始处进行匹配. 例如, ^abc 可以匹配 abc123 但不匹配 123abc.
# 2. $ 表示需要在行的末端进行匹配. 例如, abc$ 可以匹配 123abc 但不能匹配 abc123.
# 3. \d可以匹配一个数字.'00\d'可以匹配'007'，但无法匹配'00A'.
# 4. {n}表示n个字符，用{n,m}表示n-m个字符. \d{3}表示匹配3个数字，例如'010'.
# 5. -P(grep): Interpret  the pattern as a Perl-compatible regular expression (PCRE).
# 6. | 表示或
# 7. \( 以及 \) 表示括号 而(  和)是括号本身

# grep -P  '^((([0-9]{3}-)|(\([0-9]{3}\) ))[0-9]{3}-[0-9]{4})$' file.txt
# PCRE(Perl Compatible Regular Expressions)是一个Perl库，包括 perl 兼容的正则表达式库。这些在执行正规表达式模式匹配时用与Perl 5
# 同样的语法和语义是很有用的。Boost太庞大了，使用boost regex后，程序的编译速度明显变慢。测试了一下，同样一个程序，
# 使用boost::regex编译时需要3秒，而使用pcre不到1秒。因此改用pcre来解决C语言中使用正则表达式的问题
grep -P '^(\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$' file.txt



grep -P "^(\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$" file.txt