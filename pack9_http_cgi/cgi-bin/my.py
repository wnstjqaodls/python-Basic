import cgi

form = cgi.FieldStorage()  # 사용자가 전송한 자료를 py에서 받기
irum = form['name'].value  # java : request.getparameter("name")
nai = form['age'].value

print('content-type:text/html;charset=utf-8\n')
print('')
print("""
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
이름은 {0} , 나이는 {1}
<a href='../index.html'>메인으로</a>
</body>
</html>
""".format(irum,nai))