# from mymodule import my_func # Calling function directly from main module package

# # calling my_func from module file
# my_func()


# Calling main package , importing main_script from main package
from MyMainPackage import my_main_script
# Calling sub-package inside main package , import sub_script from sub-package
from MyMainPackage.SubPackage import my_sub_script

my_main_script.report_main()
my_sub_script.sub_report()
