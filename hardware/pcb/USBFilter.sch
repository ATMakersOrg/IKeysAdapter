<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.5.2">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="24" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="88" name="SimResults" color="9" fill="1" visible="yes" active="yes"/>
<layer number="89" name="SimProbes" color="9" fill="1" visible="yes" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="ATMakers">
<packages>
<package name="TRINKET">
<description>Trinket M0</description>
<wire x1="7.62" y1="11.43" x2="7.62" y2="-11.684" width="0.025" layer="21"/>
<wire x1="7.62" y1="-11.684" x2="6.858" y2="-12.446" width="0.025" layer="21"/>
<wire x1="6.858" y1="-12.446" x2="3.556" y2="-12.446" width="0.025" layer="21"/>
<wire x1="3.556" y1="-12.446" x2="2.032" y2="-13.97" width="0.025" layer="21"/>
<wire x1="2.032" y1="-13.97" x2="-5.08" y2="-13.97" width="0.025" layer="21"/>
<wire x1="-5.08" y1="-13.97" x2="-6.858" y2="-12.192" width="0.025" layer="21"/>
<wire x1="-6.858" y1="-12.192" x2="-7.62" y2="-12.192" width="0.025" layer="21"/>
<wire x1="-7.62" y1="-12.192" x2="-7.62" y2="11.43" width="0.025" layer="21"/>
<wire x1="-6.35" y1="12.7" x2="-7.62" y2="11.43" width="0.025" layer="21" curve="90"/>
<wire x1="-6.35" y1="12.7" x2="-2.794" y2="12.7" width="0.025" layer="21"/>
<wire x1="-2.794" y1="12.7" x2="-2.413" y2="12.319" width="0.025" layer="21"/>
<wire x1="-2.413" y1="12.319" x2="2.413" y2="12.319" width="0.025" layer="21"/>
<wire x1="2.413" y1="12.319" x2="2.794" y2="12.7" width="0.025" layer="21"/>
<wire x1="2.794" y1="12.7" x2="6.35" y2="12.7" width="0.025" layer="21"/>
<wire x1="7.62" y1="11.43" x2="6.35" y2="12.7" width="0.025" layer="21" curve="90"/>
<circle x="-6.096" y="6.223" radius="1.1" width="0.025" layer="21"/>
<circle x="6.096" y="6.223" radius="1.1" width="0.025" layer="21"/>
<wire x1="3.699990625" y1="9.63198125" x2="4.050003125" y2="9.982" width="0.025" layer="21" curve="90.001023"/>
<wire x1="3.699990625" y1="9.632009375" x2="3.499990625" y2="9.632009375" width="0.025" layer="21"/>
<wire x1="3.14998125" y1="9.982" x2="3.499990625" y2="9.631990625" width="0.025" layer="21" curve="90"/>
<wire x1="3.150009375" y1="9.982" x2="3.150009375" y2="10.532009375" width="0.025" layer="21"/>
<wire x1="3.500009375" y1="10.932009375" x2="3.499990625" y2="10.932009375" width="0.025" layer="21" curve="0.002852"/>
<wire x1="3.499990625" y1="10.932009375" x2="3.15" y2="10.532" width="0.025" layer="21" curve="89.997148"/>
<wire x1="3.499990625" y1="10.932009375" x2="3.699990625" y2="10.932009375" width="0.025" layer="21"/>
<wire x1="4.050009375" y1="10.532" x2="3.7" y2="10.932009375" width="0.025" layer="21" curve="90"/>
<wire x1="4.05" y1="10.532009375" x2="4.05" y2="9.982" width="0.025" layer="21"/>
<wire x1="-3.6" y1="10.93201875" x2="-4.0500125" y2="10.582009375" width="0.025" layer="21" curve="89.999945"/>
<wire x1="-3.15" y1="10.582009375" x2="-3.600009375" y2="10.93201875" width="0.025" layer="21" curve="90"/>
<wire x1="-4.05" y1="9.982" x2="-4.05" y2="10.582" width="0.025" layer="21"/>
<wire x1="-4.05001875" y1="9.982009375" x2="-3.6" y2="9.63199375" width="0.025" layer="21" curve="90.000937"/>
<wire x1="-3.600009375" y1="9.632" x2="-3.14999375" y2="9.982009375" width="0.025" layer="21" curve="90.001377"/>
<wire x1="-3.150009375" y1="10.582" x2="-3.150009375" y2="9.982" width="0.025" layer="21"/>
<circle x="1.950009375" y="8.382" radius="0.350009375" width="0.025" layer="21"/>
<circle x="-1.950009375" y="8.382" radius="0.350009375" width="0.025" layer="21"/>
<pad name="BAT" x="-6.35" y="3.81" drill="1" diameter="2.1844"/>
<pad name="GND" x="-6.35" y="1.27" drill="1" diameter="2.1844"/>
<pad name="4" x="-6.35" y="-1.27" drill="1" diameter="2.1844"/>
<pad name="3" x="-6.35" y="-3.81" drill="1" diameter="2.1844"/>
<pad name="RST" x="-6.35" y="-6.35" drill="1" diameter="2.1844"/>
<pad name="USB" x="6.35" y="3.81" drill="1" diameter="2.1844"/>
<pad name="0" x="6.35" y="1.27" drill="1" diameter="2.1844"/>
<pad name="1" x="6.35" y="-1.27" drill="1" diameter="2.1844"/>
<pad name="2" x="6.35" y="-3.81" drill="1" diameter="2.1844"/>
<pad name="3V" x="6.35" y="-6.35" drill="1" diameter="2.1844"/>
<pad name="TR12" x="5.715" y="-10.16" drill="2" diameter="3"/>
<pad name="TR11" x="-5.715" y="-10.16" drill="2" diameter="3"/>
<text x="1.27" y="-5.08" size="1.778" layer="21" rot="R90">Trinket M0</text>
</package>
</packages>
<symbols>
<symbol name="TRINKETM0">
<pin name="BAT" x="-20.32" y="5.08" length="middle"/>
<pin name="GND" x="-20.32" y="2.54" length="middle"/>
<pin name="4" x="-20.32" y="0" length="middle"/>
<pin name="3" x="-20.32" y="-2.54" length="middle"/>
<pin name="RST" x="-20.32" y="-5.08" length="middle"/>
<pin name="3V" x="20.32" y="-5.08" length="middle" rot="R180"/>
<pin name="2" x="20.32" y="-2.54" length="middle" rot="R180"/>
<pin name="1" x="20.32" y="0" length="middle" rot="R180"/>
<pin name="0" x="20.32" y="2.54" length="middle" rot="R180"/>
<pin name="USB" x="20.32" y="5.08" length="middle" rot="R180"/>
<wire x1="-15.24" y1="15.24" x2="15.24" y2="15.24" width="0.254" layer="94"/>
<wire x1="15.24" y1="15.24" x2="15.24" y2="-15.24" width="0.254" layer="94"/>
<wire x1="15.24" y1="-15.24" x2="-15.24" y2="-15.24" width="0.254" layer="94"/>
<wire x1="-15.24" y1="-15.24" x2="-15.24" y2="15.24" width="0.254" layer="94"/>
<text x="-15.24" y="15.494" size="1.778" layer="95">&gt;NAME</text>
<text x="-15.24" y="-17.78" size="1.778" layer="96">&gt;VALUE</text>
<text x="-5.08" y="10.16" size="1.778" layer="97">Trinket M0</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="TRINKETM0">
<description>Trinket M0</description>
<gates>
<gate name="G$1" symbol="TRINKETM0" x="0" y="0"/>
</gates>
<devices>
<device name="" package="TRINKET">
<connects>
<connect gate="G$1" pin="0" pad="0"/>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="3V" pad="3V"/>
<connect gate="G$1" pin="4" pad="4"/>
<connect gate="G$1" pin="BAT" pad="BAT"/>
<connect gate="G$1" pin="GND" pad="GND"/>
<connect gate="G$1" pin="RST" pad="RST"/>
<connect gate="G$1" pin="USB" pad="USB"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="U$1" library="ATMakers" deviceset="TRINKETM0" device=""/>
<part name="U$2" library="ATMakers" deviceset="TRINKETM0" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="U$1" gate="G$1" x="-43.18" y="63.5" smashed="yes">
<attribute name="NAME" x="-58.42" y="78.994" size="1.778" layer="95"/>
<attribute name="VALUE" x="-58.42" y="45.72" size="1.778" layer="96"/>
</instance>
<instance part="U$2" gate="G$1" x="-43.18" y="25.4" smashed="yes">
<attribute name="NAME" x="-58.42" y="40.894" size="1.778" layer="95"/>
<attribute name="VALUE" x="-58.42" y="7.62" size="1.778" layer="96"/>
</instance>
</instances>
<busses>
</busses>
<nets>
<net name="N$1" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="4"/>
<wire x1="-63.5" y1="63.5" x2="-73.66" y2="63.5" width="0.1524" layer="91"/>
<pinref part="U$2" gate="G$1" pin="3"/>
<wire x1="-73.66" y1="63.5" x2="-73.66" y2="22.86" width="0.1524" layer="91"/>
<wire x1="-73.66" y1="22.86" x2="-63.5" y2="22.86" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$2" class="0">
<segment>
<pinref part="U$2" gate="G$1" pin="4"/>
<wire x1="-63.5" y1="25.4" x2="-71.12" y2="25.4" width="0.1524" layer="91"/>
<pinref part="U$1" gate="G$1" pin="3"/>
<wire x1="-71.12" y1="25.4" x2="-71.12" y2="60.96" width="0.1524" layer="91"/>
<wire x1="-71.12" y1="60.96" x2="-63.5" y2="60.96" width="0.1524" layer="91"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="GND"/>
<wire x1="-63.5" y1="66.04" x2="-78.74" y2="66.04" width="0.1524" layer="91"/>
<wire x1="-78.74" y1="66.04" x2="-78.74" y2="27.94" width="0.1524" layer="91"/>
<pinref part="U$2" gate="G$1" pin="GND"/>
<wire x1="-78.74" y1="27.94" x2="-63.5" y2="27.94" width="0.1524" layer="91"/>
</segment>
</net>
<net name="USB" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="USB"/>
<wire x1="-22.86" y1="68.58" x2="-15.24" y2="68.58" width="0.1524" layer="91"/>
<pinref part="U$2" gate="G$1" pin="USB"/>
<wire x1="-15.24" y1="68.58" x2="-15.24" y2="30.48" width="0.1524" layer="91"/>
<wire x1="-15.24" y1="30.48" x2="-22.86" y2="30.48" width="0.1524" layer="91"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
