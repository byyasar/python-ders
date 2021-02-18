import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPSConnection("mebbis.meb.gov.tr")
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=txtKullaniciAd;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("10864385892"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=txtSifre;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("Yb200280+"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=__RequestVerificationToken;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("nL7gLAK3TTtVZELDS_fUzLqqBXWhZlYecRm7uXEUp_BIyf2FKirl5oZfe-b4xEXnL7wY595DLIX7-yfzv4gPR3CVtSgEOljomf1JHzZBB_81"))
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body

conn.request("POST", "/default.aspx", payload)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))