require 'rspec'
require 'rubygems'
require 'selenium-webdriver'
require 'win32ole'

#~ describe "163mail login" do 

	#~ before(:all) do
		#~ dr = Selenium::WebDriver.for :ff
		#~ url='https://passport.cnblogs.com/register.aspx'
		#~ dr.navigate.to url
		#~ sleep 3
		excel = WIN32OLE.new("excel.application")
		filepath="F:\\autotest\\ruby\\loadexcel\\Data.xlsx" #路径用两斜杠
		workbook = excel.workbooks.open(filepath)
		worksheet=workbook.worksheets(1)
		works2=workbook.worksheets(2)
		#worksheet=workbook.worksheets("sheet name") 打开表名
		#读取excel文件
		row=2
	#~ end

	#~ it "read excel" do
	while works2.range("a#{row}").value
		
		eid=works2.range("a#{row}").value.to_s
		#~ eid=eidin.value.to_s
		emsg=works2.range("b#{row}").value.to_s
		#~ emsg=emsgin.value.to_s
		
		row+=1
		
		puts eid
		puts emsg
	end
		
		workbook.save
		system ("tskill EXCEL")
		
		#~ dr.quit