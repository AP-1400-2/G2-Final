import sys,os
sys.path.append('../onlineShop')
from DataLayer.Context.UnitOfWork import context
from Tools.Validations.loginValid import loginValid
from Tools.Validations.editValid import editValid
from DataLayer.Tables.operatorTabels import operatorTabels
from DataLayer.Tables.usersTable import userTable
from DataLayer.Tables.catTable import catTable
from DataLayer.Tables.productTable import productTable


from PyQt5.QtWidgets import QLabel , QPushButton , QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

db = context()

class Operator:
    def __init__(self):
        pass
    
    @property
    def FindOperatorID(self):
        return db.OperatorRepository.GetIDByEmail(self.Email)[0][0]    

    def Login(self,email,password,instance):
        self.Email = email
        self.Password = password
        # validation for login page
        validation = loginValid(self.Email,self.Password,db).operatorValidate()
        if(validation == 0):
            instance.wrongEmail_lbl.setHidden(True)
            instance.okLoign_lbl.setHidden(True)
            instance.wrongPass_lbl.setHidden(True)
            instance.wrongFields_lbl.setHidden(False)
            return False
        elif(validation == 1):
            instance.wrongEmail_lbl.setHidden(False)
            instance.okLoign_lbl.setHidden(True)
            instance.wrongPass_lbl.setHidden(True)
            instance.wrongFields_lbl.setHidden(True)
            return False
        elif(validation == 2):
            instance.wrongEmail_lbl.setHidden(True)
            instance.okLoign_lbl.setHidden(True)
            instance.wrongPass_lbl.setHidden(False)
            instance.wrongFields_lbl.setHidden(True)
            return False
        elif(validation == 3):
            instance.wrongEmail_lbl.setHidden(False)
            instance.okLoign_lbl.setHidden(True)
            instance.wrongPass_lbl.setHidden(True)
            instance.wrongFields_lbl.setHidden(True)
            return True
    
    def viewAllUsersSection(self,instance):
        AllUsersInfo = db.userRepository.GetAll()
        instance.count_lbl.setText(f"تعداد کاربران فروشگاه : {len(AllUsersInfo)}")
        radif_dict = {}
        userName_dict = {}
        email_dict = {}
        password_dict = {}
        date_dict = {}
        randomID_dict = {}
        btn_del = {}
        btn_dt = {}
        height = 230
        height2 = 240
        index = 0
        for i in AllUsersInfo:
            userID = i[0]
            userName = i[1]
            email = i[2]
            password = i[3]
            date = i[4]
            randomID = i[5]
            # ---- createDynamic ----
            radif_dict[index] = QPushButton(instance)
            radif_dict[index].setText(f"{index}")
            radif_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            radif_dict[index].setGeometry(1040,height,81,71)
            radif_dict[index].setObjectName(f"showFaveLbl_{userID}")
            # -------
            userName_dict[index] = QPushButton(instance)
            userName_dict[index].setText(f"{userName}")
            userName_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            userName_dict[index].setGeometry(920,height,121,71)
            userName_dict[index].setObjectName(f"userName_{userID}")
            # -------
            email_dict[index] = QPushButton(instance)
            email_dict[index].setText(f"{email}")
            email_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            email_dict[index].setGeometry(740,height,181,71)
            email_dict[index].setObjectName(f"Email_{userID}")
            # -------
            password_dict[index] = QPushButton(instance)
            password_dict[index].setText(f"{password}")
            password_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            password_dict[index].setGeometry(610,height,131,71)
            password_dict[index].setObjectName(f"Password_{userID}")
            # -------
            date_dict[index] = QPushButton(instance)
            date_dict[index].setText(f"{date}")
            date_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            date_dict[index].setGeometry(480,height,131,71)
            date_dict[index].setObjectName(f"Date_{userID}")
            # -------
            randomID_dict[index] = QPushButton(instance)
            randomID_dict[index].setText(f"{randomID}")
            randomID_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            randomID_dict[index].setGeometry(350,height,131,71)
            randomID_dict[index].setObjectName(f"RandomID{userID}")
            # -------
            btn_del[index] = QPushButton(instance)
            btn_del[index].setText(f"حذف")
            btn_del[index].setStyleSheet("QPushButton {border-radius : 10%;background-color: #e0270f;color : #fff;font: 10pt 'IRANSans';}")
            btn_del[index].setGeometry(140,height2,91,51)
            btn_del[index].setObjectName(f"userDeleteBtn_{userID}")
            btn_del[index].setCursor(Qt.PointingHandCursor)
            # -------
            btn_dt[index] = QPushButton(instance)
            btn_dt[index].setText("مشاهده")
            btn_dt[index].setStyleSheet("QPushButton {border-radius : 10%;background-color: #1cc275;color : #fff;font: 10pt 'IRANSans';}")
            btn_dt[index].setGeometry(240,height2,101,51)
            btn_dt[index].setObjectName(f"userDetailsBtn_{userID}")
            btn_dt[index].setCursor(Qt.PointingHandCursor)
            # ------
            height += 70
            height2 += 70
            index += 1
            
        num = len(btn_del)
        for i in range(num,20):
            btn_del[i] = QPushButton(instance)
            btn_dt[i] = QPushButton(instance)
            btn_del[i].setHidden(True)
            btn_dt[i].setHidden(True)
            
        #  deleteFavorit btn click functions
        btn_del[0].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[0].objectName()))
        btn_del[1].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[1].objectName()))
        btn_del[2].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[2].objectName()))
        btn_del[3].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[3].objectName()))
        btn_del[4].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[4].objectName()))
        btn_del[5].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[5].objectName()))
        btn_del[6].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[6].objectName()))
        btn_del[7].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[7].objectName()))
        btn_del[8].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[8].objectName()))
        btn_del[9].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[9].objectName()))
        btn_del[10].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_del[10].objectName()))

        
        btn_dt[0].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[0].objectName()))
        btn_dt[1].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[1].objectName()))
        btn_dt[2].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[2].objectName()))
        btn_dt[3].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[3].objectName()))
        btn_dt[4].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[4].objectName()))
        btn_dt[5].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[5].objectName()))
        btn_dt[6].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[6].objectName()))
        btn_dt[7].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[7].objectName()))
        btn_dt[8].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[8].objectName()))
        btn_dt[9].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[9].objectName()))
        btn_dt[10].clicked.connect(lambda: instance.OpenViewAccountUI(btn_dt[10].objectName()))

    def viewAllProductsSection(self,instance):
        AllProductsInfo = db.ProductsRepository.GetAll()
        instance.count_lbl.setText(f"تعداد محصولات فروشگاه : {len(AllProductsInfo)}")
        radif_dict = {}
        productName_dict = {}
        productDetails_dict = {}
        cat_dict = {}
        price_dict = {}
        date_dict = {}
        randomID_dict = {}
        saler_dict = {}
        # btn_delete = {}
        # lbl_delete = {}
        btn_edit = {}
        lbl_edit = {}
        height = 230
        height2 = 240
        index = 0
        for i in AllProductsInfo:
            productID = i[0]
            productName = i[1]
            productDetail = i[2]
            price = i[3]
            date = i[4]
            randomID = i[5]
            salerID = i[6]
            catID = i[7]
            findSalerName = db.SalerRepository.GetSalerNameByID(salerID)[0][0]
            findCatName = db.CatRepository.GetCatNameById(catID)[0][0]
            # ---- createDynamic ----
            radif_dict[index] = QPushButton(instance)
            radif_dict[index].setText(f"{index}")
            radif_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            radif_dict[index].setGeometry(1040,height,81,71)
            radif_dict[index].setObjectName(f"showFaveLbl_{productID}")
            # -------
            productName_dict[index] = QPushButton(instance)
            productName_dict[index].setText(f"{productName}")
            productName_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            productName_dict[index].setGeometry(920,height,121,71)
            productName_dict[index].setObjectName(f"userName_{productID}")
            # -------
            productDetails_dict[index] = QPushButton(instance)
            productDetails_dict[index].setText(f"... {productDetail[0:20]}")
            productDetails_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            productDetails_dict[index].setGeometry(720,height,201,71)
            productDetails_dict[index].setObjectName(f"Email_{productID}")
            # -------
            cat_dict[index] = QPushButton(instance)
            cat_dict[index].setText(f"{findCatName}")
            cat_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            cat_dict[index].setGeometry(610,height,111,71)
            cat_dict[index].setObjectName(f"Email_{productID}")
            # -------
            price_dict[index] = QPushButton(instance)
            price_dict[index].setText(f"{price}")
            price_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            price_dict[index].setGeometry(520,height,91,71)
            price_dict[index].setObjectName(f"Password_{productID}")
            # -------
            date_dict[index] = QPushButton(instance)
            date_dict[index].setText(f"{date}")
            date_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            date_dict[index].setGeometry(430,height,91,71)
            date_dict[index].setObjectName(f"Date_{productID}")
            # -------
            randomID_dict[index] = QPushButton(instance)
            randomID_dict[index].setText(f"{randomID}")
            randomID_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            randomID_dict[index].setGeometry(320,height,111,71)
            randomID_dict[index].setObjectName(f"RandomID{productID}")
            # -------
            saler_dict[index] = QPushButton(instance)
            saler_dict[index].setText(f"{findSalerName}")
            saler_dict[index].setStyleSheet("QPushButton {background-color : #fff ; border:1px solid #000;}")
            saler_dict[index].setGeometry(200,height,121,71)
            saler_dict[index].setObjectName(f"RandomID{productID}")
            # ---create remove icon lbl
            # lbl_delete[index] = QLabel(instance)
            # lbl_delete[index].setGeometry(100,height+10,51,51)
            # lbl_delete[index].setObjectName(f"removeIconLbl_{productID}")
            # img = QPixmap(os.getcwd()+"\\Tools\\imgs\\deleteIcon.jpg")
            # lbl_delete[index].setPixmap(img)
            # # ---create remove icon btn
            # btn_delete[index] = QPushButton(instance)
            # btn_delete[index].setGeometry(100,height+10,51,51)
            # btn_delete[index].setObjectName(f"removeIconbtn_{productID}")
            # btn_delete[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
            # btn_delete[index].setCursor(Qt.PointingHandCursor)
            # ---create edit icon lbl
            lbl_edit[index] = QLabel(instance)
            lbl_edit[index].setGeometry(150,height+10,51,51)
            lbl_edit[index].setObjectName(f"editIconLbl_{productID}")
            img = QPixmap(os.getcwd()+"\\Tools\\imgs\\editIcon.jpg")
            lbl_edit[index].setPixmap(img)
            # ---create edit icon btn
            btn_edit[index] = QPushButton(instance)
            btn_edit[index].setGeometry(150,height+10,51,51)
            btn_edit[index].setObjectName(f"editIconbtn_{productID}")
            btn_edit[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
            btn_edit[index].setCursor(Qt.PointingHandCursor)
            # ------
            height += 70
            height2 += 70
            index += 1
            
        # num = len(btn_delete)
        # for i in range(num,20):
        #     btn_delete[i] = QPushButton(instance)
        #     btn_delete[i].setHidden(True)
            
        num = len(btn_edit)
        for i in range(num,20):
            btn_edit[i] = QPushButton(instance)
            btn_edit[i].setHidden(True)
            
        #  btn_delete click functions
        # btn_delete[0].clicked.connect(lambda: instance.goToDeleteUserFromDB(btn_delete[0].objectName()))

        #  btn_edit click functions
        btn_edit[0].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[0].objectName()))
        btn_edit[1].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[1].objectName()))
        btn_edit[2].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[2].objectName()))
        btn_edit[3].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[3].objectName()))
        btn_edit[4].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[4].objectName()))
        btn_edit[5].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[5].objectName()))
        btn_edit[6].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[6].objectName()))
        btn_edit[7].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[7].objectName()))
        btn_edit[8].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[8].objectName()))
        btn_edit[9].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[9].objectName()))
        btn_edit[10].clicked.connect(lambda: instance.OpenEditProductUI(btn_edit[10].objectName()))
    
    def viewDiscountCode(self):
        pass
    
    def viewCatDetailsUI(self,instance):
        mainCat_dict = {}
        subCat_dict = {}
        edit_lbl = {}
        edit_btn = {}
        main_width = 700
        main_height = 20
        sub_width = 620
        index = 0
        getMainCats = db.CatRepository.getMainCats()
        for main in getMainCats:
            if(main_width < 0 ):
                main_width = 700
                sub_width = 620
                main_height += 290
            sub_height = main_height + 40
            mainCatID = main[0]
            findMainCatName = db.CatRepository.GetCatNameById(mainCatID)[0][0]
            # ---- create main cat lbl ----
            mainCat_dict[index] = QLabel(instance)
            mainCat_dict[index].setText(f"{findMainCatName}")
            mainCat_dict[index].setStyleSheet("QLabel {font: 15pt 'B Koodak';}")
            mainCat_dict[index].setGeometry(main_width,main_height,161,41)
            mainCat_dict[index].setObjectName(f"mainCat_{mainCatID}")
            
            # ---- ceate edit lbl ----
            edit_lbl[index] = QLabel(instance)
            edit_lbl[index].setGeometry(main_width+170,main_height,51,41)
            edit_lbl[index].setObjectName(f"editlbl_{mainCatID}")
            img = QPixmap(os.getcwd()+"\\Tools\\imgs\\editIcon.jpg")
            edit_lbl[index].setPixmap(img)
            # ---- ceate edit btn ----
            edit_btn[index] = QPushButton(instance)
            edit_btn[index].setGeometry(main_width+170,main_height,51,41)
            edit_btn[index].setObjectName(f"editbtn_{mainCatID}")
            edit_btn[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
            edit_btn[index].setCursor(Qt.PointingHandCursor)
            
            
            # ---- find and create subcats ----
            getSubCats = db.CatRepository.GetAllSubCatbyID(mainCatID)
            for sub in getSubCats:
                subCatID = sub[0]
                findSubCatName = db.CatRepository.GetCatNameById(subCatID)[0][0]
                subCat_dict[index] = QLabel(instance)
                subCat_dict[index].setText(f"{findSubCatName}")
                subCat_dict[index].setStyleSheet("QLabel {font: 15pt 'B nazanin';}")
                subCat_dict[index].setGeometry(sub_width,sub_height,161,41)
                subCat_dict[index].setObjectName(f"subCat_{mainCatID}")
                sub_height += 40
            main_width -= 300
            sub_width -= 300
            index += 1
            
        num = len(edit_btn)
        for i in range(num,20):
            edit_btn[i] = QPushButton(instance)
            edit_btn[i].setHidden(True)
        
        edit_btn[0].clicked.connect(lambda: instance.openEditCatUI(edit_btn[0].objectName()))
        edit_btn[1].clicked.connect(lambda: instance.openEditCatUI(edit_btn[1].objectName()))
        edit_btn[2].clicked.connect(lambda: instance.openEditCatUI(edit_btn[2].objectName()))
        edit_btn[3].clicked.connect(lambda: instance.openEditCatUI(edit_btn[3].objectName()))
        edit_btn[4].clicked.connect(lambda: instance.openEditCatUI(edit_btn[4].objectName()))
        edit_btn[5].clicked.connect(lambda: instance.openEditCatUI(edit_btn[5].objectName()))
        edit_btn[6].clicked.connect(lambda: instance.openEditCatUI(edit_btn[6].objectName()))
        edit_btn[7].clicked.connect(lambda: instance.openEditCatUI(edit_btn[7].objectName()))
        edit_btn[8].clicked.connect(lambda: instance.openEditCatUI(edit_btn[8].objectName()))
        edit_btn[9].clicked.connect(lambda: instance.openEditCatUI(edit_btn[9].objectName()))
        edit_btn[10].clicked.connect(lambda: instance.openEditCatUI(edit_btn[10].objectName()))
                    
    def editCatDetails(self,mainCatID,instance):
        findMainCatName = db.CatRepository.GetCatNameById(mainCatID)[0][0]
        subCatlbl_dict = {}
        instance.subCatInput_dict = {}
        removeIconlbl_dict = {}
        removeIconbtn_dict = {}
        index = 0
        height = 100
        # create subcat
        findAllSubcats = db.CatRepository.GetAllSubCatbyID(mainCatID)
        for s in findAllSubcats:
            subcatID = s[0]
            # --- create subCat_lbl ----
            subCatlbl_dict[index] = QLabel(instance)
            subCatlbl_dict[index].setGeometry(900,height,121,41)
            subCatlbl_dict[index].setObjectName(f"subcatlbl_{subcatID}")
            subCatlbl_dict[index].setText(f"زیر شاخه {index+1} : ")
            subCatlbl_dict[index].setStyleSheet("QLabel {font: 15pt 'B nazanin';}")
            # --- create subCat_btn ----
            findSubCatName = db.CatRepository.GetCatNameById(subcatID)[0][0]
            instance.subCatInput_dict[index] = QLineEdit(instance)
            instance.subCatInput_dict[index].setGeometry(540,height,301,51)
            instance.subCatInput_dict[index].setObjectName(f"CatInput_{subcatID}")
            instance.subCatInput_dict[index].setStyleSheet("QLineEdit { border : 1px solid #b1afaf; border-radius : 10%;font: 12pt 'Century Gothic';} QLineEdit:focus {border : 1px solid #df2569;}")
            instance.subCatInput_dict[index].setText(findSubCatName)
            # ---create remove icon lbl
            removeIconlbl_dict[index] = QLabel(instance)
            removeIconlbl_dict[index].setGeometry(460,height,51,51)
            removeIconlbl_dict[index].setObjectName(f"removeIconLbl_{subcatID}")
            img = QPixmap(os.getcwd()+"\\Tools\\imgs\\deleteIcon.jpg")
            removeIconlbl_dict[index].setPixmap(img)
            # ---create remove icon btn
            removeIconbtn_dict[index] = QPushButton(instance)
            removeIconbtn_dict[index].setGeometry(460,height,51,51)
            removeIconbtn_dict[index].setObjectName(f"removeIconbtn_{subcatID}")
            removeIconbtn_dict[index].setStyleSheet("QPushButton { background-color : transparent; border : none;}")
            removeIconbtn_dict[index].setCursor(Qt.PointingHandCursor)
            # -------
            index += 1
            height += 70
            
        # ---- create mainCat_input ----
        instance.subCatInput_dict[index] = QLineEdit(instance)
        instance.subCatInput_dict[index].setGeometry(540,20,301,51)
        instance.subCatInput_dict[index].setObjectName(f"CatInput_{mainCatID}")
        instance.subCatInput_dict[index].setStyleSheet("QLineEdit { border : 1px solid #b1afaf; border-radius : 10%;font: 12pt 'Century Gothic';} QLineEdit:focus {border : 1px solid #df2569;}")
        instance.subCatInput_dict[index].setText(findMainCatName)
        
        # --- crate mainCat_lbl ----
        subCatlbl_dict[index] = QLabel(instance)
        subCatlbl_dict[index].setGeometry(870,20,201,41)
        subCatlbl_dict[index].setObjectName("mainCatLbl")
        subCatlbl_dict[index].setText(f"عنوان شاخه اصلی : ")
        subCatlbl_dict[index].setStyleSheet("QLabel {font: 18pt 'B Koodak';}")
        height = 110
                    
        num = len(removeIconbtn_dict)
        for i in range(num,20):
            removeIconbtn_dict[i] = QPushButton(instance)
            removeIconbtn_dict[i].setHidden(True)
            
        
        removeIconbtn_dict[0].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[0].objectName()))
        removeIconbtn_dict[1].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[1].objectName()))
        removeIconbtn_dict[2].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[2].objectName()))
        removeIconbtn_dict[3].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[3].objectName()))
        removeIconbtn_dict[4].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[4].objectName()))
        removeIconbtn_dict[5].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[5].objectName()))
        removeIconbtn_dict[6].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[6].objectName()))
        removeIconbtn_dict[7].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[7].objectName()))
        removeIconbtn_dict[8].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[8].objectName()))
        removeIconbtn_dict[9].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[9].objectName()))
        removeIconbtn_dict[10].clicked.connect(lambda: instance.OpenConfirmRemoveSubCatUI(removeIconbtn_dict[10].objectName()))
        
    def confirmEditcat(self,instance):
        num = len(instance.subCatInput_dict)
        for i in range(num):
            findInput_objName = instance.subCatInput_dict[i].objectName()
            findInputID = findInput_objName.split("_")[1]
            findInputText = instance.subCatInput_dict[i].text()
            newCat = catTable(findInputID,findInputText)
            db.CatRepository.Update(newCat)
            db.CatRepository.Save()
        return True
            
    def addNewSubCat(self,mainCatID,instance):
        getInputText = instance.addNewSubCat_input.text()     
        if(getInputText == ""):
            instance.wrong_lbl.setHidden(False)
        else:
            instance.wrong_lbl.setHidden(True)
            newCat = catTable(mainCatID,getInputText)
            db.CatRepository.createSubCat(newCat)
            db.CatRepository.Save()
            return True
    
    def removeSubCat(self,subcatID):
        db.CatRepository.Delete(subcatID)  
        db.CatRepository.Save()
        return True

    def addNewMainCat(self,instance):
        getInputText = instance.addNewSubCat_input.text()     
        if(getInputText == ""):
            instance.wrong_lbl.setHidden(False)
        else:
            instance.wrong_lbl.setHidden(True)
            newCat = catTable(0,getInputText)
            db.CatRepository.CreateMainCat(newCat)
            db.CatRepository.Save()
            return True
         
    def removeMainCat(self,mainID):
        getAllSubCat = db.CatRepository.GetAllSubCatbyID(mainID)
        for i in getAllSubCat:
            subCatID = i[0]
            db.CatRepository.Delete(subCatID)
        db.CatRepository.Delete(mainID)
        db.CatRepository.Save()
        return True 
            
    def ViewOperatorDetails(self,ID,instance):
        findAllOperatorDetails = db.OperatorRepository.GetByID(ID)
        for detail in findAllOperatorDetails:
            userName = detail[1]
            email = detail[2]
            password = detail[3]
            randomID = detail[4]
            date = detail[5]
        instance.viewAc.show_userName.setText(f"{userName}")
        instance.viewAc.show_email.setText(f"{email}")
        instance.viewAc.show_password.setText(f"{password}")
        instance.viewAc.show_date.setText(f"{date}")
        instance.viewAc.show_randomID.setText(f"{randomID}")
        
    def EditOperatorInformation(self,OperatorID,userName,email,oldPass,dbPass,newPass,instance):
        findAllUserInfo = db.OperatorRepository.GetByID(OperatorID)
        validation = editValid(oldPass,dbPass,newPass).operatorValidate()
        if(validation == 0):
            instance.viewAc.wrongOldPass_lbl.setHidden(False)
            instance.viewAc.notEqualPass_lbl.setHidden(True)
            instance.viewAc.shouldEnterNewPass_lbl.setHidden(True)
            instance.viewAc.okEdit_lbl.setHidden(True)
            return False
        elif(validation == 1):
            instance.viewAc.wrongOldPass_lbl.setHidden(True)
            instance.viewAc.notEqualPass_lbl.setHidden(True)
            instance.viewAc.shouldEnterNewPass_lbl.setHidden(False)
            instance.viewAc.okEdit_lbl.setHidden(True)
            return False
        elif(validation == 2):
            instance.viewAc.wrongOldPass_lbl.setHidden(True)
            instance.viewAc.notEqualPass_lbl.setHidden(False)
            instance.viewAc.shouldEnterNewPass_lbl.setHidden(True)
            instance.viewAc.okEdit_lbl.setHidden(True)
            return False
        elif(validation == 3):
            # successful edit user info
            instance.viewAc.wrongOldPass_lbl.setHidden(True)
            instance.viewAc.notEqualPass_lbl.setHidden(True)
            instance.viewAc.shouldEnterNewPass_lbl.setHidden(True)
            instance.viewAc.okEdit_lbl.setHidden(False)
            updateOperator = operatorTabels(userName,email,newPass,findAllUserInfo[0][4],findAllUserInfo[0][5])
            db.OperatorRepository.Update(updateOperator,OperatorID)
            db.OperatorRepository.Save()
            return True
         
    def EditProductDetails(self,productID,instance):
        productName = db.ProductsRepository.GetProductNameByID(productID)[0][0]
        productPrice = db.ProductsRepository.GetPriceByID(productID)[0][0]
        productDate = db.ProductsRepository.GetDateByID(productID)[0][0]
        productRandomID = db.ProductsRepository.GetRandomID(productID)[0][0]
        productDetails = db.ProductsRepository.GetDetailsByID(productID)[0][0]
        salerID = db.ProductsRepository.GetSalerIDByID(productID)[0][0]
        salerName = db.SalerRepository.GetSalerNameByID(salerID)[0][0]
        catID = db.ProductsRepository.GetCatIDByID(productID)[0][0]
        catName = db.CatRepository.GetCatNameById(catID)[0][0]
        findAllSalerName = db.SalerRepository.GetAll()
        findAllSubCats = db.CatRepository.GetAllSubCats()
        
        instance.viewEditProductUI.productName_input.setText(f"{productName}")
        instance.viewEditProductUI.productPrice_input.setText(f"{productPrice}")
        instance.viewEditProductUI.productDate_input.setText(f"{productDate}")
        instance.viewEditProductUI.productRandomID_input.setText(f"{productRandomID}")
        instance.viewEditProductUI.productDetails_input.setPlainText(f"{productDetails}")
        instance.viewEditProductUI.salerName_lbl.setText(f"{salerName}")
        instance.viewEditProductUI.catName_lbl.setText(f"{catName}")
        for saler in findAllSalerName:
            salerName = saler[1]
            instance.viewEditProductUI.saler_comboBox.addItem(salerName)
        for subCats in findAllSubCats:
            catName = subCats[2]
            instance.viewEditProductUI.cat_comboBox.addItem(catName)
            
    def ConfrimEditProduct(self,productID,instance):
        getProductName = instance.productName_input.text()
        getProductDetails = instance.productDetails_input.toPlainText()
        getProductPrice = instance.productPrice_input.text()
        getProductDate = instance.productDate_input.text()
        getProductRandomID = instance.productRandomID_input.text()
        getProductSalerName = instance.saler_comboBox.currentText()
        getProductCatName = instance.cat_comboBox.currentText()
        
        findSalerID = db.SalerRepository.GetSalerIDByName(getProductSalerName)[0][0]
            
        findCatId = db.CatRepository.GetCatIDByName(getProductCatName)[0][0]
            
        newProduct = productTable(getProductName,getProductDetails,getProductPrice,getProductDate,getProductRandomID,findSalerID,findCatId)
        db.ProductsRepository.Update(newProduct,productID)
        db.ProductsRepository.Save()
        
        return True
    
    def ConfirmUserShopCart(self):
        pass
    
    def ConfrimDeleteUser(self,userID):
        findAllUserInfo = db.userRepository.GetByID(userID)
        userName = findAllUserInfo[0][1]
        email = findAllUserInfo[0][2]
        password = findAllUserInfo[0][3]
        date = findAllUserInfo[0][4]
        randomID = findAllUserInfo[0][5]
        newUser = userTable(userName,email,password,date,randomID)
        db.userRepository.Delete(newUser,userID)
        db.userRepository.Save()
        return True
    