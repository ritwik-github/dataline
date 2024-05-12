#--------Author Info-----------------------
print("------------------------------------------------------- \n ================= Hakuna Matata | It Means no Worries ================= \n-------------------------------------------------------")
print(" Dataline : the DBMS®️ - Project Pipeline Management System \n author : ©️ Ritwik Giri \n Connect : www.linkedin.com/in/ritwik-giri-gaffer \n Visit : www.ritwik-gaffer.art \n email : light@ritwik-gaffer.art ")
print("-------------------------------------------- \n progress.....")


# Dataline_CustomTKinter_GUI
# import Required Libreries


import customtkinter as ctk
import os
import sys
import subprocess
from PIL import Image, ImageTk
from customtkinter import filedialog , CTkImage

################################################################### UI Design Starts here ##############################################################


# main window size and title
root = ctk.CTk()
root.geometry("1255x750")
root.resizable(0,0)
root.title("DATALINE                                                                                                                                                                     Kisholoy(1.0.0)") #dded blank space to get the title in center
root.iconbitmap('sourceImages/clapStick.ico')  #If We keep any Image; Application Will always search for the Images in given Path
ctk.set_appearance_mode("dark")    # this is to define Theme (dark | light | Systemdefault)

"""
Root Path Entry

"""

# RootDirectory Label Frame
projectDir_frame = ctk.CTkFrame(root, width=200,height=28, corner_radius=3, fg_color="#343638")
projectDir_frame.grid(row=0, column=0, padx=15, pady=8)

# RootDirectory Label
projectDir_label = ctk.CTkLabel(root, text="Root Directory", text_color="#b3b3b3", bg_color="#343638", font=ctk.CTkFont(size=13, weight='normal'))
projectDir_label.grid(row=0, column=0, padx=15, pady=8)

# RootDirectory path Entry
projectDir_entry = ctk.CTkEntry(root, width=960, height=28, corner_radius=3, border_width=1, placeholder_text="X:\ECP_contents", placeholder_text_color="#707070", state='normal')
projectDir_entry.place(x=230, y=8)

"""
Add Path/Copy Folder Path Button 
"""

def addPath():
    return filedialog.askdirectory(title = "Copy Root Directory Path")
    
addPath_button = ctk.CTkButton(root, text="+", width=30, fg_color="#333333", bg_color="#333333", corner_radius=3,border_width=1,command=addPath ) 
addPath_button.place(x=1200, y=8)




# Left pannel librerry Frame
leftPannelLib_frame = ctk.CTkFrame(root, width=200, height=700, corner_radius=3, fg_color="#343638", border_width=1)
leftPannelLib_frame.grid(row=1, column=0,)


# Left pannel librerry entries
# projectCode label
projectCode_label = ctk.CTkLabel(leftPannelLib_frame, text="enterProjectName | Code", text_color="#b3b3b3", bg_color="#343638", font=ctk.CTkFont(size=12, weight='normal'))
projectCode_label.place(x=32, y=10)

# projectCode entry
projectCode_entry = ctk.CTkEntry(leftPannelLib_frame, width=130, height=28, corner_radius=2, border_width=1, fg_color="#333333", placeholder_text="eg: EYE", placeholder_text_color="#707070", state='normal', justify='center')
projectCode_entry.place(x=35, y=40)



# Discipline/pipelineStructure_lbl
dccContainer_label = ctk.CTkLabel(leftPannelLib_frame, text="Core\nPipeline Structure", text_color="#b3b3b3", bg_color="#343638", font=ctk.CTkFont(size=12, weight='normal'))
dccContainer_label.place(x=55, y=80)


structure_image = ctk.CTkImage(light_image=Image.open("sourceImages/DATALINE tree_A.png"),size=(140, 500))
structure_image_label = ctk.CTkLabel(leftPannelLib_frame,text_color="#333333", font=ctk.CTkFont(size=1, weight='normal'), image=structure_image)
structure_image_label.place(x=28.5, y=120)


"""
Button to Enlarge PIPELINE Structure Image
by clicking on the + icon/button It opens the Image File/Pdf File from File system
"""
def Expand():
    # Create a new window
    image_window = ctk.CTkToplevel(root)
    image_window.title("PIPELINE Structure")

    # Load and display the image
    img = Image.open("sourceImages/DATALINE tree_low.png")
    img = ImageTk.PhotoImage(img)
    label = ctk.CTkLabel(image_window, text_color="#333333", font=ctk.CTkFont(size=1, weight='normal'), image=img)
    label.pack()


    
expand_button = ctk.CTkButton(leftPannelLib_frame, text="+", width=30, fg_color="#333333", bg_color="#333333", corner_radius=1,command= Expand )
expand_button.place(x=130, y=580)



#Tool Credits

toolCredits_frame = ctk.CTkFrame(leftPannelLib_frame, width=180, height=60, fg_color="#323232", border_width=1, border_color="black", corner_radius=3)
toolCredits_frame.place(x=10, y=630)
creditText_lable = ctk.CTkLabel(toolCredits_frame, text="(c)- RITWIK GIRI \n 2024 All Rights Reserved \n Please DON'T re-distribute", text_color="#808080", bg_color="#323232", font=ctk.CTkFont(size=12, weight='normal'), justify='center')
creditText_lable.place(x=18, y=10)


"""
Core Operational Entry

"""


# operation pannel Frame (rightSide)
operationPannel_frame = ctk.CTkFrame(root, width=1000, height=700, fg_color="#343638", corner_radius=3, border_width=1)
operationPannel_frame.grid(row=1, column=1)


# input_operations (bulk)
seqName_label = ctk.CTkLabel(operationPannel_frame, text="enterSeqName", text_color="#b3b3b3", bg_color="#343638", font=ctk.CTkFont(size=12, weight='normal'))
seqName_label.place(x=60, y=10)

seqName_entry = ctk.CTkEntry(operationPannel_frame, width=130, height=28, corner_radius=2, border_width=1, fg_color="#333333", placeholder_text="eg: 010_EB", placeholder_text_color="#707070", state='normal', justify='center')
seqName_entry.place(x=35, y=40)


shotNamePrefix_label = ctk.CTkLabel(operationPannel_frame, text="shotNamePrefix", text_color="#b3b3b3", bg_color="#343638", font=ctk.CTkFont(size=12, weight='normal'))
shotNamePrefix_label.place(x=300, y=10)

shotName_entry = ctk.CTkEntry(operationPannel_frame, width=130, height=28, corner_radius=2, border_width=1, fg_color="#333333", placeholder_text="eg: EB OR empty" ,placeholder_text_color="#707070", state='normal', justify='center')
shotName_entry.place(x=280, y=40)


# combobox var
shotNumVar = ctk.IntVar(value="03") #03 is default, Others are selectable from the dropdown list

shotCombobox_label = ctk.CTkLabel(operationPannel_frame, text="numberOfShots", text_color="#b3b3b3", bg_color="#343638", font=ctk.CTkFont(size=12, weight='normal'))
shotCombobox_label.place(x=440, y=10)

shotCombobox_entry = ctk.CTkComboBox(operationPannel_frame, width=130, height=28, corner_radius=2, border_width=1, button_color="#444444", dropdown_text_color="#757575", font=ctk.CTkFont(size=12), variable=shotNumVar, values=["01","02", "03", "04","05", "06", "07","08","09","10",], justify='center')
shotCombobox_entry.place(x=420,y=40)



"""
Exclussive Entry

"""
# exclussive_box
exclussiveBox_frame = ctk.CTkFrame(operationPannel_frame, width=980, height=150, fg_color="#323232", border_width=1, border_color="black", corner_radius=3)
exclussiveBox_frame.place(x=10, y=140)

# PathEntry Exclussive
exclussivePath_label = ctk.CTkLabel(exclussiveBox_frame, text="* this is wild card entry. Doesn't depend upon root entries || just enter show level directory path", text_color="grey", bg_color="#323232", font=ctk.CTkFont(size=12, weight='normal'))
exclussivePath_label.place(x=22, y=0.5)

exclussivePath_entry = ctk.CTkEntry(exclussiveBox_frame, width=920, height=28, corner_radius=3, border_width=1,fg_color="#222222", placeholder_text="X:\ECP_contents\show", placeholder_text_color="#707070", state='normal')
exclussivePath_entry.place(x=18, y=28)
"""
Add Path/Copy Folder Path Button 
"""

def addExclussivePath():
    return filedialog.askdirectory(title = "Copy Folder Path Show Level")
    
addExclussivePath_button = ctk.CTkButton(exclussiveBox_frame, text="+", width=30, fg_color="#333333", bg_color="#333333", corner_radius=3,border_width=1,command=addExclussivePath ) 
addExclussivePath_button.place(x=942, y=28)
"""
#################################
"""

# exclussive_input_operaions
seqNameExclussive_label = ctk.CTkLabel(exclussiveBox_frame, text="enterExclussiveSeqName", text_color="#b3b3b3", bg_color="#323232", font=ctk.CTkFont(size=12, weight='normal'))
seqNameExclussive_label.place(x=22, y=65)

seqNameExclussive_entry = ctk.CTkEntry(exclussiveBox_frame, width=130, height=28, corner_radius=2, border_width=1, fg_color="#333333", placeholder_text="eg: 005_TS", placeholder_text_color="#707070", state='normal', justify='center')
seqNameExclussive_entry.place(x=25, y=100)


shotNamePrefixExclussive_label = ctk.CTkLabel(exclussiveBox_frame, text="shotNamePrefix", text_color="#b3b3b3", bg_color="#323232", font=ctk.CTkFont(size=12, weight='normal'))
shotNamePrefixExclussive_label.place(x=290, y=65)

shotNameExclussive_entry = ctk.CTkEntry(exclussiveBox_frame, width=130, height=28, corner_radius=2, border_width=1, fg_color="#333333", placeholder_text="eg: TS", placeholder_text_color="#707070", state='normal', justify='center')
shotNameExclussive_entry.place(x=270, y=100)


# comboboxExclussive var
shotNumExclussiveVar = ctk.IntVar(value="01") #01 is default, Others are selectable from the dropdown list

shotExclussiveCombobox_label = ctk.CTkLabel(exclussiveBox_frame, text="numberOfShots", text_color="#b3b3b3", bg_color="#323232", font=ctk.CTkFont(size=12, weight='normal'))
shotExclussiveCombobox_label.place(x=450, y=65)

shotExclussiveCombobox_entry = ctk.CTkComboBox(exclussiveBox_frame, width=130, height=28, corner_radius=2, border_width=1, button_color="#444444", dropdown_text_color="#757575", font=ctk.CTkFont(size=12), variable=shotNumExclussiveVar, values=["01","02", "03", "04","05", "06", "07","08","09","10",], justify='center')
shotExclussiveCombobox_entry.place(x=430, y=100)


"""
guideBox Log

"""

# guide_box
guidebox_frame = ctk.CTkFrame(operationPannel_frame, width=900, height=370, fg_color="#323232", border_width=1, border_color="orange", corner_radius=3)
guidebox_frame.place(x=50, y=320)

# guideText
guideText_lable = ctk.CTkLabel(guidebox_frame, text="Tip:\n1-The first rule is to enter the project root directory and project code (for the bulk generation only_no need for Exclussive entry).\n2-Enter a seq name (as hinted in UI) & number of shots.Hit generate, it will generate shots in bulk number.\n3-To generate on by one seq >> shots, enter previously created show path in the exclussive section, No need to enter root directry and project code and bulk shot sec.\n4-enter seq name and shot name as hinted in UI (in exclussive sec) to generate one by one shot generaion exclussively with the second Generate button", text_color="#808080", bg_color="#323232", font=ctk.CTkFont(size=12, weight='normal'), justify='left')
guideText_lable.place(x=10, y=10)


# terminalLogUI
terminalLog_frame = ctk.CTkScrollableFrame(guidebox_frame, orientation = "vertical", width=800, height=0, label_text="Validation <> Log", label_text_color="orange", )
terminalLog_frame.place(x=40, y=100)
terminalLog_frame._parent_canvas.yview_moveto(-1)


################################################# Core UI design ends here check Button Functions at the end of Core Operations ###############################################################

"""
GenBulk Button Function/Core Operation

"""
# button function Bulk Folders Creation
def genBulk():
    dirPath = projectDir_entry.get()
    showCode = projectCode_entry.get()
    rootPath = f"{dirPath}\{showCode}"
    seqName = seqName_entry.get()
    seqPath = f"{rootPath}\{seqName}"
    shotName = shotName_entry.get()
    shotNumber = shotCombobox_entry.get()
    shotPath = f"{seqPath}\{shotName}"
    
    


    print(f"Directory '{rootPath}' --proceeding...")
    # *******UI_LOG****** #
    log_lableA = ctk.CTkLabel(terminalLog_frame, text=(rootPath,'--proceeding...PLEASE_CHECK_TERMINAL_FOR_DETAILED_LOG'), text_color='#FFE87C', font=ctk.CTkFont(size=11, weight='normal'), justify='left' )
    log_lableA.pack()

    ##### Validation And Function

    if dirPath:
        # if dirPath is valid then go ahed and proceed to Create the directory
        create_directory(rootPath)
    else:
        print("ERROR:No directory selected. Enter Valid File System Path")
        # *******UI_LOG****** #
        log_lableB = ctk.CTkLabel(terminalLog_frame, text=('No directory Selected. Enter valid FileSystem Path'), text_color='red', font=ctk.CTkFont(size=12, weight='normal'), justify='left' )
        log_lableB.pack()
    if showCode:
        # if showCode is valid then go ahed and proceed to Create the directory
        print("(-_-)", "|| ☢️  ♾️  ☣️ ")
    else:
        print("ERROR:Plase enter Show Name.")
        # *******UI_LOG****** #
        log_lableC = ctk.CTkLabel(terminalLog_frame, text=('Please Enter Show Name'), text_color='dark Orange', font=ctk.CTkFont(size=11, weight='normal'), justify='left' )
        log_lableC.pack()
    if seqName:
        print()
    else:
        print("ERROR:Please Enter a Seq Name to Create Seq_shots.")
        
    #clear_Entries ############
    """    
    projectCode_entry.delete(0, ctk.END)
    projectDir_entry.delete(0, ctk.END)
    """

"""
Proceed with creating core directories
"""
def create_directory(rootPath):
    dirPath = projectDir_entry.get()
    showCode = projectCode_entry.get()
    rootPath = f"{dirPath}\{showCode}"
    seqName = seqName_entry.get()
    seqPath = f"{rootPath}\{seqName}"
    shotName = shotName_entry.get()
    shotNumber = shotCombobox_entry.get()
    shotPath = f"{seqPath}\{shotName}"
    
    try:
        # try if all entries above fns are valid then go ahed and MAKE the directory
        os.makedirs(name=rootPath)
        
        print(f"Directory- {rootPath} --created successfully.")
        log_lableD = ctk.CTkLabel(terminalLog_frame, text=(f"Directory- {rootPath} --created successfully."), text_color='green', font=ctk.CTkFont(size=11, weight='normal'), justify='left' )
        log_lableD.pack()

        # changing Dir/entering into Project leaf to create leaf dirs
        os.chdir(rootPath)
        print(f"CHANGING DIRECTORY PATH TO CREATE CHILD FOLDERS.....\n{os.getcwd()}\ \n--creating Folders under project dir...")



        # AMS core operation Starts here **********************************************************************************************************************************************************************
        



        # creating leafDirs per stream/decepline

        # parent Directories

        os.makedirs(name='buildAssets', mode=0o777 , exist_ok=False)
        os.makedirs(name='bakeAssets', mode=0o777 , exist_ok=False)
        os.makedirs(name='refRnd', mode=0o777 , exist_ok=False)
        os.makedirs(name='editPreviz', mode=0o777 , exist_ok=False)
        os.makedirs(name='diReMaster', mode=0o777 , exist_ok=False)
        os.makedirs(name='renderElements', mode=0o777 , exist_ok=False)
        os.makedirs(name='tools', mode=0o777 , exist_ok=False)
        os.makedirs(name='projectTracking', mode=0o777 , exist_ok=False)

        print(f"{os.getcwd()} \ parent Dirs - Created SUCCESSFULLY.....")

        # child Directories

                                                                                                # ****** assets *******

        os.chdir("buildAssets")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        # create build deceiplines
        list = ['3dModel','environment','anim','rigging','techAnim','groom','pantry','lookdev','lighting','fx','comp','utils']
        for buidDeceplineList in list:
            os.makedirs(buidDeceplineList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()} \ build deceplines ('3dModel','environment','anim','rigging','techAnim','groom','pantry','lookdev','lighting','fx','comp','utils') - Created SUCCESSFULLY.....")

        ##################### Assets 3D Model, Sclupting #########################################
        os.chdir("3dModel")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        # create build DCC directories
        list = ['blender','Maya','zBrush','houdini','megascans']
        for buildDccList in list:
            os.makedirs(buildDccList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()} \ build DCCs ('blender','Maya','zBrush','houdini','megascans') - Created SUCCESSFULLY.....")

        os.chdir('../')

        ###################### rigging #####################################
        
        #print(f"directory Changed to One Step UP--- {os.getcwd()}") # to check if the directory actually got changed *UP 1 Step*
        os.chdir("rigging")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed
        os.makedirs(name='maya', mode=0o777 , exist_ok=False)

        print(f"{os.getcwd()}\maya - Created SUCCESSFULLY.....")

        os.chdir('../')

        ############################### texturing ######################################
        
        #print(f"directory Changed to One Step UP--- {os.getcwd()}") # to check if the directory actually got changed *UP 1 Step*
        os.chdir("pantry")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        # create pantry deceplines
        list = ['hdri', 'mari','photoshop','substance','tex','tx']
        for pantryDeceplineList in list:
            os.makedirs(pantryDeceplineList, mode=0o777 , exist_ok=False)

        print(f"{os.getcwd()} ('hdri', 'mari','photoshop','substance','tex','tx') - Created SUCCESSFULLY.....")

        os.chdir('../')

        ################################ grooming #######################################
        
        #print(f"directory Changed to One Step UP--- {os.getcwd()}") # to check if the directory actually got changed *UP 1 Step*
        os.chdir("groom")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        # create groom deceplines
        list = ['cloth', 'hair','fur','folliage','muscle']
        for groomList in list:
            os.makedirs(groomList, mode=0o777 , exist_ok=False)

        print(f"{os.getcwd()} ('cloth', 'hair','fur','folliage','muscle') - Created SUCCESSFULLY.....")

        os.chdir('../')
        
        ################################### anim ######################################
        
        #print(f"directory Changed to One Step UP--- {os.getcwd()}") # to check if the directory actually got changed *UP 1 Step*
        os.chdir("anim")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed
        os.makedirs(name='maya', mode=0o777 , exist_ok=False)

        print(f"{os.getcwd()}\maya - Created SUCCESSFULLY.....")

        os.chdir('../')

        ######################## TechAnim, CFX-Dynamics-Simulation ##############################
        
        
        #print(f"directory Changed to One Step UP--- {os.getcwd()}") # to check if the directory actually got changed *UP 1 Step*
        os.chdir("techAnim")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        # create cfx deceplines
        list = ['clothSim', 'hairSim','furSim','envDynamics','muscleSim']
        for cfxList in list:
            os.makedirs(cfxList, mode=0o777 , exist_ok=False)

        print(f"{os.getcwd()} ('clothSim', 'hairSim','furSim','envDynamics','muscleSim') - Created SUCCESSFULLY.....")

        # clothSim
        os.chdir("clothSim")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        list = ['maya','houdini']
        for clothSimList in list:
            os.makedirs(clothSimList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('maya','houdini') - Created SUCCESSFULLY.....")
        
        # hairSim
        os.chdir('../')
        
        os.chdir("hairSim")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        list = ['maya','houdini','yeti']
        for hairSimList in list:
            os.makedirs(hairSimList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('maya','houdini','yeti') - Created SUCCESSFULLY.....")
        # furSim
        os.chdir('../')
        
        os.chdir("furSim")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        list = ['maya','houdini','yeti']
        for furSimList in list:
            os.makedirs(furSimList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('maya','houdini','yeti') - Created SUCCESSFULLY.....")
        # muscleSim
        os.chdir('../')
        
        os.chdir("muscleSim")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        list = ['maya','houdini','ziva']
        for muscleSimList in list:
            os.makedirs(muscleSimList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('maya','houdini','ziva') - Created SUCCESSFULLY.....")
        #envDynamics
        os.chdir('../')
        
        os.chdir("envDynamics")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        list = ['maya','houdini',]
        for envDynList in list:
            os.makedirs(envDynList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('maya','houdini') - Created SUCCESSFULLY.....")

        os.chdir('../../')

        ############################## fxSimulation ##################################
        
        os.chdir("fx")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        list = ['maya','houdini',]
        for fxSimList in list:
            os.makedirs(fxSimList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('maya','houdini') - Created SUCCESSFULLY.....")

        os.chdir('../')
        
        

        ################################## lookdev ########################################
        
        os.chdir("lookdev")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        list = ['maya', 'katana','houdini']
        for ldvDccList in list:
            os.makedirs(ldvDccList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('maya','katana','houdini') - Created SUCCESSFULLY.....")

        os.chdir('../')
        

        ################################## lighting #######################################
        
        os.chdir("lighting")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        list = ['maya', 'katana','houdini']
        for lgtDccList in list:
            os.makedirs(lgtDccList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('maya','katana','houdini') - Created SUCCESSFULLY.....")

        os.chdir("maya")
        os.makedirs(name='mayaSceneFile', mode=0o777, exist_ok=False)

        os.chdir('../')
        os.chdir("houdini")
        os.makedirs(name='hipFile', mode=0o777, exist_ok=False)

        os.chdir('../')
        os.chdir("katana")
        os.makedirs(name='katanaProject', mode=0o777, exist_ok=False)

        os.chdir('../../') 


        ################################## comp ########################################
        os.chdir("comp")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        os.makedirs(name='preComp', mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('preComp') - Created SUCCESSFULLY.....")

        os.chdir('../')

        ######################### utils #############################################
        
        os.chdir("utils")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        list = ['renderStats', 'misc']
        for utilsList in list:
            os.makedirs(utilsList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('renderStats','misc') - Created SUCCESSFULLY.....")

        os.chdir('../../')

                                                                                            # ******** rnd *********
        # refRndData
        os.chdir("refRnd")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        list = ['confluence', 'pureRef']
        for refRndList in list:
            os.makedirs(refRndList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('confluence', 'pureRef') - Created SUCCESSFULLY.....")

        os.chdir('../')

                                                                                            # ********** releaseBakePublish **********
        # releaseBakePublish
        os.chdir("bakeAssets")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed
        list = ['animCache','camCache','dynamicsCache','fxCache','geoCache','groomCache','katanaPublishes','shaderExport','USD']
        for publishList in list:
            os.makedirs(publishList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('animCache','camCache','dynamicsCache','fxCache','geoCache','groomCache','katanaPublishes','shaderExport','USD') - Created SUCCESSFULLY.....")

        os.chdir("dynamicsCache")
        list = ['clothCache', 'hairCache','furCache','envDynamicsCache','muscleCache']
        for dynamicsCacheList in list:
            os.makedirs(dynamicsCacheList, mode=0o777, exist_ok=False)

        os.chdir('../')

        os.chdir("katanaPublishes")
        list = ['katanaLookfile','katanaLivegrp']
        for katanaPublishesList in list:
            os.makedirs(katanaPublishesList, mode=0o777, exist_ok=False)

        os.chdir('../../')

                                                                                            # ********** editPreviz **********
        # editorial
        os.chdir("editPreviz")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        list = ['nukeStudio', 'premierePro','resolve','rvTimeline']
        for editPrevizList in list:
            os.makedirs(editPrevizList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('nukeStudio', 'premierePro','resolve','rvTimeline') - Created SUCCESSFULLY.....")

        os.chdir('../')

                                                                                            # ********** renders_Elements **********
        # diRemastering
        os.chdir("renderElements")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        list = ['playblasts', 'hwRender','ldv','fxFlips','lsc','comp','rvAnnotations','edit','di','delivery']
        for renderElementsList in list:
            os.makedirs(renderElementsList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('playblasts', 'hwRender','ldv','fxFlips','lsc','comp','rvAnnotations','edit','di','delivery') - Created SUCCESSFULLY.....")

        os.chdir('../')

                                                                                            # ********** DI-Color_ReMaster **********
        # renderElements
        os.chdir("diReMaster")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed

        os.makedirs(name='resolve', mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('resolve') - Created SUCCESSFULLY.....")

        os.chdir('../')

                                                                                            # ********** tools **********
        # toolsScripts
        os.chdir("tools")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed
        list = ['arnold','prman', 'maya','katana','houdini','mari','nuke','ziva','substance','rv','projectEnvVar','scripts']
        for toolsList in list:
            os.makedirs(toolsList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('arnold','prman', 'maya','katana','houdini','mari','nuke','ziva','substance','rv','projectEnvVar','scripts') - Created SUCCESSFULLY.....")

        os.chdir('../')

                                                                                            # ********** projectTracking **********
        # tracking
        
        os.chdir("projectTracking")
        print(f"directory Changed to--- {os.getcwd()}") # to check if the directory actually got changed
        list = ['shotgun','excel','confluence','googlesheet']
        for projectTrackingList in list:
            os.makedirs(projectTrackingList, mode=0o777, exist_ok=False)

        print(f"{os.getcwd()}\ ('shotgun','excel','confluence','googlesheet') - Created SUCCESSFULLY.....")

        os.chdir('../')
        

        
        # AMS core operation Ends here ********************************************************************************************************************************************************************
        
        print(f"{os.getcwd()} Proceeding with Sequence_Shot Directories")

        # **********************************Seq_Shot Directory Starts here *******************************************

        


        os.chdir(rootPath)
        os.makedirs(name=seqPath, mode=0o777, exist_ok=False)

        os.chdir(seqPath)

        print(f"{os.getcwd()} - Created SUCCESSFULLY.....  ")

        print(f"{os.getcwd()}\ creating Shot folders", file=sys.stdout, flush=False)

        if shotNumber: ####### if shot Number Entry is valid or at-Least 01 then proceed Else Print 

            ######################## this is shot Core folder Structure ###############

            def shotCore(): #call shotCore() to create the shot level child directories under each Shot
    
                coreList = ['bakeShot', 'editPreviz','diReMaster','renderElements','anim','techAnim','groom','envDmp','fx','lighting','compositing','rpm']
                for parentDept in coreList:
                    os.makedirs(parentDept, mode=0o777 , exist_ok=False)

                os.chdir("bakeShot")
                
                list = ['animCache','camCache','dynamicsCache','fxCache','geoCache','groomCache','katanaPublishes','shaderExport','USD']
                for publishList in list:
                    os.makedirs(publishList, mode=0o777, exist_ok=False)

                os.chdir("dynamicsCache")
                list = ['clothCache', 'hairCache','furCache','envDynamicsCache','muscleCache']
                for dynamicsCacheList in list:
                    os.makedirs(dynamicsCacheList, mode=0o777, exist_ok=False)

                os.chdir('../')

                os.chdir("katanaPublishes")
                list = ['katanaLookfile','katanaLivegrp']
                for katanaPublishesList in list:
                    os.makedirs(katanaPublishesList, mode=0o777, exist_ok=False)

                os.chdir('../../')
                os.chdir('renderElements')
                list = ['animQC','lightQC','groomQC','fxQC','taQC','envQC','dmp','rpm','fx','comp','lighting','lsc','lookdev','edit','di']
                for shotRenderElementList in list:
                    os.makedirs(shotRenderElementList, mode=0o777, exist_ok=False)

                os.chdir('../')
                os.chdir('groom')    
                    
                groomList = ['cloth', 'hair','fur','folliage','muscle']
                for groomDept in groomList:
                    os.makedirs(groomDept, mode=0o777 , exist_ok=False)
                os.chdir('../')

                os.chdir('lighting')
                lightingDccList = ['maya','katana','houdini']
                for lightingDcc in lightingDccList:
                    os.makedirs(lightingDcc, mode=0o777, exist_ok=False)
                os.chdir('../')

                os.chdir('compositing')
                compList = ['lsc','comp']
                for compDeptList in compList:
                    os.makedirs(compDeptList, mode=0o777 , exist_ok=False)
                os.chdir('../')

                os.chdir('rpm')
                rpmDeptList = ['track','roto','prep','matchMove']
                for rpmDept in rpmDeptList:
                    os.makedirs(rpmDept, mode=0o777, exist_ok=False)
                os.chdir('../')

            ##########################################################################

            ###### if chosen shot number/range/list is 01 then make directory as listed below
            if shotNumber == "01":
                list = ['01','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotName}_{bulkShotList}")

                
                os.chdir(f"{shotName}_01")
                print(f"{os.getcwd()}")

                shotCore()  # for shot number 01

                os.chdir('../')

                os.chdir(f"{shotName}_seq") # for seq
                shotCore()

                    

            ###### if chosen shot number/range/list is 02 then make directory as listed below

            elif shotNumber == "02":
                list = ['01','02','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotName}_{bulkShotList}")

                
                os.chdir(f"{shotName}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotName}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotName}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")
                    
                    

            ###### if chosen shot number/range/list is 03 then make directory as listed below

            elif shotNumber == "03":
                list = ['01','02','03','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotName}_{bulkShotList}")

                
                os.chdir(f"{shotName}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotName}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotName}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotName}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            ###### if chosen shot number/range/list is 04 then make directory as listed below

            elif shotNumber == "04":
                list = ['01','02','03','04','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotName}_{bulkShotList}")

                os.chdir(f"{shotName}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotName}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotName}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotName}_04")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 04
                os.chdir('../')

                os.chdir(f"{shotName}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            ###### if chosen shot number/range/list is 05 then make directory as listed below

            elif shotNumber == "05":
                list = ['01','02','03','04','05','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotName}_{bulkShotList}")

                os.chdir(f"{shotName}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotName}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotName}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotName}_04")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 04
                os.chdir('../')

                os.chdir(f"{shotName}_05")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 05
                os.chdir('../')

                os.chdir(f"{shotName}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            ###### if chosen shot number/range/list is 06 then make directory as listed below

            elif shotNumber == "06":
                list = ['01','02','03','04','05','06','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotName}_{bulkShotList}")

                os.chdir(f"{shotName}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotName}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotName}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotName}_04")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 04
                os.chdir('../')

                os.chdir(f"{shotName}_05")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 05
                os.chdir('../')

                os.chdir(f"{shotName}_06")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 06
                os.chdir('../')

                os.chdir(f"{shotName}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            ###### if chosen shot number/range/list is 07 then make directory as listed below

            elif shotNumber == "07":
                list = ['01','02','03','04','05','06','07','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotName}_{bulkShotList}")

                os.chdir(f"{shotName}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotName}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotName}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotName}_04")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 04
                os.chdir('../')

                os.chdir(f"{shotName}_05")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 05
                os.chdir('../')

                os.chdir(f"{shotName}_06")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 06
                os.chdir('../')

                os.chdir(f"{shotName}_07")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 07
                os.chdir('../')

                os.chdir(f"{shotName}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            ###### if chosen shot number/range/list is 08 then make directory as listed below

            elif shotNumber == "08":
                list = ['01','02','03','04','05','06','07','08','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotName}_{bulkShotList}")

                os.chdir(f"{shotName}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotName}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotName}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotName}_04")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 04
                os.chdir('../')

                os.chdir(f"{shotName}_05")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 05
                os.chdir('../')

                os.chdir(f"{shotName}_06")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 06
                os.chdir('../')

                os.chdir(f"{shotName}_07")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 07
                os.chdir('../')

                os.chdir(f"{shotName}_08")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 08
                os.chdir('../')

                os.chdir(f"{shotName}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            ###### if chosen shot number/range/list is 09 then make directory as listed below

            elif shotNumber == "09":
                list = ['01','02','03','04','05','06','07','08','09','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotName}_{bulkShotList}")

                os.chdir(f"{shotName}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotName}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotName}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotName}_04")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 04
                os.chdir('../')

                os.chdir(f"{shotName}_05")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 05
                os.chdir('../')

                os.chdir(f"{shotName}_06")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 06
                os.chdir('../')

                os.chdir(f"{shotName}_07")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 07
                os.chdir('../')

                os.chdir(f"{shotName}_08")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 08
                os.chdir('../')

                os.chdir(f"{shotName}_09")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 09
                os.chdir('../')

                os.chdir(f"{shotName}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            ###### if chosen shot number/range/list is 10 then make directory as listed below

            elif shotNumber == "10":
                list = ['01','02','03','04','05','06','07','08','09','10','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotName}_{bulkShotList}")

                os.chdir(f"{shotName}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotName}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotName}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotName}_04")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 04
                os.chdir('../')

                os.chdir(f"{shotName}_05")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 05
                os.chdir('../')

                os.chdir(f"{shotName}_06")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 06
                os.chdir('../')

                os.chdir(f"{shotName}_07")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 07
                os.chdir('../')

                os.chdir(f"{shotName}_08")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 08
                os.chdir('../')

                os.chdir(f"{shotName}_09")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 09
                os.chdir('../')

                os.chdir(f"{shotName}_10")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 10
                os.chdir('../')

                os.chdir(f"{shotName}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

        else:
            print('are You Mad, chose a valid shot number/list, next time you will run the tool')
    
    
    
        # **********************************Seq_Shot Directory Starts here *******************************************
    
    
    except OSError as e:
        print(f"--Error creating directory- {rootPath}: {e}")
        # *******UI_LOG****** #
        log_lableE = ctk.CTkLabel(terminalLog_frame, text=(f"--Error creating directory {rootPath}: {e}"), text_color='red', font=ctk.CTkFont(size=11, weight='normal'), justify='left' )
        log_lableE.pack()








"""
#################
GenBulk Button
#################
"""

# Generatte button bulk ###########################################################################################################
generate_button = ctk.CTkButton(operationPannel_frame, text="Generate", width=100, fg_color="grey", command=genBulk )
generate_button.place(x=850, y=40)

###############################################################################################################


"""
Exclussive Operation Button Function

"""
# button function Exclussive folder Creation
def genExclussive():
    dirPathExclussive = exclussivePath_entry.get()
    seqNameExclussive = seqNameExclussive_entry.get()
    shotNameExclussive = shotNameExclussive_entry.get()
    seqNameExclussivePath = f"{dirPathExclussive}\{seqNameExclussive}"
    shotNameExclussivePath = f"{seqNameExclussivePath}\{shotNameExclussive}"
    shotNumberExclussive = shotExclussiveCombobox_entry.get()
    


    print(f"Directory '{seqNameExclussivePath}' --proceeding...")
    # *******UI_LOG****** #
    log_lableA = ctk.CTkLabel(terminalLog_frame, text=(seqNameExclussivePath,'--proceeding...PLEASE_CHECK_TERMINAL_FOR_DETAILED_LOG'), text_color='#FFE87C', font=ctk.CTkFont(size=11, weight='normal'), justify='left' )
    log_lableA.pack()

    ##### Validation And Function

    if dirPathExclussive:
        # if showDirPath is valid then go ahed and proceed to Create the directory
        createExcl_directory(seqNameExclussivePath)
    else:
        print("ERROR:No directory selected. Enter Valid/Existing Show Directory Path")
        # *******UI_LOG****** #
        log_lableB = ctk.CTkLabel(terminalLog_frame, text=('No directory Selected. Enter Valid/Existing Show Directory Path'), text_color='red', font=ctk.CTkFont(size=12, weight='normal'), justify='left' )
        log_lableB.pack()
    if seqNameExclussive:
        # if SeqName is valid then go ahed and proceed to Create the directory
        print("(-_-)", "|| ☢️  ♾️  ☣️ ")
    else:
        print("ERROR:Plase enter Seq Name.")
        # *******UI_LOG****** #
        log_lableC = ctk.CTkLabel(terminalLog_frame, text=('Please Enter Sequence_shot Name'), text_color='dark Orange', font=ctk.CTkFont(size=11, weight='normal'), justify='left' )
        log_lableC.pack()
    if shotNameExclussive:
        print()
    else:
        print("ERROR:Please Enter a Seq Name to Create Seq_shots.")


"""
Proceed to creating Exclussive seq/shot folders

"""
def createExcl_directory(seqNameExclussivePath):
    dirPathExclussive = exclussivePath_entry.get()
    seqNameExclussive = seqNameExclussive_entry.get()
    shotNameExclussive = shotNameExclussive_entry.get()
    seqNameExclussivePath = f"{dirPathExclussive}\{seqNameExclussive}"
    shotNameExclussivePath = f"{seqNameExclussivePath}\{shotNameExclussive}"
    shotNumberExclussive = shotExclussiveCombobox_entry.get()

    try:
        # try if all entries above fns are valid then go ahed and MAKE the directory
        os.makedirs(name=seqNameExclussivePath)
        print(f"Directory- {seqNameExclussivePath} --created successfully.")
        log_lableD = ctk.CTkLabel(terminalLog_frame, text=(f"Directory- {seqNameExclussivePath} --created successfully."), text_color='green', font=ctk.CTkFont(size=11, weight='normal'), justify='left' )
        log_lableD.pack()

        os.chdir(seqNameExclussivePath)
        

        if shotNumberExclussive: ####### if shot Name Entry is valid and number of shot is at-least 01 then proceed Else Print Caution report

        
            ######################## this is shot Core folder Structure ###############

            def shotCore(): #call shotCore() to create the shot level child directories under each Shot
    
                coreList = ['bakeShot', 'editPreviz','diReMaster','renderElements','anim','techAnim','groom','envDmp','fx','lighting','compositing','rpm']
                for parentDept in coreList:
                    os.makedirs(parentDept, mode=0o777 , exist_ok=False)

                os.chdir("bakeShot")
                
                list = ['animCache','camCache','dynamicsCache','fxCache','geoCache','groomCache','katanaPublishes','shaderExport','USD']
                for publishList in list:
                    os.makedirs(publishList, mode=0o777, exist_ok=False)

                os.chdir("dynamicsCache")
                list = ['clothCache', 'hairCache','furCache','envDynamicsCache','muscleCache']
                for dynamicsCacheList in list:
                    os.makedirs(dynamicsCacheList, mode=0o777, exist_ok=False)

                os.chdir('../')

                os.chdir("katanaPublishes")
                list = ['katanaLookfile','katanaLivegrp']
                for katanaPublishesList in list:
                    os.makedirs(katanaPublishesList, mode=0o777, exist_ok=False)

                os.chdir('../../')
                os.chdir('renderElements')
                list = ['animQC','lightQC','groomQC','fxQC','taQC','envQC','dmp','rpm','fx','comp','lighting','lsc','lookdev','edit','di']
                for shotRenderElementList in list:
                    os.makedirs(shotRenderElementList, mode=0o777, exist_ok=False)

                os.chdir('../')
                os.chdir('groom')    
                    
                groomList = ['cloth', 'hair','fur','folliage','muscle']
                for groomDept in groomList:
                    os.makedirs(groomDept, mode=0o777 , exist_ok=False)
                os.chdir('../')

                os.chdir('lighting')
                lightingDccList = ['maya','katana','houdini']
                for lightingDcc in lightingDccList:
                    os.makedirs(lightingDcc, mode=0o777, exist_ok=False)
                os.chdir('../')

                os.chdir('compositing')
                compList = ['lsc','comp']
                for compDeptList in compList:
                    os.makedirs(compDeptList, mode=0o777 , exist_ok=False)
                os.chdir('../')

                os.chdir('rpm')
                rpmDeptList = ['track','roto','prep','matchMove']
                for rpmDept in rpmDeptList:
                    os.makedirs(rpmDept, mode=0o777, exist_ok=False)
                os.chdir('../')

            ##########################################################################

            ###### if chosen shot number/range/list is 01 then make directory as listed below
            if shotNumberExclussive == "01":
                list = ['01','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotNameExclussive}_{bulkShotList}")

                
                os.chdir(f"{shotNameExclussive}_01")
                print(f"{os.getcwd()}")

                shotCore()  # for shot number 01

                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_seq") # for seq
                shotCore()

                    

            ###### if chosen shot number/range/list is 02 then make directory as listed below

            elif shotNumberExclussive == "02":
                list = ['01','02','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotNameExclussive}_{bulkShotList}")

                
                os.chdir(f"{shotNameExclussive}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")
                    
                    

            ###### if chosen shot number/range/list is 03 then make directory as listed below

            elif shotNumberExclussive == "03":
                list = ['01','02','03','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotNameExclussive}_{bulkShotList}")

                
                os.chdir(f"{shotNameExclussive}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            ###### if chosen shot number/range/list is 04 then make directory as listed below

            elif shotNumberExclussive == "04":
                list = ['01','02','03','04','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotNameExclussive}_{bulkShotList}")

                os.chdir(f"{shotNameExclussive}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_04")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 04
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            ###### if chosen shot number/range/list is 05 then make directory as listed below

            elif shotNumberExclussive == "05":
                list = ['01','02','03','04','05','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotNameExclussive}_{bulkShotList}")

                os.chdir(f"{shotNameExclussive}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_04")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 04
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_05")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 05
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            ###### if chosen shot number/range/list is 06 then make directory as listed below

            elif shotNumberExclussive == "06":
                list = ['01','02','03','04','05','06','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotNameExclussive}_{bulkShotList}")

                os.chdir(f"{shotNameExclussive}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_04")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 04
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_05")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 05
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_06")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 06
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            ###### if chosen shot number/range/list is 07 then make directory as listed below

            elif shotNumberExclussive == "07":
                list = ['01','02','03','04','05','06','07','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotNameExclussive}_{bulkShotList}")

                os.chdir(f"{shotNameExclussive}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_04")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 04
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_05")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 05
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_06")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 06
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_07")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 07
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            ###### if chosen shot number/range/list is 08 then make directory as listed below

            elif shotNumberExclussive == "08":
                list = ['01','02','03','04','05','06','07','08','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotNameExclussive}_{bulkShotList}")

                os.chdir(f"{shotNameExclussive}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_04")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 04
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_05")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 05
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_06")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 06
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_07")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 07
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_08")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 08
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            ###### if chosen shot number/range/list is 09 then make directory as listed below

            elif shotNumberExclussive == "09":
                list = ['01','02','03','04','05','06','07','08','09','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotNameExclussive}_{bulkShotList}")

                os.chdir(f"{shotNameExclussive}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_04")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 04
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_05")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 05
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_06")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 06
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_07")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 07
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_08")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 08
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_09")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 09
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            ###### if chosen shot number/range/list is 10 then make directory as listed below

            elif shotNumberExclussive == "10":
                list = ['01','02','03','04','05','06','07','08','09','10','seq']
                for bulkShotList in list:
                    os.makedirs(name=f"{shotNameExclussive}_{bulkShotList}")

                os.chdir(f"{shotNameExclussive}_01")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 01
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_02")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 02
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_03")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 03
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_04")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 04
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_05")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 05
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_06")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 06
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_07")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 07
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_08")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 08
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_09")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 09
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_10")
                print(f"{os.getcwd()}")

                shotCore() # for shot number 10
                os.chdir('../')

                os.chdir(f"{shotNameExclussive}_seq")
                print(f"{os.getcwd()}")

                shotCore() # for seq
                os.chdir('../')
                #print(f"{os.getcwd()}")

            
        
        else:
            print('are You Mad, provide a shot name followed by _ Seq name, next time you will run the tool')

    except OSError as e:
        print(f"--Error creating directory- {seqNameExclussivePath}: {e}")
        # *******UI_LOG****** #
        log_lableE = ctk.CTkLabel(terminalLog_frame, text=(f"--Error creating directory {seqNameExclussivePath}: {e}"), text_color='red', font=ctk.CTkFont(size=11, weight='normal'), justify='left' )
        log_lableE.pack()

"""
#################
GenExclussive Button
#################
"""



# Generatte button exclussive ###########################################################################################
generateExcl_button = ctk.CTkButton(operationPannel_frame, text="Generate", width=100, fg_color="black", command=genExclussive ) 
generateExcl_button.place(x=850, y=240)

##############################################################################################################################







"""
Application Run

"""

# Start the CustomTKinter event loop | Start the Application
root.mainloop()
print("============================================")