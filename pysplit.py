'''
Created on Jul 24, 2013
    A utility for use with Udacity or other compatible Python classes.
    Requirements: 
    Files are saved in the same folder or subdirectory.
    Lessons/Chapters/Topics are saved as separate files
    Comment lines begin with #, and questions are posted as comments.
    Each question - solution pair is separated with a single line starting with !
    Code, spaces, or tab characters must precede comments that are to be included within the code.
    To select a single file, exit first prompt window and a file selector window will appear.
    #@author: lily
'''
    
import os
# settings
primary_extension = '.txt'
question_extension = '.txt'
solution_extension = '.py'
question_append = 'qts'
solution_append = 'sol'
question_subdir = './questions/'
solution_subdir = './solutions/'
reddit_subdir = './reddit/'

#global root DO NOT MODIFY
root = None

# selects a single file or directory and runs conversion on the file or on all text files in that directory.
def run():
    # query user using directory GUI and return path selected
    root = selector(True)
    
    is_directory = os.path.isdir(root)
    if is_directory:
        os.chdir(root)
        subdir()
        # convert every file in the selected directory with predefined file extension.    
        for file_ in os.listdir('.'):
            if file_.endswith(primary_extension):
                convert(file_)
    # single-file conversion if directory selector is exited
    else:
        file_ = selector(False)
        convert(file_)
    # end run()
    
#takes in a string representation of the original filename and returns two new file names: question_name and solution_name according to the configuration.   
def new_filenames(old_name):
    ext_pos = old_name[::-1].find('.')
    name = old_name[:len(old_name)-ext_pos]
    question_name = name+question_append+question_extension 
    solution_name = name+solution_append+solution_extension
    print 'new file names generated'
    return question_name, solution_name
    # end new_filenames()
    
# Function presents the user with a GUI to select a directory and returns the path.
def selector(get_dir):
    # using Tkinter lib to create GUI navigation elements
    import Tkinter, tkFileDialog
    root = Tkinter.Tk()
    # hide the parent window
    root.withdraw()
    #present user with GUI input
    file_path = None
    # method will choose a directory if get_dir argument is True, and a file if it is False.
    if get_dir:
        file_path = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    else:
        file_path = tkFileDialog.askopenfilename(parent=root,initialdir="/",title='Please select a file')
    return file_path
    # end selector()

# creates all necessary subdirectories in the root folder if they do not already exist.    
def subdir():
    #os.chdir(root)
    try:
        os.makedirs(question_subdir)
    except OSError:
            pass
    try:
        os.makedirs(solution_subdir)
    except OSError:
            pass
    try:
        os.makedirs(reddit_subdir)
    except OSError:
            pass
        
# formats the input string into a reddit version of a bold string.        
def bold(string):
    return '**'+string+'**'

# primary function of pysplit. This portion takes in a filename, reads the file, and creates two new files: questions and solutions.
def convert(filename):
    print filename
    try:
        # open the passed in filename for reading
        seed_file = open(filename)
        # retrieve new file names
        question_name, solution_name = new_filenames(filename)
        
        # navigate to subdirectories, create and open new files
        os.chdir(question_subdir)
        question_file = open(question_name,'w')
        os.chdir('..')
        os.chdir(reddit_subdir)
        reddit_file = open(question_name,'w')
        os.chdir('..')
        os.chdir(solution_subdir)
        solution_file = open(solution_name,'w')
        os.chdir('..')
        
        # some helper variables
        num_questions = 1
        n = '\n'
        t = '    '
        defined = 'none'
        # all files are ready for use
        question_file.write("Question #"+str(num_questions)+n+n)
        reddit_file.write(n+"**Question #"+str(num_questions)+"**"+n+n)
        solution_file.write("##Solution #"+str(num_questions)+n+n)
        num_questions += 1
        # parse lines in the file
        for line in seed_file:
            if line.strip():                # skips any empty lines
                if line[0] =='#':           # writes the question text into the question and reddit files.
                    question_file.write(t+line[1:])
                    reddit_file.write(line[1:])
                elif line[0] == '!':        # handle new questions. Denote new questions to all files.
                    if defined!='none':
                        solution_file.write('# end'+defined+n+n)
                        defined = 'none'
                    question_file.write(n+"Question #"+str(num_questions)+n+n)
                    reddit_file.write(n+"**Question #"+str(num_questions)+"**"+n+n)
                    solution_file.write("##Solution #"+str(num_questions)+n+n)
                    num_questions += 1
                else:                       # parse solution to add the end def comments.
                    if line[0:4]!='    ':
                        if defined!='none':
                            solution_file.write('# end'+defined+n+n)
                    if line[0:3]=='def':         
                        defined = line[3:line.find(':')]
                        
                    solution_file.write(line)# handle solutions, write to solution file

        seed_file.close()
        question_file.close()
        solution_file.close()
        
    except:
        print 'Conversion Failed'

# not yet implemented   
def config_append(question_append, solution_append): pass
def config_dir(question_dir, solution_dir): pass
def config_ext(question_ext, solution_ext): pass
        
# run split program if module running as primary program    
if __name__ == '__main__':
    run()