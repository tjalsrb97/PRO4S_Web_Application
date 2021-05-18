var wms_layers = [];

var format_temp_0 = new ol.format.GeoJSON();
var features_temp_0 = format_temp_0.readFeatures(json_temp_0, {
    dataProjection: 'EPSG:4326',
    featureProjection: 'EPSG:3857'
});
var jsonSource_temp_0 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_temp_0.addFeatures(features_temp_0);
var lyr_temp_0 = new ol.layer.Vector({
    declutter: true,
    source: jsonSource_temp_0,
    style: style_temp_0,
    interactive: true,
    title: 'temp<br />\
    <img src="styles/legend/temp_0_0.png" /> -117.43 - -113.21<br />\
    <img src="styles/legend/temp_0_1.png" /> -113.21 - -111.96<br />\
    <img src="styles/legend/temp_0_2.png" /> -111.96 - -111.06<br />\
    <img src="styles/legend/temp_0_3.png" /> -111.06 - -110.28<br />\
    <img src="styles/legend/temp_0_4.png" /> -110.28 - -109.61<br />\
    <img src="styles/legend/temp_0_5.png" /> -109.61 - -108.95<br />\
    <img src="styles/legend/temp_0_6.png" /> -108.95 - -108.39<br />\
    <img src="styles/legend/temp_0_7.png" /> -108.39 - -107.91<br />\
    <img src="styles/legend/temp_0_8.png" /> -107.91 - -107.48<br />\
    <img src="styles/legend/temp_0_9.png" /> -107.48 - -107.17<br />\
    <img src="styles/legend/temp_0_10.png" /> -107.17 - -106.81<br />\
    <img src="styles/legend/temp_0_11.png" /> -106.81 - -106.48<br />\
    <img src="styles/legend/temp_0_12.png" /> -106.48 - -106.14<br />\
    <img src="styles/legend/temp_0_13.png" /> -106.14 - -105.81<br />\
    <img src="styles/legend/temp_0_14.png" /> -105.81 - -105.48<br />\
    <img src="styles/legend/temp_0_15.png" /> -105.48 - -105.17<br />\
    <img src="styles/legend/temp_0_16.png" /> -105.17 - -104.84<br />\
    <img src="styles/legend/temp_0_17.png" /> -104.84 - -104.54<br />\
    <img src="styles/legend/temp_0_18.png" /> -104.54 - -104.26<br />\
    <img src="styles/legend/temp_0_19.png" /> -104.26 - -103.95<br />\
    <img src="styles/legend/temp_0_20.png" /> -103.95 - -103.67<br />\
    <img src="styles/legend/temp_0_21.png" /> -103.67 - -103.3<br />\
    <img src="styles/legend/temp_0_22.png" /> -103.3 - -102.91<br />\
    <img src="styles/legend/temp_0_23.png" /> -102.91 - -102.6<br />\
    <img src="styles/legend/temp_0_24.png" /> -102.6 - -102.18<br />\
    <img src="styles/legend/temp_0_25.png" /> -102.18 - -101.81<br />\
    <img src="styles/legend/temp_0_26.png" /> -101.81 - -101.34<br />\
    <img src="styles/legend/temp_0_27.png" /> -101.34 - -100.9<br />\
    <img src="styles/legend/temp_0_28.png" /> -100.9 - -100.39<br />\
    <img src="styles/legend/temp_0_29.png" /> -100.39 - -99.93<br />\
    <img src="styles/legend/temp_0_30.png" /> -99.93 - -99.35<br />\
    <img src="styles/legend/temp_0_31.png" /> -99.35 - -98.67<br />\
    <img src="styles/legend/temp_0_32.png" /> -98.67 - -97.88<br />\
    <img src="styles/legend/temp_0_33.png" /> -97.88 - -96.63<br />\
    <img src="styles/legend/temp_0_34.png" /> -96.63 - -89.4<br />'
});
var format_Gangnam_1m_1 = new ol.format.GeoJSON();
var features_Gangnam_1m_1 = format_Gangnam_1m_1.readFeatures(json_Gangnam_1m_1, {
    dataProjection: 'EPSG:4326',
    featureProjection: 'EPSG:3857'
});
var jsonSource_Gangnam_1m_1 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_Gangnam_1m_1.addFeatures(features_Gangnam_1m_1);
var lyr_Gangnam_1m_1 = new ol.layer.Vector({
    declutter: true,
    source: jsonSource_Gangnam_1m_1,
    style: style_Gangnam_1m_1,
    interactive: true,
    title: '<img src="styles/legend/Gangnam_1m_1.png" /> Gangnam_1m'
});

lyr_temp_0.setVisible(true);
lyr_Gangnam_1m_1.setVisible(true);
var layersList = [lyr_temp_0, lyr_Gangnam_1m_1];
lyr_temp_0.set('fieldAliases', {
    'idx': 'idx',
    'RX': 'RX',
    'RY': 'RY',
    'TX': 'TX',
    'TY': 'TY',
    'TZ': 'TZ',
    'azimuth': 'azimuth',
    'tilts': 'tilts',
    'chai1': 'chai1',
    'chai2': 'chai2',
    'dist': 'dist',
    'predict': 'predict',
    'pre2': 'pre2',
    'wb1': 'wb1',
    'wb2': 'wb2',
    'wb3': 'wb3',
    'hj1': 'hj1',
    'hj2': 'hj2',
});
lyr_Gangnam_1m_1.set('fieldAliases', {
    'AGL': 'AGL',
    'AMSL': 'AMSL',
    'PRIORITY': 'PRIORITY',
    'CLUTTER': 'CLUTTER',
    'IDENTICAL': 'IDENTICAL',
    'UNIQUE_ID': 'UNIQUE_ID',
    'EDITREASON': 'EDITREASON',
    'EDITYYMM': 'EDITYYMM',
    'TFID': 'TFID',
    'region': 'region',
    'APT_CHK': 'APT_CHK',
    'Shape_Leng': 'Shape_Leng',
    'Shape_Area': 'Shape_Area',
});
lyr_temp_0.set('fieldImages', {
    'idx': 'Range',
    'RX': 'Range',
    'RY': 'Range',
    'TX': 'TextEdit',
    'TY': 'TextEdit',
    'TZ': 'Range',
    'azimuth': 'Range',
    'tilts': 'Range',
    'chai1': 'TextEdit',
    'chai2': 'TextEdit',
    'dist': 'TextEdit',
    'predict': 'TextEdit',
    'pre2': 'TextEdit',
    'wb1': 'TextEdit',
    'wb2': 'TextEdit',
    'wb3': 'TextEdit',
    'hj1': 'TextEdit',
    'hj2': 'TextEdit',
});
lyr_Gangnam_1m_1.set('fieldImages', {
    'AGL': '',
    'AMSL': '',
    'PRIORITY': '',
    'CLUTTER': '',
    'IDENTICAL': '',
    'UNIQUE_ID': '',
    'EDITREASON': '',
    'EDITYYMM': '',
    'TFID': '',
    'region': '',
    'APT_CHK': '',
    'Shape_Leng': '',
    'Shape_Area': '',
});
lyr_temp_0.set('fieldLabels', {
    'idx': 'no label',
    'RX': 'no label',
    'RY': 'no label',
    'TX': 'no label',
    'TY': 'no label',
    'TZ': 'no label',
    'azimuth': 'no label',
    'tilts': 'no label',
    'chai1': 'no label',
    'chai2': 'no label',
    'dist': 'no label',
    'predict': 'no label',
    'pre2': 'no label',
    'wb1': 'no label',
    'wb2': 'no label',
    'wb3': 'no label',
    'hj1': 'no label',
    'hj2': 'no label',
});
lyr_Gangnam_1m_1.set('fieldLabels', {
    'AGL': 'no label',
    'AMSL': 'no label',
    'PRIORITY': 'no label',
    'CLUTTER': 'no label',
    'IDENTICAL': 'no label',
    'UNIQUE_ID': 'no label',
    'EDITREASON': 'no label',
    'EDITYYMM': 'no label',
    'TFID': 'no label',
    'region': 'no label',
    'APT_CHK': 'no label',
    'Shape_Leng': 'no label',
    'Shape_Area': 'no label',
});
lyr_Gangnam_1m_1.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});
