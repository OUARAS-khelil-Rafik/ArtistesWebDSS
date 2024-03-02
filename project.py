from xml.dom import minidom
from xml.dom.minidom import parse

dom= parse('artisteDevoir.xml')

fichier=open('ArtistesWeb.html','w')

artist=dom.getElementsByTagName("artiste")

album=dom.getElementsByTagName("album")

fichier.write('<!doctype html>\n')
fichier.write('<html>\n')
fichier.write('<head>\n')
fichier.write('<title> Projet DSS </title>\n')
fichier.write('</head>\n')
fichier.write('<body style="background-color: black">\n')
fichier.write('<h1 style="text-align: center; color: red; margin: 30px">LISTE ARTISTES</h1>\n')

for el in artist:
    
    nom=el.getAttribute('nom')
    fichier.write('<h2 style="text-align: center; color:green;" >NOM: ' +nom+ '</h2>\n')
    img_src = el.getElementsByTagName('img')[0].getAttribute('src')
    img_alt = el.getElementsByTagName('img')[0].getAttribute('alt')
    fichier.write('<img src="' + img_src + '" alt="' + img_alt + '" style="width: 350px; height: 350px; border: 1px dashed red; text-align: center; display: block; margin-left: auto; margin-right: auto;">\n')
    ville=el.getAttribute('ville')
    fichier.write('<h2 style="text-align: center; color:white;">Ville: '+ville+'</h2>\n')
    site= el.childNodes[1].getAttribute('url')
    fichier.write('<h2 style="text-align: center; color:blue;">Site: <a href="'+site+'">'+site+'</a></h2>\n')
    ref= el.getAttribute('no')
    fichier.write('<h2 style="text-align: center; color:white;">Production</h2>\n')
    fichier.write('<table BORDER="2" style="margin-left: auto; margin-right: auto; border-color:green;">\n')
    for i in range(album.length):
      a=album[i].childNodes[3].attributes['ref'].nodeValue
      
      if(a==ref) : 
         titre=album[i].getElementsByTagName('titre')[0].childNodes[0].nodeValue
         fichier.write('<tr><td style="text-align: center; color: red; border: 1px solid green; padding: 8px;"><b>NOM ALBUM</b></td>\n')
         fichier.write('<td style="text-align: center; color: white; border: 1px solid green; padding: 8px;">\n')
         fichier.write('<b>'+titre+'</b>\n')
         fichier.write('</td></tr>\n')
         chanson=album[i].getElementsByTagName('chanson')
         
         for k in range(chanson.length):
            c=chanson[k].childNodes[0].nodeValue
         fichier.write('<tr style="border: 1,5px solid green;" >\n')
         fichier.write('<td style="text-align: center; color:blue; border: 1px solid green; padding: 8px;"><b>CHANSON</b></td>\n')
         fichier.write('<td style="text-align: center; color:white; border: 1px solid green; padding: 8px;">'+c+'</td></tr>\n')
    fichier.write('</table>\n')
    fichier.write('<hr style="color: red; border-width: 2px; margin-right: 100px; margin-left: 100px; margin-bottom: 60px; margin-top: 60px; border-style: dashed;">')

fichier.write('<h2 style="text-align: center; color: white; border: 2px dashed red; border-radius: 5px; padding: 10px; margin-left: 150px; margin-right: 150px;"> Cette page est realisee par l\'etudiant : OUARAS KHELIL RAFIK, Groupe: 01</h2>\n')     
fichier.write('</body>\n')
fichier.write('</html>')
fichier.close()