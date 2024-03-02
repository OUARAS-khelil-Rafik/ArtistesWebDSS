<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
    <html>
        <head>
            <title>Projet DSS</title>
        </head>
        <body style="background-color: black">
            <h1 style="text-align: center; color: red; margin: 30px">LISTE ARTISTES</h1>
            <xsl:for-each select="CD/artiste">
                <xsl:variable name="ref" select="@no"/>
                <h2 style="text-align: center; color: green;">NOM: <xsl:value-of select="@nom"/></h2>
                <img src="{img/@src}" alt="{img/@alt}" style="width: 350px; height: 350px; border: 1px dashed red; text-align: center; display: block; margin-left: auto; margin-right: auto;"/>
                <h2 style="text-align: center; color: white;">Ville: <xsl:value-of select="@ville"/></h2>
                <h2 style="text-align: center; color: blue;">Site: <a href="{site/@url}"><xsl:value-of select="site/@url"/></a></h2>
                <h2 style="text-align: center; color: white;">Production</h2>
                <table border="2" style="margin-left: auto; margin-right: auto; border-color: green;">
                    <xsl:for-each select="/CD/album[ref-artiste/@ref = $ref]">
                        <xsl:variable name="album" select="."/>
                        <tr>
                            <td style="text-align: center; color: red; border: 1px solid green; padding: 8px;"><b>NOM ALBUM</b></td>
                            <td style="text-align: center; color: white; border: 1px solid green; padding: 8px;"><b><xsl:value-of select="titre"/></b></td>
                        </tr>
                        <xsl:for-each select="chansons/chanson">
                            <tr style="border: 1.5px solid green;">
                                <td style="text-align: center; color: blue; border: 1px solid green; padding: 8px;"><b>CHANSON</b></td>
                                <td style="text-align: center; color: white; border: 1px solid green; padding: 8px;">
                                    <xsl:value-of select="."/>
                                </td>
                            </tr>
                        </xsl:for-each>
                    </xsl:for-each>
                </table>
                <hr style="color: red; border-width: 2px; margin-right: 100px; margin-left: 100px; margin-bottom: 60px; margin-top: 60px; border-style: dashed;"/>
            </xsl:for-each>
            <h2 style="text-align: center; color: white; border: 2px dashed red; border-radius: 5px; padding: 10px; margin-left: 150px; margin-right: 150px;">Cette page est réalisée par l'étudiant : OUARAS KHELIL RAFIK, Groupe: 01</h2>
        </body>
    </html>
</xsl:template>

</xsl:stylesheet>
