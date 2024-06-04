"""Simple Wrapper for pdftk"""

__all__ = ['pdftk']
__author__ = "Prince Kumar"
__version__ = "0.1.0-alpha"


from subprocess import run as srun
from os.path import basename,dirname,join as osjoin,exists,getsize,isfile,isdir,basename
from os import getcwd,chdir, mkdir,rename,remove as osremove
import time 
import shutil


class _PDF:
  def __init__(self,file):
    self.filename=basename(file)
    self.directory=dirname(file) if (dirname(file)!='') else getcwd()
    self.full_path=osjoin(self.directory,self.filename)

class _utils:
  def __init__(self):
    pass
  def prevent_overwrite(self,nam):
    if isfile(nam):
      return self.prevent_overwrite(nam[:-4] + '(1)' + nam[-4:])
    else:
      return nam
    
#pdftk does not create non existing folder

class pdftk:
  """Complete wrapper for pdftk."""
  def __init__(self) -> None:
    self.executable='pdftk'
    if not shutil.which('pdftk'):
      raise Exception("Pdftk is not installed. First Make sure that it is installed and is on path")
    self.cmd=[self.executable]
  def execute(self):
    peo=srun(self.cmd,capture_output=False)
    return True if (peo.returncode==0) else False
  def get_page_count(self,pdf):
    self.cmd+=[pdf, 'dump_data']
    peo=srun(self.cmd,capture_output=True,text=True)
    if peo.returncode==0:
      for line in peo.stdout.splitlines():
        if line.startswith('NumberOfPages'):
          num_pages = int(line.split(':')[1].strip())
          return num_pages
  def merge(self,input_files:list,output=None,user_pw=None,owner_pw=None):
    pdf=_PDF(input_files[0])
    self.cmd+=input_files
    if not output:
      output=osjoin(pdf.directory,pdf.filename[:-4] + '_merged.pdf')
    output=_PDF(_utils().prevent_overwrite(output)).full_path
    self.cmd+=['output',output]
    if owner_pw:
      self.cmd+=['owner_pw',owner_pw]
    if user_pw:
      self.cmd+=['user_pw',user_pw]
    return output if (self.execute()) else None
  def burst_pdf(self,pdf,output_folder=None,input_pw=None):
    pdf=_PDF(pdf)
    fol=osjoin(pdf.directory,str(time.time())) if not output_folder else output_folder
    if not exists(fol):
      mkdir(fol)
    self.cmd+=[pdf.full_path]
    if input_pw:
      self.cmd+=['input_pw',input_pw]
    self.cmd+=['burst','output',f'{fol}/{pdf.filename[:-4]}_%04d_.pdf']
    return fol if (self.execute()) else None 
  def decrypt(self,pdf,input_pw,output=None):
    pdf=_PDF(pdf)
    if not output:
      output=osjoin(pdf.directory,pdf.filename[:-4]+'_decrypted.pdf')
    output=_PDF(_utils().prevent_overwrite(output)).full_path
    self.cmd+=[pdf.full_path,'input_pw',input_pw,'output',output]
    return output if (self.execute()) else None
  def encrypt(self,pdf,user_pw=None,owner_pw=None,output=None):
    if not (user_pw or owner_pw):
      raise Exception('At least one of user_pw or owner_pw is required.')
    pdf=_PDF(pdf)
    if not output:
      output=osjoin(pdf.directory,pdf.filename[:-4]+'_encrypted.pdf')
    output=_PDF(_utils().prevent_overwrite(output)).full_path
    self.cmd+=[pdf.full_path,'output',output]
    if owner_pw:
      self.cmd+=['owner_pw',owner_pw]
    if user_pw:
      self.cmd+=['user_pw',user_pw]
    return output if (self.execute()) else None
  def add_background(self,pdf,back_pdf,input_pw=None,multi=False, user_pw=None, owner_pw=None,output=None):
    """If the input PDF does not have a transparent background (such as a PDF created from page scans) then
		 the resulting background won't be visible -- use the add_stamp operation instead."""
    pdf=_PDF(pdf)
    if not output:
      output=osjoin(pdf.directory,pdf.filename[:-4]+'_addbkgnd.pdf')
    output=_PDF(_utils().prevent_overwrite(output)).full_path
    self.cmd+=[pdf.full_path]
    if input_pw:
      self.cmd+=['input_pw',input_pw]
    if multi:
      self.cmd+=['multibackground',back_pdf]
    else:
      self.cmd+=['background',back_pdf]
    self.cmd+=['output',output]
    if user_pw:
      self.cmd+=['user_pw',user_pw]
    if owner_pw:
      self.cmd+=['owner_pw',owner_pw]
    return output if (self.execute()) else None
  def add_stamp(self,pdf,back_pdf,input_pw=None,multi=False, user_pw=None, owner_pw=None,output=None):
    pdf=_PDF(pdf)
    if not output:
      output=osjoin(pdf.directory,pdf.filename[:-4]+'_stamped.pdf')
    output=_PDF(_utils().prevent_overwrite(output)).full_path
    self.cmd+=[pdf.full_path]
    if input_pw:
      self.cmd+=['input_pw',input_pw]
    if multi:
      self.cmd+=['multistamp',back_pdf]
    else:
      self.cmd+=['stamp',back_pdf]
    self.cmd+=['output',output]
    if user_pw:
      self.cmd+=['user_pw',user_pw]
    if owner_pw:
      self.cmd+=['owner_pw',owner_pw]
    return output if (self.execute()) else None
  def split_pdf(self,pdf,page_or_range:list,output=None,input_pw=None):
    pdf=_PDF(pdf)
    self.cmd+=[pdf.full_path]
    if input_pw:
      self.cmd+=['input_pw',input_pw]
    self.cmd+=['cat',*page_or_range]
    if not output:
      output=pdf[:-4]+ 'split.pdf'
    output=_PDF(_utils().prevent_overwrite(output)).full_path
    self.cmd+=['output',output]
    return output if (self.execute()) else None
  def rotate_pdf(self,pdf,direction='north',page_ranges='1-end',output=None,input_pw=None, user_pw=None, owner_pw=None):
    """Each option sets the page rotation as follows (in degrees): north: 0,east: 90, south: 180, west: 270, left: -90,
     right: +90, down: +180. left, right, and down make relative adjustments to a page's rotation."""
    pdf=_PDF(pdf)
    self.cmd+=[pdf.full_path]
    if input_pw:
      self.cmd+=['input_pw',input_pw]
    self.cmd+=['rotate',page_ranges+direction]
    if not output:
      output=pdf[:-4]+ 'rotated'+direction+'.pdf'
    output=_PDF(_utils().prevent_overwrite(output)).full_path
    self.cmd+=['output',output]
    if user_pw:
      self.cmd+=['user_pw',user_pw]
    if owner_pw:
      self.cmd+=['owner_pw',owner_pw]
    return output if (self.execute()) else None


  
'''
def add_chapters(dict_of_chaps_and_pg_no):
    txtf=str(time.time())+'.txt'
    for key,value in dict_of_chaps_and_pg_no.items():
      with open(txtf,'a') as f:
        f.write(f'[/Page {value} /Title ({key}) /OUT pdfmark')
    return txtf
'''






