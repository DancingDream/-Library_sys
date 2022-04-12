import datetime

def bookStateFunction(self):
    resl =[]
    for item in self:
        if (item.state == True):
            # state = '在借中'
            reDate = ''
            tempDate = datetime.date.today()
        else:
            # state = '已归还'
            reDate = str(item.returnDate)
            tempDate = item.returnDate

        postponeDate = (item.borrowDate - tempDate).days
        if (postponeDate <= item.deadline):
             postpone = False   #未延期
        else:
            postpone = True  #已延期
            if(postponeDate > 2*item.deadline):  #更新禁用状态
                item.borrowerID.update(
                    banState = True
                )

        temp = {
            'borrowerID': item.borrowerID.userName,
            'borrowerBook': item.borrowerBook.bookName,
            'borrowDate': str(item.borrowDate),
            'returnDate': reDate,
            'state': item.state,
            'postpone': postpone
        }
        resl.append(temp)
    return resl