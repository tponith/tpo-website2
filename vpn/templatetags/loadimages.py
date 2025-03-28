from django import template
register = template.Library()

@register.simple_tag
def count_images():
	imgnames = ['accen.png' ,'af.png' ,'al.png' ,'ang.png' ,'aq.png' ,'bosch.jpg' ,'ca.jpg' ,'cap.jpg' ,'cog.png' ,'eo.png' ,'fa.png' ,'fd.jpg' ,'ff.png' ,'gb.jpeg' ,'gl.jpg' ,'godrej.png' ,'gs.jpg' ,'hm.jpg' ,'honda.jpg' ,'hsbc.png' ,'ibm.png' ,'ic.png' ,'im.png' ,'infosys.jpg' ,'int.jpg' ,'is.jpg' ,'itti.png' ,'iz.jpg' ,'jcb.jpg' ,'jio.jpg' ,'jug.png' ,'kec.png' ,'kpit.png' ,'lntin.png' ,'lnt.jpg' ,'maruti.jpg' ,'msi.png' ,'new.jpg' ,'ocean.jpg' ,'oracle.jpg' ,'ori.jpg' ,'pb.jpg' ,'ril.png' ,'sa.jpg' ,'samsung.png' ,'sap.png' ,'sd.png' ,'sm.jpg' ,'sub.png' ,'tech.jpg' ,'th.jpg' ,'tmj.jpg' ,'tpd.jpg' ,'uf.png' ,'uhg.png' ,'united.png' ,'ved.jpg' ,'vir.jpg' ,'vz.jpg' ,'wipro.png' ,'xl.png' ,'yod.jpg' ,'za.png' ,'zs.png','ba.jpg','bloomberg.png','jp.png','bs.gif' ]
	lastval = len(imgnames)
	return lastval

@register.simple_tag
def img_names():
	imgnames = ['accen.png' ,'af.png' ,'al.png' ,'ang.png' ,'aq.png' ,'bosch.jpg' ,'ca.jpg' ,'cap.jpg' ,'cog.png' ,'eo.png' ,'fa.png' ,'fd.jpg' ,'ff.png' ,'gb.jpeg' ,'gl.jpg' ,'godrej.png' ,'gs.jpg' ,'hm.jpg' ,'honda.jpg' ,'hsbc.png' ,'ibm.png' ,'ic.png' ,'im.png' ,'infosys.jpg' ,'int.jpg' ,'is.jpg' ,'itti.png' ,'iz.jpg' ,'jcb.jpg' ,'jio.jpg' ,'jug.png' ,'kec.png' ,'kpit.png' ,'lntin.png' ,'lnt.jpg' ,'maruti.jpg' ,'msi.png' ,'new.jpg' ,'ocean.jpg' ,'oracle.jpg' ,'ori.jpg' ,'pb.jpg' ,'ril.png' ,'sa.jpg' ,'samsung.png' ,'sap.png' ,'sd.png' ,'sm.jpg' ,'sub.png' ,'tech.jpg' ,'th.jpg' ,'tmj.jpg' ,'tpd.jpg' ,'uf.png' ,'uhg.png' ,'united.png' ,'ved.jpg' ,'vir.jpg' ,'vz.jpg' ,'wipro.png' ,'xl.png' ,'yod.jpg' ,'za.png' ,'zs.png','ba.jpg','bloomberg.png','jp.png','bs.gif' ]
	return imgnames
