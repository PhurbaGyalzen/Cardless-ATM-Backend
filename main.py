
# Importing library
import qrcode


img = qrcode.make('{"atmCode":"BSN112", "bankName": "Rastra Banijya Bank","branchName":"Faika","bankCode":"SBANPKA","location":"Dillibazar"}')
img.save("qrcode1.png")
