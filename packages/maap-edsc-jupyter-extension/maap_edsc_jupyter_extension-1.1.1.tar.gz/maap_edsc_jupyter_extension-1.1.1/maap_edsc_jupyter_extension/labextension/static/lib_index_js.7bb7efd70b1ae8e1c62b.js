"use strict";
(self["webpackChunkmaap_edsc_jupyter_extension"] = self["webpackChunkmaap_edsc_jupyter_extension"] || []).push([["lib_index_js"],{

/***/ "./node_modules/css-loader/dist/cjs.js!./style/index.css":
/*!***************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./style/index.css ***!
  \***************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/sourceMaps.js */ "./node_modules/css-loader/dist/runtime/sourceMaps.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
// Imports


var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0___default()));
// Module
___CSS_LOADER_EXPORT___.push([module.id, `div.iframe-widget {
    height:100%;
    width:100%;
}

div.iframe-widget iframe{
    height:100%;
    width:100%;
}
.btn{
    border: none;
    box-sizing: border-box;
    outline: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    margin: 4px;
    padding: 5px 7px;
    /*border-radius: 0;*/
}

.btn:hover {
    background-color: #eeeeee;
}`, "",{"version":3,"sources":["webpack://./style/index.css"],"names":[],"mappings":"AAAA;IACI,WAAW;IACX,UAAU;AACd;;AAEA;IACI,WAAW;IACX,UAAU;AACd;AACA;IACI,YAAY;IACZ,sBAAsB;IACtB,aAAa;IACb,wBAAwB;IACxB,qBAAqB;IACrB,WAAW;IACX,gBAAgB;IAChB,oBAAoB;AACxB;;AAEA;IACI,yBAAyB;AAC7B","sourcesContent":["div.iframe-widget {\n    height:100%;\n    width:100%;\n}\n\ndiv.iframe-widget iframe{\n    height:100%;\n    width:100%;\n}\n.btn{\n    border: none;\n    box-sizing: border-box;\n    outline: none;\n    -webkit-appearance: none;\n    -moz-appearance: none;\n    margin: 4px;\n    padding: 5px 7px;\n    /*border-radius: 0;*/\n}\n\n.btn:hover {\n    background-color: #eeeeee;\n}"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "./lib/buildCmrQuery.js":
/*!******************************!*\
  !*** ./lib/buildCmrQuery.js ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   buildCmrQuery: () => (/* binding */ buildCmrQuery),
/* harmony export */   buildParams: () => (/* binding */ buildParams),
/* harmony export */   pick: () => (/* binding */ pick),
/* harmony export */   prepKeysForCmr: () => (/* binding */ prepKeysForCmr)
/* harmony export */ });
/* harmony import */ var qs__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! qs */ "webpack/sharing/consume/default/qs/qs");
/* harmony import */ var qs__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(qs__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _globals__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./globals */ "./lib/globals.js");
/* harmony import */ var _globals__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_globals__WEBPACK_IMPORTED_MODULE_1__);


//import globals from "./globals";
const buildCmrQuery = (urlParams, nonIndexedKeys, permittedCmrKeys, granule = true) => {
    return buildParams({
        body: camelCaseKeysToUnderscore(urlParams),
        nonIndexedKeys,
        permittedCmrKeys,
        granule
    });
};
/**
 * Apapted from source: https://github.com/nasa/earthdata-search/blob/f09ff3bfd40420322f005654bc349374aab1fe57/serverless/src/util/cmr/buildParams.js
 * Builds a URL used to perform a search request
 * @param {object} paramObj Parameters needed to build a search request URL
 */
const buildParams = (paramObj) => {
    const { body, nonIndexedKeys, permittedCmrKeys, granule, stringifyResult = true } = paramObj;
    let obj = pick(body, permittedCmrKeys);
    if (!obj.concept_id || obj.concept_id.length == 0) {
        obj = null;
    }
    granule ? _globals__WEBPACK_IMPORTED_MODULE_1__.granuleParams = obj : _globals__WEBPACK_IMPORTED_MODULE_1__.collectionParams = obj;
    // For JSON requests we want dont want to stringify the params returned
    if (stringifyResult) {
        // Transform the query string hash to an encoded url string
        const queryParams = prepKeysForCmr(obj, nonIndexedKeys);
        return queryParams;
    }
    return obj;
};
/**
 * Adapted from source https://github.com/nasa/earthdata-search/blob/f09ff3bfd40420322f005654bc349374aab1fe57/serverless/src/util/pick.js
 * Select only desired keys from a provided object.
 * @param {object} providedObj - An object containing any keys.
 * @param {array} keys - An array of strings that represent the keys to be picked.
 * @return {obj} An object containing only the desired keys.
 */
const pick = (providedObj = {}, keys) => {
    let obj = null;
    // if `null` is provided the default parameter will not be
    // set so we'll handle it manually
    if (providedObj == null) {
        obj = {};
    }
    else {
        obj = providedObj;
    }
    let filteredObj = {};
    keys.forEach((key) => {
        let val;
        if (key === 'exclude') {
            val = getObject(obj, "excluded_granule_ids");
        }
        else {
            val = getObject(obj, key);
        }
        if (val) {
            filteredObj[key] = val;
        }
    });
    return filteredObj;
};
/*
* Adapted from
* https://stackoverflow.com/questions/15523514/find-by-key-deep-in-a-nested-array
* */
function getObject(theObject, key) {
    var result = null;
    if (theObject instanceof Array) {
        for (var i = 0; i < theObject.length; i++) {
            result = getObject(theObject[i], key);
            if (result) {
                break;
            }
        }
    }
    else {
        for (var prop in theObject) {
            if (prop == key) {
                if (theObject[prop]) {
                    return theObject[prop];
                }
            }
            if (theObject[prop] instanceof Object || theObject[prop] instanceof Array) {
                result = getObject(theObject[prop], key);
                if (result) {
                    break;
                }
            }
        }
    }
    return result;
}
/**
 * Adapted from source https://github.com/nasa/earthdata-search/blob/f09ff3bfd40420322f005654bc349374aab1fe57/sharedUtils/prepKeysForCmr.js
 * Create a query string containing both indexed and non-indexed keys.
 * @param {object} queryParams - An object containing all queryParams.
 * @param {array} nonIndexedKeys - An array of strings that represent the keys which should not be indexed.
 * @return {string} A query string containing both indexed and non-indexed keys.
 */
const prepKeysForCmr = (queryParams, nonIndexedKeys = []) => {
    const nonIndexedAttrs = {};
    const indexedAttrs = { ...queryParams };
    nonIndexedKeys.forEach((key) => {
        nonIndexedAttrs[key] = indexedAttrs[key];
        delete indexedAttrs[key];
    });
    // problem where returned statement has boundingBox[0]="" which is a syntax error. 
    // This checks if a value is an object and contains 0 as a key which likely means it is indexed
    // Set to the first value by default, because I cannot find an instance where we need it passed as a list
    // nor do we currently support that for the searchCollection/ searchGranule functions
    // This still needs some testing, but seems like the best way to do this right now
    Object.keys(indexedAttrs).forEach(key => {
        if (typeof indexedAttrs[key] === 'object' && Object.keys(indexedAttrs[key]).includes('0')) {
            indexedAttrs[key] = indexedAttrs[key][0];
        }
    });
    return [
        (0,qs__WEBPACK_IMPORTED_MODULE_0__.stringify)(indexedAttrs),
        (0,qs__WEBPACK_IMPORTED_MODULE_0__.stringify)(nonIndexedAttrs, { indices: false, arrayFormat: 'brackets' })
    ].filter(Boolean).join('&');
};
/*
* Source: https://stackoverflow.com/questions/30970286/convert-javascript-object-camelcase-keys-to-underscore-case
* */
function camelCaseKeysToUnderscore(obj) {
    if (typeof (obj) != "object")
        return obj;
    for (let oldName in obj) {
        // Camel to underscore
        let newName = oldName.replace(/([A-Z])/g, function ($1) { return "_" + $1.toLowerCase(); });
        // Only process if names are different
        if (newName != oldName) {
            // Check for the old property name to avoid a ReferenceError in strict mode.
            if (obj.hasOwnProperty(oldName)) {
                obj[newName] = obj[oldName];
                delete obj[oldName];
            }
        }
        // Recursion
        if (typeof (obj[newName]) == "object") {
            obj[newName] = camelCaseKeysToUnderscore(obj[newName]);
        }
    }
    return obj;
}


/***/ }),

/***/ "./lib/encodersDecoders.js":
/*!*********************************!*\
  !*** ./lib/encodersDecoders.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   decodeAdvancedSearch: () => (/* binding */ decodeAdvancedSearch),
/* harmony export */   decodeAutocomplete: () => (/* binding */ decodeAutocomplete),
/* harmony export */   decodeCollections: () => (/* binding */ decodeCollections),
/* harmony export */   decodeFacets: () => (/* binding */ decodeFacets),
/* harmony export */   decodeFeatures: () => (/* binding */ decodeFeatures),
/* harmony export */   decodeGranuleFilters: () => (/* binding */ decodeGranuleFilters),
/* harmony export */   decodeGridCoords: () => (/* binding */ decodeGridCoords),
/* harmony export */   decodeHasGranulesOrCwic: () => (/* binding */ decodeHasGranulesOrCwic),
/* harmony export */   decodeMap: () => (/* binding */ decodeMap),
/* harmony export */   decodeScienceKeywords: () => (/* binding */ decodeScienceKeywords),
/* harmony export */   decodeString: () => (/* binding */ decodeString),
/* harmony export */   decodeTemporal: () => (/* binding */ decodeTemporal),
/* harmony export */   decodeTimeline: () => (/* binding */ decodeTimeline),
/* harmony export */   encodeAdvancedSearch: () => (/* binding */ encodeAdvancedSearch),
/* harmony export */   encodeAutocomplete: () => (/* binding */ encodeAutocomplete),
/* harmony export */   encodeCollections: () => (/* binding */ encodeCollections),
/* harmony export */   encodeFacets: () => (/* binding */ encodeFacets),
/* harmony export */   encodeFeatures: () => (/* binding */ encodeFeatures),
/* harmony export */   encodeGranuleFilters: () => (/* binding */ encodeGranuleFilters),
/* harmony export */   encodeGridCoords: () => (/* binding */ encodeGridCoords),
/* harmony export */   encodeHasGranulesOrCwic: () => (/* binding */ encodeHasGranulesOrCwic),
/* harmony export */   encodeMap: () => (/* binding */ encodeMap),
/* harmony export */   encodeScienceKeywords: () => (/* binding */ encodeScienceKeywords),
/* harmony export */   encodeString: () => (/* binding */ encodeString),
/* harmony export */   encodeTemporal: () => (/* binding */ encodeTemporal),
/* harmony export */   encodeTimeline: () => (/* binding */ encodeTimeline),
/* harmony export */   isNumber: () => (/* binding */ isNumber),
/* harmony export */   timelineIntervals: () => (/* binding */ timelineIntervals)
/* harmony export */ });
/* harmony import */ var lodash__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! lodash */ "./node_modules/lodash/lodash.js");
/* harmony import */ var lodash__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(lodash__WEBPACK_IMPORTED_MODULE_0__);
/**
 *
 * All encoders and decoders copied from earthdata search source code.
 * They can all be found in this directory: https://github.com/nasa/earthdata-search/tree/master/static/src/js/util/url
 *
 * June 30, 2020 - https://github.com/nasa/earthdata-search/releases/tag/v1.123.14
 *
 * */
/**
 * Decodes a string parameter (returns the same value)
 * @param {string} string
 */
const decodeString = string => string;
/**
 * Encodes a string parameter (returns the same value)
 * @param {string} string
 */
const encodeString = string => string || '';
/**
 * Encodes a Feature Facet object into a string
 * @param {object} features Feature Facet object
 * @return {string} A `!` delimited string of the Feature Facet values
 */
const encodeFeatures = (features) => {
    if (!features)
        return '';
    const { customizable, mapImagery, nearRealTime } = features;
    const encoded = [];
    if (mapImagery)
        encoded.push('Map Imagery');
    if (nearRealTime)
        encoded.push('Near Real Time');
    if (customizable)
        encoded.push('Customizable');
    const encodedString = encoded.join('!');
    if (encodedString === '')
        return '';
    return encodedString;
};
/**
 * Decodes a Feature Facet parameter string into an object
 * @param {string} string A `!` delimited string of the Feature Facet values
 * @return {object} Feature Facet object
 */
const decodeFeatures = (string) => {
    const defaultFeatures = {
        mapImagery: false,
        nearRealTime: false,
        customizable: false
    };
    if (!string) {
        return defaultFeatures;
    }
    const decodedValues = string.split('!');
    const decodedFeatures = {
        mapImagery: decodedValues.indexOf('Map Imagery') !== -1,
        nearRealTime: decodedValues.indexOf('Near Real Time') !== -1,
        customizable: decodedValues.indexOf('Customizable') !== -1
    };
    return {
        ...decodedFeatures
    };
};
/**
 * Encodes a Facet object into a string
 * @param {object} facets Facet object
 * @return {string} A `!` delimited string of the facet values
 */
const encodeFacets = (facets) => {
    if (!facets)
        return '';
    const encoded = [];
    facets.forEach((facet) => {
        encoded.push(facet);
    });
    return encoded.join('!');
};
/**
 * Decodes a Facet parameter string into an object
 * @param {string} string A `!` delimited string of the facet values
 * @return {object} Facet object
 */
const decodeFacets = (string) => {
    if (!string) {
        return undefined;
    }
    const decodedValues = string.split('!');
    return decodedValues;
};
const projections = {
    arctic: 'epsg3413',
    geographic: 'epsg4326',
    antarctic: 'epsg3031'
};
const projectionList = [
    projections.arctic,
    projections.geographic,
    projections.antarctic
];
/**
 * Encodes a Map object into a string
 * @param {object} query Map object with query and state
 * @return {string} A `!` delimited string of the map values
 */
const encodeMap = (map) => {
    if (!map)
        return '';
    const { base, latitude, longitude, overlays, projection, zoom } = map;
    const encodedProjection = projectionList.indexOf(projection);
    let encodedBase;
    if (base.blueMarble)
        encodedBase = 0;
    if (base.trueColor)
        encodedBase = 1;
    if (base.landWaterMap)
        encodedBase = 2;
    const encodedOverlays = [];
    if (overlays.referenceFeatures)
        encodedOverlays.push(0);
    if (overlays.coastlines)
        encodedOverlays.push(1);
    if (overlays.referenceLabels)
        encodedOverlays.push(2);
    const encodedString = [
        latitude,
        longitude,
        zoom,
        encodedProjection,
        encodedBase,
        encodedOverlays.join(',')
    ].join('!');
    if (encodedString === '0!0!2!1!0!0,2')
        return '';
    return encodedString;
};
/**
 * Decodes a map parameter string into an object
 * @param {string} string A `!` delimited string of the map values
 * @return {object} Map object with query and state
 */
const decodeMap = (string) => {
    if (!string) {
        return {};
    }
    const [latitude, longitude, zoom, projection, base, overlays] = string.split('!');
    const decodedLatitude = parseFloat(latitude);
    const decodedLongitude = parseFloat(longitude);
    const decodedZoom = parseFloat(zoom);
    const decodedProjection = projectionList[projection];
    const decodedBase = {
        blueMarble: base === '0',
        trueColor: base === '1',
        landWaterMap: base === '2'
    };
    const decodedOverlays = {
        referenceFeatures: overlays.split(',').indexOf('0') !== -1,
        coastlines: overlays.split(',').indexOf('1') !== -1,
        referenceLabels: overlays.split(',').indexOf('2') !== -1
    };
    const map = {
        base: decodedBase,
        latitude: decodedLatitude,
        longitude: decodedLongitude,
        overlays: decodedOverlays,
        projection: decodedProjection,
        zoom: decodedZoom
    };
    return {
        ...map
    };
};
/**
 * Lookup a object key given a value
 * @param {string} object JavaScript Object with key-value pairs
 * @param {string} value A value in the object
 * @return {string} A key in the object
 */
const getObjectKeyByValue = (object, value) => Object.keys(object)
    .find(key => object[key] === value);
/**
 * Mapping of Science Keyword keys to encoded values
 */
const scienceKeywordMapping = {
    topic: 'fst',
    term: 'fsm',
    variable_level_1: 'fs1',
    variable_level_2: 'fs2',
    variable_level_3: 'fs3',
    detailed_variable: 'fsd'
};
/**
 * Encodes a Science Keyword Facet object into a flat object with encoded keys
 * @param {object} scienceKeywords Science Keyword Facet object
 * @return {object} A flat object with encoded Science Keyword keys
 */
const encodeScienceKeywords = (scienceKeywords) => {
    if (!scienceKeywords)
        return '';
    if (Object.keys(scienceKeywords).length === 0)
        return '';
    const encoded = {};
    scienceKeywords.forEach((keyword, index) => {
        Object.keys(keyword).forEach((key) => {
            encoded[`${scienceKeywordMapping[key]}${index}`] = keyword[key];
        });
    });
    return encoded;
};
/**
 * Decodes a parameter object into a Science Keyword object
 * @param {object} params URL parameter object from parsing the URL parameter string
 * @return {object} Science Keyword Facet object
 */
const decodeScienceKeywords = (params) => {
    if (Object.keys(params).length === 0)
        return undefined;
    const decoded = [];
    Object.keys(params).forEach((encodedKey) => {
        // All of the science keyword facets have an index as the last character of the key
        // Strip off the last character and check the mapping if it exists
        const key = encodedKey.slice(0, -1);
        const index = encodedKey.slice(-1);
        const decodedKey = getObjectKeyByValue(scienceKeywordMapping, key);
        if (decodedKey) {
            // Update the decoded index with value
            if (decoded[index] === undefined)
                decoded[index] = {};
            decoded[index][decodedKey] = params[encodedKey];
        }
    });
    if (decoded.length > 0)
        return decoded;
    return undefined;
};
/**
 * Encodes a Temporal object into a string
 * @param {object} temporal Temporal object
 * @return {string} A `,` delimited string of the temporal values
 */
const encodeTemporal = (temporal) => {
    if (!temporal)
        return undefined;
    const { endDate, startDate, recurringDayStart, recurringDayEnd, isRecurring } = temporal;
    const valuesToEncode = [
        startDate,
        endDate
    ];
    if (isRecurring) {
        valuesToEncode.push(...[recurringDayStart, recurringDayEnd]);
    }
    const encodedString = valuesToEncode.filter(Boolean).join(',');
    // TODO: Strip empty elements then join
    if (encodedString === '')
        return undefined;
    return encodedString;
};
/**
 * Mapping of timeline zoom levels. The Timeline (sometimes) and URL use numbers, CMR uses words
 */
const timelineIntervals = {
    minute: '2',
    hour: '3',
    day: '4',
    month: '5',
    year: '6'
};
/**
 * Decodes a Temporal parameter string into an object
 * @param {string} string A `,` delimited string of the temporal values
 * @return {object} Temporal object
 */
const decodeTemporal = (string) => {
    if (!string) {
        return {};
    }
    const [startDate, endDate, recurringDayStart = '', recurringDayEnd = ''] = string.split(',');
    const isRecurring = !!(recurringDayStart && recurringDayEnd);
    const temporal = {
        endDate,
        startDate,
        recurringDayStart,
        recurringDayEnd,
        isRecurring
    };
    return {
        ...temporal
    };
};
/**
 * Encodes a Timeline object into an encoded object
 * @param {object} timelineQuery Timeline query object
 * @param {string} pathname Pathname string from react-router
 * @return {string} A `!` delimited string of the timeline values
 */
const encodeTimeline = (timelineQuery, pathname) => {
    if (pathname === '/search')
        return '';
    if (!timelineQuery)
        return '';
    const { center, interval, start, end } = timelineQuery;
    if (!center && !start && !end)
        return '';
    const encodedStart = start || '';
    const encodedEnd = end || '';
    const encodedString = [center, timelineIntervals[interval], encodedStart, encodedEnd].join('!');
    // if there is no center, return an empty string
    if (encodedString[0] === '!')
        return '';
    return {
        tl: encodedString
    };
};
/**
 * Decodes a parameter object into a Timeline object
 * @param {object} params URL parameter object from parsing the URL parameter string
 * @return {object} Timeline object with query and state
 */
const decodeTimeline = (params) => {
    const { tl: timeline } = params;
    if (!timeline)
        return undefined;
    const [center, intervalNum, start, end] = timeline.split('!');
    const interval = getObjectKeyByValue(timelineIntervals, intervalNum);
    const query = {
        center: parseInt(center, 10) || undefined,
        end: parseInt(end, 10) || undefined,
        interval,
        start: parseInt(start, 10) || undefined
    };
    return query;
};
/**
 * Encode a list of Granule IDs
 * @param {boolean} isCwic Are the granules CWIC
 * @param {array} granuleIds List of granule IDs
 */
const encodeGranules = (isCwic, granuleIds) => {
    // On page log, isCwic hasn't been determined yet
    // temporary fix, if the granule doesn't start with G, it is CWIC
    const [firstGranuleId] = granuleIds;
    if (isCwic || isNumber(firstGranuleId)) {
        return granuleIds.join('!');
    }
    // CMR Granule Ids
    // G12345-PROVIDER
    const provider = granuleIds[0].split('-')[1];
    const formattedGranuleIds = granuleIds.map(granuleId => granuleId.split('G')[1].split('-')[0]);
    return `${formattedGranuleIds.join('!')}!${provider}`;
};
/**
 * Decode a string of Granule IDs
 * @param {string} excludedGranules Encoded Granule IDs
 */
const decodedGranules = (key, granules) => {
    const keys = Object.keys(granules);
    let result = {
        isCwic: false,
        granuleIds: []
    };
    if (keys.indexOf(key) !== -1) {
        const { [key]: decodedGranules } = granules;
        const granulesList = decodedGranules.split('!');
        const provider = granulesList.pop();
        const granuleIds = granulesList.map(granuleId => `G${granuleId}-${provider}`);
        result = {
            isCwic: false,
            granuleIds
        };
    }
    if (keys.indexOf(`c${key}`) !== -1) {
        const { [`c${key}`]: decodedGranules } = granules;
        const granuleIds = decodedGranules.split('!');
        result = {
            isCwic: true,
            granuleIds
        };
    }
    return result;
};
const encodeSelectedVariables = (projectCollection) => {
    if (!projectCollection)
        return null;
    const { accessMethods, selectedAccessMethod } = projectCollection;
    if (!accessMethods || !selectedAccessMethod)
        return null;
    const selectedMethod = accessMethods[selectedAccessMethod];
    const { selectedVariables } = selectedMethod;
    if (!selectedVariables)
        return null;
    return selectedVariables.join('!');
};
const encodeOutputFormat = (projectCollection) => {
    if (!projectCollection)
        return null;
    const { accessMethods, selectedAccessMethod } = projectCollection;
    if (!accessMethods || !selectedAccessMethod)
        return null;
    const selectedMethod = accessMethods[selectedAccessMethod];
    const { selectedOutputFormat } = selectedMethod;
    if (!selectedOutputFormat)
        return null;
    return selectedOutputFormat;
};
const encodeAddedGranules = (isCwic, projectCollection) => {
    if (!projectCollection)
        return null;
    const { addedGranuleIds = [] } = projectCollection;
    if (!addedGranuleIds.length)
        return null;
    return encodeGranules(isCwic, addedGranuleIds);
};
const encodeRemovedGranules = (isCwic, projectCollection) => {
    if (!projectCollection)
        return null;
    const { removedGranuleIds = [] } = projectCollection;
    if (!removedGranuleIds.length)
        return null;
    return encodeGranules(isCwic, removedGranuleIds);
};
const decodedSelectedVariables = (pgParam) => {
    const { uv: variableIds } = pgParam;
    if (!variableIds)
        return undefined;
    return variableIds.split('!');
};
const decodedOutputFormat = (pgParam) => {
    const { of: outputFormat } = pgParam;
    return outputFormat;
};
/**
 * Encodes a Collections object into an object
 * @param {object} collections Collections object
 * @param {string} focusedCollection Focused Collection ID
 * @return {string} An object with encoded Collections
 */
const encodeCollections = (props) => {
    const { collections = {}, focusedCollection, project = {} } = props;
    const { byId } = collections;
    const { byId: projectById = {}, collectionIds: projectIds = [] } = project;
    // pParameter - focusedCollection!projectCollection1!projectCollection2
    const pParameter = [
        focusedCollection,
        ...projectIds
    ].join('!');
    // If there isn't a focusedCollection or any projectIds, we don't see to continue
    if (pParameter === '')
        return '';
    // pgParameter - excluded granules and granule filters based on pParameter collections
    const pgParameter = [];
    if (byId) {
        pParameter.split('!').forEach((collectionId, index) => {
            let pg = {};
            // if the focusedCollection is also in projectIds, don't encode the focusedCollection
            if (index === 0 && projectIds.indexOf(focusedCollection) !== -1) {
                pgParameter[index] = pg;
                return;
            }
            const collection = byId[collectionId];
            if (!collection) {
                pgParameter[index] = pg;
                return;
            }
            const projectCollection = projectById[collectionId];
            // excludedGranules
            let encodedExcludedGranules;
            const { excludedGranuleIds = [], granules, granuleFilters, isVisible, isCwic } = collection;
            const excludedKey = isCwic ? 'cx' : 'x';
            if (granules && excludedGranuleIds.length > 0) {
                encodedExcludedGranules = encodeGranules(isCwic, excludedGranuleIds);
            }
            if (encodedExcludedGranules)
                pg[excludedKey] = encodedExcludedGranules;
            let encodedAddedGranules;
            let encodedRemovedGranules;
            const addedKey = isCwic ? 'ca' : 'a';
            const removedKey = isCwic ? 'cr' : 'r';
            // Encode granules added to the current project
            if (projectCollection
                && projectCollection.addedGranuleIds
                && projectCollection.addedGranuleIds.length > 0) {
                encodedAddedGranules = encodeAddedGranules(isCwic, projectCollection);
            }
            // Encode granules removed from the current project
            if (projectCollection
                && projectCollection.removedGranuleIds
                && projectCollection.removedGranuleIds.length > 0) {
                encodedRemovedGranules = encodeRemovedGranules(isCwic, projectCollection);
            }
            if (encodedAddedGranules)
                pg[addedKey] = encodedAddedGranules;
            if (encodedRemovedGranules)
                pg[removedKey] = encodedRemovedGranules;
            // Collection visible, don't encode the focusedCollection
            if (index !== 0 && isVisible)
                pg.v = 't';
            // Add the granule encoded granule filters
            if (granuleFilters) {
                pg = { ...pg, ...encodeGranuleFilters(granuleFilters) };
            }
            // Encode selected variables
            pg.uv = encodeSelectedVariables(projectCollection);
            // Encode selected output format
            pg.of = encodeOutputFormat(projectCollection);
            pgParameter[index] = pg;
        });
    }
    const encoded = {
        p: pParameter,
        pg: pgParameter
    };
    return encoded;
};
/**
 * Decodes a parameter object into a Collections object
 * @param {object} params URL parameter object from parsing the URL parameter string
 * @return {object} Collections object
 */
const decodeCollections = (params) => {
    if (Object.keys(params).length === 0)
        return {};
    const { p, pg } = params;
    if (!p && !pg)
        return {};
    let focusedCollection = '';
    let collections;
    let project;
    const allIds = [];
    const byId = {};
    const projectIds = [];
    const projectById = {};
    p.split('!').forEach((collectionId, index) => {
        // If there is no collectionId, move on to the next index
        // i.e. there is no focusedCollection
        if (collectionId === '')
            return;
        // Add collectionId to correct allIds and projectIds
        if (allIds.indexOf(collectionId) === -1)
            allIds.push(collectionId);
        if (index > 0)
            projectIds.push(collectionId);
        // Set the focusedCollection
        if (index === 0)
            focusedCollection = collectionId;
        let excludedGranuleIds = [];
        let addedGranuleIds = [];
        let removedGranuleIds = [];
        let granuleFilters = {};
        let selectedOutputFormat;
        let isCwic;
        let excludedIsCwic;
        let addedIsCwic;
        let removedIsCwic;
        let isVisible = false;
        let variableIds;
        if (pg && pg[index]) {
            // Excluded Granules
            //graceal2 this is where I would make the change to alter the logic of excluded granules
            ({ isCwic: excludedIsCwic, granuleIds: excludedGranuleIds } = decodedGranules('x', pg[index]));
            ({ isCwic: addedIsCwic, granuleIds: addedGranuleIds = [] } = decodedGranules('a', pg[index]));
            ({ isCwic: removedIsCwic, granuleIds: removedGranuleIds = [] } = decodedGranules('r', pg[index]));
            isCwic = excludedIsCwic || addedIsCwic || removedIsCwic;
            // Collection visible
            const { v: visible = '' } = pg[index];
            if (visible === 't')
                isVisible = true;
            // Decode selected variables
            variableIds = decodedSelectedVariables(pg[index]);
            // Decode granule filters
            granuleFilters = decodeGranuleFilters(pg[index]);
            // Decode output format
            selectedOutputFormat = decodedOutputFormat(pg[index]);
        }
        // Populate the collection object for the redux store
        byId[collectionId] = {
            excludedGranuleIds,
            granules: {},
            granuleFilters,
            isCwic,
            isVisible,
            metadata: {}
        };
        if (index > 0) {
            projectById[collectionId] = {};
        }
        if (variableIds || selectedOutputFormat) {
            projectById[collectionId] = {
                accessMethods: {
                    opendap: {
                        selectedVariables: variableIds,
                        selectedOutputFormat
                    }
                }
            };
        }
        if (addedGranuleIds.length && projectById[collectionId]) {
            projectById[collectionId].addedGranuleIds = addedGranuleIds;
        }
        if (removedGranuleIds.length && projectById[collectionId]) {
            projectById[collectionId].removedGranuleIds = removedGranuleIds;
        }
    });
    // if no decoded collections information exists, return undfined for collections
    if (pg || projectIds.length > 0) {
        collections = {
            allIds,
            byId
        };
        project = {
            byId: projectById,
            collectionIds: projectIds
        };
    }
    return {
        collections,
        focusedCollection,
        project
    };
};
/**
 * Encodes a granule filters object into an object.
 * @param {Object} granuleFilters - The granule filters object.
 * @return {String} An object with encoded granule filters.
 */
const encodeGranuleFilters = (granuleFilters) => {
    const pg = {};
    if (granuleFilters.temporal)
        pg.qt = encodeTemporal(granuleFilters.temporal);
    if (granuleFilters.dayNightFlag)
        pg.dnf = granuleFilters.dayNightFlag;
    if (granuleFilters.browseOnly)
        pg.bo = granuleFilters.browseOnly;
    if (granuleFilters.onlineOnly)
        pg.oo = granuleFilters.onlineOnly;
    if (granuleFilters.cloudCover)
        pg.cc = granuleFilters.cloudCover;
    if (granuleFilters.orbitNumber)
        pg.on = granuleFilters.orbitNumber;
    if (granuleFilters.equatorCrossingLongitude)
        pg.ecl = granuleFilters.equatorCrossingLongitude;
    if (granuleFilters.readableGranuleName)
        pg.id = granuleFilters.readableGranuleName.join('!');
    if (granuleFilters.equatorCrossingDate) {
        pg.ecd = encodeTemporal(granuleFilters.equatorCrossingDate);
    }
    if (granuleFilters.sortKey)
        pg.gsk = granuleFilters.sortKey;
    return pg;
};
/**
 * Decodes part of the decoded ?pg url parameter into a granule filters object
 * @param {Object} params - URL parameter object from parsing the URL parameter string
 * @return {Object} A granule filters object
 */
const decodeGranuleFilters = (params = {}) => {
    const granuleFilters = {};
    if (params.qt)
        granuleFilters.temporal = decodeTemporal(params.qt);
    if (params.dnf)
        granuleFilters.dayNightFlag = params.dnf;
    if (params.bo)
        granuleFilters.browseOnly = params.bo === 'true';
    if (params.oo)
        granuleFilters.onlineOnly = params.oo === 'true';
    if (params.cc)
        granuleFilters.cloudCover = params.cc;
    if (params.on)
        granuleFilters.orbitNumber = params.on;
    if (params.ecl)
        granuleFilters.equatorCrossingLongitude = params.ecl;
    if (params.id)
        granuleFilters.readableGranuleName = params.id.split('!');
    if (params.ecd)
        granuleFilters.equatorCrossingDate = decodeTemporal(params.ecd);
    if (params.gsk)
        granuleFilters.sortKey = params.gsk;
    return granuleFilters;
};
/**
 * Returns true the string contains only number characters and false if there are any non-number characters
 * @return {boolean}
 */
const reg = new RegExp(/^\d+$/);
const isNumber = string => reg.test(string);
const encodeGridCoords = (gridCoords) => {
    if (!gridCoords)
        return '';
    const encodedCoords = gridCoords
        .trim()
        .replace(/,/g, ':')
        .replace(/\s+/g, ',')
        .replace(/(^|,)(\d+)($|:)/g, '$1$2-$2$3')
        .replace(/(^|:)(\d+)($|,)/g, '$1$2-$2$3');
    return encodedCoords;
};
const decodeGridCoords = (string) => {
    if (!string)
        return undefined;
    const decodedString = string
        .replace(/,/g, ' ')
        .replace(/:/g, ',')
        .replace(/(\d+)-(\d+)/g, (m, m0, m1) => {
        if (m0 === m1)
            return m0;
        return m;
    });
    return decodedString;
};
/**
 * Encodes hasGranulesOrCwic
 * @param {object} hasGranulesOrCwic hasGranulesOrCwic value from redux store
 * @return {string} Encoded value for hasGranulesOrCwic
 */
const encodeHasGranulesOrCwic = (hasGranulesOrCwic) => {
    // When we have undefined in the store, the encoded value is true (ac=true)
    if (!hasGranulesOrCwic)
        return true;
    // When we have true in the store, we don't encode the value
    return '';
};
/**
 * Decodes hasGranulesOrCwic
 * @param {string} value Encoded value for hasGranulesOrCwic
 * @return {object} Decoded hasGranulesOrCwic value
 */
const decodeHasGranulesOrCwic = (value) => {
    // When we see true in the url, we do not store hasGranulesOrCwic in the store
    if (value === 'true')
        return undefined;
    // If we do not see the ac param in the store, we save hasGranulesOrCwic=true in the store
    return true;
};
/**
 * Encodes the Advanced Search params into an object
 * @param {Object} advancedSearch advancedSearch object from the store
 */
const encodeAdvancedSearch = (advancedSearch) => {
    if (!advancedSearch)
        return '';
    const { regionSearch } = advancedSearch;
    if (!regionSearch)
        return '';
    const { selectedRegion } = regionSearch;
    if (!selectedRegion)
        return '';
    return {
        sr: {
            ...selectedRegion
        }
    };
};
/**
 * Decodes a parameter object into an advancedSearch object
 * @param {Object} params URL parameter object from parsing the URL parameter string
 */
const decodeAdvancedSearch = (params) => {
    if (Object.keys(params).length === 0)
        return undefined;
    const { sr } = params;
    if (!sr)
        return undefined;
    const advancedSearch = {
        regionSearch: {
            selectedRegion: {
                ...sr
            }
        }
    };
    return advancedSearch;
};

/**
 * Encodes the Autocomplete Selected params into an object
 * @param {Object} selected autocomplete selected object from the store
 */
const encodeAutocomplete = (selected) => {
    if (!selected || selected.length === 0)
        return '';
    const param = {};
    selected.forEach(({ type, fields }) => {
        if (Object.keys(param).includes(type)) {
            param[type].push(fields);
        }
        else {
            param[type] = [fields];
        }
    });
    return param;
};
/**
 * Decodes a parameter object into an Autocomplete Selected array
 * @param {Object} params URL parameter object from parsing the URL parameter string
 */
const decodeAutocomplete = (params) => {
    if (!params || (0,lodash__WEBPACK_IMPORTED_MODULE_0__.isEmpty)(params))
        return undefined;
    const values = [];
    Object.keys(params).forEach((key) => {
        const items = params[key];
        Object.keys(items).forEach((index) => {
            // Pull out the colon delimited value
            const fields = items[index];
            // Split the fields and pop the last element (which represents the leaf node)
            const value = fields.split(':').slice(-1);
            // slice returns an array, select the element
            const [selectedValue] = value;
            values.push({ type: key, fields: items[index], value: selectedValue });
        });
    });
    return values;
};


/***/ }),

/***/ "./lib/globals.js":
/*!************************!*\
  !*** ./lib/globals.js ***!
  \************************/
/***/ (() => {


var limit = "100";
var params = {};
var granuleParams;
var collectionParams;
var granuleQuery;
var collectionQuery;
var edscUrl;


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/docmanager */ "webpack/sharing/consume/default/@jupyterlab/docmanager");
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/mainmenu */ "webpack/sharing/consume/default/@jupyterlab/mainmenu");
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var jquery__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! jquery */ "webpack/sharing/consume/default/jquery/jquery");
/* harmony import */ var jquery__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(jquery__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _urlParser__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ./urlParser */ "./lib/urlParser.js");
/* harmony import */ var _style_index_css__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ../style/index.css */ "./style/index.css");
/* harmony import */ var _widgets__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! ./widgets */ "./lib/widgets.js");
/* harmony import */ var _popups__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! ./popups */ "./lib/popups.js");
/* harmony import */ var _globals__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./globals */ "./lib/globals.js");
/* harmony import */ var _globals__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(_globals__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var _request__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./request */ "./lib/request.js");
/* harmony import */ var _buildCmrQuery__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! ./buildCmrQuery */ "./lib/buildCmrQuery.js");
/* harmony import */ var _searchKeys__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! ./searchKeys */ "./lib/searchKeys.js");
/// <reference path="./widgets.ts" />
/** jupyterlab imp: {}orts **/







/** phosphor imports **/

/** other external imports **/

/** internal imports **/








let edsc_server = '';
var valuesUrl = new URL(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getBaseUrl() + 'jupyter-server-extension/getConfig');
let DEFAULT_RESULTS_LIMIT = 100;
(0,_request__WEBPACK_IMPORTED_MODULE_9__.request)('get', valuesUrl.href).then((res) => {
    if (res.ok) {
        let environment = JSON.parse(res.data);
        edsc_server = 'https://' + environment['edsc_server'];
    }
});
///////////////////////////////////////////////////////////////
//
// Earthdata Search Client extension
//
///////////////////////////////////////////////////////////////
const extension = {
    id: 'edsc_extension',
    autoStart: true,
    requires: [_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__.IDocumentManager, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer, _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_4__.IMainMenu, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_5__.INotebookTracker],
    activate: activate
};
function activate(app, docManager, palette, restorer, mainMenu, tracker, panel) {
    let widget;
    const namespace = 'tracker-iframe';
    let instanceTracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({ namespace });
    //
    // Listen for messages being sent by the iframe - parse the url and set as parameters for search
    //
    window.addEventListener("message", (event) => {
        // if the message sent is the edsc url
        if (typeof event.data === "string") {
            (_globals__WEBPACK_IMPORTED_MODULE_10___default().edscUrl) = event.data;
            const queryString = '?' + event.data.split('?')[1];
            const decodedUrlObj = (0,_urlParser__WEBPACK_IMPORTED_MODULE_11__.decodeUrlParams)(queryString);
            //graceal Note that I switched granuleNonIndexedKeys and granulePermittedCmrKeys because they were switched in 
            // buildCmrQuery definition
            (_globals__WEBPACK_IMPORTED_MODULE_10___default().granuleQuery) = "https://fake.com/?" + (0,_buildCmrQuery__WEBPACK_IMPORTED_MODULE_12__.buildCmrQuery)(decodedUrlObj, _searchKeys__WEBPACK_IMPORTED_MODULE_13__.granuleNonIndexedKeys, _searchKeys__WEBPACK_IMPORTED_MODULE_13__.granulePermittedCmrKeys, true);
            (_globals__WEBPACK_IMPORTED_MODULE_10___default().collectionQuery) = "https://fake.com/?" + (0,_buildCmrQuery__WEBPACK_IMPORTED_MODULE_12__.buildCmrQuery)(decodedUrlObj, _searchKeys__WEBPACK_IMPORTED_MODULE_13__.collectionNonIndexedKeys, _searchKeys__WEBPACK_IMPORTED_MODULE_13__.collectionPermittedCmrKeys, false);
        }
    });
    //
    // Get the current cell selected in a notebook
    //
    function getCurrent(args) {
        const widget = tracker.currentWidget;
        const activate = args['activate'] !== false;
        if (activate && widget) {
            app.shell.activateById(widget.id);
        }
        return widget;
    }
    // PASTE SEARCH INTO A NOTEBOOK
    function pasteSearch(args, result_type, query_type = 'granule') {
        const current = getCurrent(args);
        // If no search is selected, send an error
        if (!(_globals__WEBPACK_IMPORTED_MODULE_10___default().granuleParams) || Object.keys((_globals__WEBPACK_IMPORTED_MODULE_10___default().granuleParams)).length == 0) {
            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Notification.error("Error: No Search Selected. Select collections through the green plus in EarthData Search Client.", { autoClose: 3000 });
            return;
        }
        // Paste Search Query
        if (result_type == "query") {
            var getUrl = new URL(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getBaseUrl() + 'jupyter-server-extension/edsc/getQuery');
            if (query_type === 'granule') {
                getUrl.searchParams.append("cmr_query", (_globals__WEBPACK_IMPORTED_MODULE_10___default().granuleQuery));
                getUrl.searchParams.append("query_type", 'granule');
            }
            else {
                getUrl.searchParams.append("cmr_query", (_globals__WEBPACK_IMPORTED_MODULE_10___default().collectionQuery));
                getUrl.searchParams.append("query_type", 'collection');
            }
            getUrl.searchParams.append("limit", String((_globals__WEBPACK_IMPORTED_MODULE_10___default().limit)));
            // Make call to back end
            var xhr = new XMLHttpRequest();
            let response_text = "";
            xhr.onload = function () {
                if (xhr.status == 200) {
                    let response = jquery__WEBPACK_IMPORTED_MODULE_7__.parseJSON(xhr.response);
                    response_text = response.query_string;
                    if (response_text == "") {
                        response_text = "No results found.";
                    }
                    if (current) {
                        _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_5__.NotebookActions.insertBelow(current.content);
                        _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_5__.NotebookActions.paste(current.content);
                        current.content.mode = 'edit';
                        const insert_text = "# generated from this EDSC search: " + (_globals__WEBPACK_IMPORTED_MODULE_10___default().edscUrl) + "\n" + response_text;
                        if (current.content.activeCell) {
                            current.content.activeCell.model.sharedModel.setSource(insert_text);
                        }
                    }
                }
                else {
                    console.log("Error making call to get query. Status is " + xhr.status);
                    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Notification.error("Error making call to get search query. Have you selected valid search parameters?", { autoClose: 3000 });
                }
            };
            xhr.onerror = function () {
                console.error("Error making call to get query");
            };
            xhr.open("GET", getUrl.href, true);
            xhr.send(null);
            // Paste Search Results
        }
        else {
            var getUrl = new URL(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getBaseUrl() + 'jupyter-server-extension/edsc/getGranules');
            getUrl.searchParams.append("cmr_query", (_globals__WEBPACK_IMPORTED_MODULE_10___default().granuleQuery));
            getUrl.searchParams.append("limit", String((_globals__WEBPACK_IMPORTED_MODULE_10___default().limit)));
            // Make call to back end
            const promise = createXhr(current, getUrl);
            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Notification.promise(promise, {
                pending: { message: 'Getting granule search results', options: { autoClose: 3000 } },
                success: {
                    message: (result, data) => `Pasting granule search results successful`,
                },
                error: {
                    message: (reason, data) => `${reason}`,
                }
            });
        }
    }
    /**
     * Create Xhr and alert if success or failure
     * @param current Current cell in the notebook
     * @param getUrl Url to fetch
     */
    function createXhr(current, getUrl) {
        return new Promise((resolve, reject) => {
            var xhr = new XMLHttpRequest();
            let url_response = [];
            xhr.onload = function () {
                if (xhr.status == 200) {
                    let response = jquery__WEBPACK_IMPORTED_MODULE_7__.parseJSON(xhr.response);
                    let response_text = response.granule_urls;
                    if (response_text == "") {
                        response_text = "No results found.";
                    }
                    url_response = response_text;
                    if (current) {
                        _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_5__.NotebookActions.insertBelow(current.content);
                        _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_5__.NotebookActions.paste(current.content);
                        current.content.mode = 'edit';
                        const insert_text = "# generated from this EDSC search: " + (_globals__WEBPACK_IMPORTED_MODULE_10___default().edscUrl) + "\n" + url_response;
                        if (current.content.activeCell) {
                            current.content.activeCell.model.value.text = insert_text;
                        }
                    }
                    resolve('Success');
                }
                else {
                    console.log("Error making call to get results. Status is " + xhr.status);
                    //Notification.error("Error making call to get search results. Have you selected valid search parameters?", {autoClose: 3000});
                    reject("Error making call to get search results. Have you selected valid search parameters?");
                }
            };
            xhr.onerror = function () {
                console.log("Error making call to get results");
            };
            xhr.open("GET", getUrl.href, true);
            xhr.send(null);
        });
    }
    /******** Set commands for command palette and main menu *********/
    // Add an application command to open ESDC
    const open_command = 'iframe:open';
    app.commands.addCommand(open_command, {
        label: 'Open EarthData Search',
        isEnabled: () => true,
        execute: args => {
            // Only allow user to have one EDSC window
            if (widget == undefined) {
                widget = new _widgets__WEBPACK_IMPORTED_MODULE_14__.IFrameWidget(edsc_server);
                app.shell.add(widget, 'main');
                app.shell.activateById(widget.id);
            }
            else {
                // if user already has EDSC, just switch to tab
                app.shell.add(widget, 'main');
                app.shell.activateById(widget.id);
            }
            if (!instanceTracker.has(widget)) {
                // Track the state of the widget for later restoration
                instanceTracker.add(widget);
            }
        }
    });
    palette.addItem({ command: open_command, category: 'Search' });
    const display_params_command = 'search:displayParams';
    app.commands.addCommand(display_params_command, {
        label: 'View Selected Search Parameters',
        isEnabled: () => true,
        execute: args => {
            (0,_popups__WEBPACK_IMPORTED_MODULE_15__.displaySearchParams)();
        }
    });
    palette.addItem({ command: display_params_command, category: 'Search' });
    const paste_collection_query_command = 'search:pasteCollectionQuery';
    app.commands.addCommand(paste_collection_query_command, {
        label: 'Paste Collection Search Query',
        isEnabled: () => true,
        execute: args => {
            pasteSearch(args, "query", "collection");
        }
    });
    palette.addItem({ command: paste_collection_query_command, category: 'Search' });
    const paste_granule_query_command = 'search:pasteGranuleQuery';
    app.commands.addCommand(paste_granule_query_command, {
        label: 'Paste Granule Search Query',
        isEnabled: () => true,
        execute: args => {
            pasteSearch(args, "query", "granule");
        }
    });
    palette.addItem({ command: paste_granule_query_command, category: 'Search' });
    const paste_results_command = 'search:pasteResults';
    app.commands.addCommand(paste_results_command, {
        label: 'Paste Granule Search Results',
        isEnabled: () => true,
        execute: args => {
            pasteSearch(args, "results");
        }
    });
    palette.addItem({ command: paste_results_command, category: 'Search' });
    const set_limit_command = 'search:setLimit';
    app.commands.addCommand(set_limit_command, {
        label: 'Set Results Limit',
        isEnabled: () => true,
        execute: args => {
            (0,_popups__WEBPACK_IMPORTED_MODULE_15__.setResultsLimit)();
        }
    });
    palette.addItem({ command: set_limit_command, category: 'Search' });
    const { commands } = app;
    let searchMenu = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.Menu({ commands });
    searchMenu.title.label = 'Data Search';
    [
        open_command,
        display_params_command,
        paste_collection_query_command,
        paste_granule_query_command,
        paste_results_command,
        set_limit_command
    ].forEach(command => {
        searchMenu.addItem({ command });
    });
    mainMenu.addMenu(searchMenu, true, { rank: 100 });
    // Track and restore the widget state
    restorer.restore(instanceTracker, {
        command: open_command,
        name: () => namespace
    });
    console.log('JupyterLab MAAP Earth Data Search Client extension is activated!');
    // assign default values because globals file wasn't doing it
    (_globals__WEBPACK_IMPORTED_MODULE_10___default().limit) = DEFAULT_RESULTS_LIMIT;
    (_globals__WEBPACK_IMPORTED_MODULE_10___default().granuleParams) = null;
    (_globals__WEBPACK_IMPORTED_MODULE_10___default().collectionParams) = null;
    return instanceTracker;
}
;
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);


/***/ }),

/***/ "./lib/popups.js":
/*!***********************!*\
  !*** ./lib/popups.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   displaySearchParams: () => (/* binding */ displaySearchParams),
/* harmony export */   setResultsLimit: () => (/* binding */ setResultsLimit)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _widgets__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./widgets */ "./lib/widgets.js");


function setResultsLimit() {
    (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showDialog)({
        title: 'Set Results Limit:',
        body: new _widgets__WEBPACK_IMPORTED_MODULE_1__.LimitPopupWidget(),
        focusNodeSelector: 'input',
        buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.okButton({ label: 'Ok' })]
    });
}
function displaySearchParams() {
    (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showDialog)({
        title: 'Current Search Parameters:',
        body: new _widgets__WEBPACK_IMPORTED_MODULE_1__.ParamsPopupWidget(),
        focusNodeSelector: 'input',
        buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.okButton({ label: 'Ok' })]
    });
}


/***/ }),

/***/ "./lib/request.js":
/*!************************!*\
  !*** ./lib/request.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   DEFAULT_REQUEST_OPTIONS: () => (/* binding */ DEFAULT_REQUEST_OPTIONS),
/* harmony export */   request: () => (/* binding */ request)
/* harmony export */ });
const DEFAULT_REQUEST_OPTIONS = {
    ignoreCache: false,
    headers: {
        Accept: 'text/html, application/json, text/javascript, text/plain',
    },
    // default max duration for a request
    timeout: 5000,
};
function queryParams(params = {}) {
    return Object.keys(params)
        .map(k => encodeURIComponent(k) + '=' + encodeURIComponent(params[k]))
        .join('&');
}
function withQuery(url, params = {}) {
    const queryString = queryParams(params);
    return queryString ? url + (url.indexOf('?') === -1 ? '?' : '&') + queryString : url;
}
function parseXHRResult(xhr) {
    return {
        ok: xhr.status >= 200 && xhr.status < 300,
        status: xhr.status,
        statusText: xhr.statusText,
        headers: xhr.getAllResponseHeaders(),
        data: xhr.responseText,
        json: () => JSON.parse(xhr.responseText),
        url: xhr.responseURL
    };
}
function errorResponse(xhr, message = null) {
    return {
        ok: false,
        status: xhr.status,
        statusText: xhr.statusText,
        headers: xhr.getAllResponseHeaders(),
        data: message || xhr.statusText,
        json: () => JSON.parse(message || xhr.statusText),
        url: xhr.responseURL
    };
}
function request(method, url, queryParams = {}, body = null, options = DEFAULT_REQUEST_OPTIONS) {
    const ignoreCache = options.ignoreCache || DEFAULT_REQUEST_OPTIONS.ignoreCache;
    const headers = options.headers || DEFAULT_REQUEST_OPTIONS.headers;
    const timeout = options.timeout || DEFAULT_REQUEST_OPTIONS.timeout;
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open(method, withQuery(url, queryParams));
        if (headers) {
            Object.keys(headers).forEach(key => xhr.setRequestHeader(key, headers[key]));
        }
        if (ignoreCache) {
            xhr.setRequestHeader('Cache-Control', 'no-cache');
        }
        xhr.timeout = timeout;
        xhr.onload = evt => {
            resolve(parseXHRResult(xhr));
        };
        xhr.onerror = evt => {
            resolve(errorResponse(xhr, 'Failed to make request.'));
        };
        xhr.ontimeout = evt => {
            resolve(errorResponse(xhr, 'Request took longer than expected.'));
        };
        if (method === 'post' && body) {
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(JSON.stringify(body));
        }
        else {
            xhr.send();
        }
    });
}


/***/ }),

/***/ "./lib/searchKeys.js":
/*!***************************!*\
  !*** ./lib/searchKeys.js ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   collectionNonIndexedKeys: () => (/* binding */ collectionNonIndexedKeys),
/* harmony export */   collectionPermittedCmrKeys: () => (/* binding */ collectionPermittedCmrKeys),
/* harmony export */   granuleNonIndexedKeys: () => (/* binding */ granuleNonIndexedKeys),
/* harmony export */   granulePermittedCmrKeys: () => (/* binding */ granulePermittedCmrKeys)
/* harmony export */ });
/**
 * Whitelist parameters supplied by the request
 * Modified from https://github.com/nasa/earthdata-search/blob/f09ff3bfd40420322f005654bc349374aab1fe57/static/src/js/util/request/granuleRequest.js
 */
const granulePermittedCmrKeys = [
    'concept_id',
    'bounding_box',
    'circle',
    'browse_only',
    'cloud_cover',
    'day_night_flag',
    'echo_collection_id',
    'equator_crossing_date',
    'equator_crossing_longitude',
    'exclude',
    'line',
    'online_only',
    'options',
    'orbit_number',
    'page_num',
    'page_size',
    'point',
    'polygon',
    'readable_granule_name',
    'sort_key',
    'temporal',
    'two_d_coordinate_system'
];
const granuleNonIndexedKeys = [
    'concept_id',
    'exclude',
    'readable_granule_name',
    'sort_key'
];
// Whitelist parameters supplied by the request
const collectionPermittedCmrKeys = [
    'bounding_box',
    'circle',
    'collection_data_type',
    'concept_id',
    'data_center_h',
    'data_center',
    'echo_collection_id',
    'facets_size',
    'format',
    'granule_data_format',
    'granule_data_format_h',
    'has_granules_or_cwic',
    'has_granules',
    'include_facets',
    'include_granule_counts',
    'include_has_granules',
    'include_tags',
    'instrument',
    'instrument_h',
    'keyword',
    'line',
    'options',
    'page_num',
    'page_size',
    'platform',
    'platform_h',
    'point',
    'polygon',
    'processing_level_id_h',
    'project_h',
    'project',
    'provider',
    'science_keywords_h',
    'sort_key',
    'spatial_keyword',
    'tag_key',
    'temporal',
    'two_d_coordinate_system'
];
const collectionNonIndexedKeys = [
    'collection_data_type',
    'concept_id',
    'data_center_h',
    'granule_data_format',
    'granule_data_format_h',
    'instrument',
    'instrument_h',
    'platform',
    'platform_h',
    'processing_level_id_h',
    'project_h',
    'provider',
    'sort_key',
    'spatial_keyword',
    'tag_key'
];


/***/ }),

/***/ "./lib/urlParser.js":
/*!**************************!*\
  !*** ./lib/urlParser.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   decodeUrlParams: () => (/* binding */ decodeUrlParams)
/* harmony export */ });
/* harmony import */ var qs__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! qs */ "webpack/sharing/consume/default/qs/qs");
/* harmony import */ var qs__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(qs__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./encodersDecoders */ "./lib/encodersDecoders.js");
/**
 *
 * Url Decoder copied from earthdata search source code
 * https://github.com/nasa/earthdata-search/blob/master/static/src/js/util/url/url.js#L78
 *
 * June 30, 2020 - https://github.com/nasa/earthdata-search/releases/tag/v1.123.14
 *
 */













/**
 * Mapping of URL Shortened Keys to their redux store keys
 */
const urlDefs = {
    focusedGranule: { shortKey: 'g', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeString, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeString },
    keywordSearch: { shortKey: 'q', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeString, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeString },
    pointSearch: { shortKey: 'sp', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeString, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeString },
    boundingBoxSearch: { shortKey: 'sb', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeString, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeString },
    polygonSearch: { shortKey: 'polygon', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeString, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeString },
    lineSearch: { shortKey: 'line', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeString, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeString },
    circleSearch: { shortKey: 'circle', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeString, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeString },
    map: { shortKey: 'm', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeMap, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeMap },
    temporalSearch: { shortKey: 'qt', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeTemporal, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeTemporal },
    overrideTemporalSearch: { shortKey: 'ot', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeTemporal, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeTemporal },
    featureFacets: { shortKey: 'ff', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeFeatures, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeFeatures },
    platformFacets: { shortKey: 'fp', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeFacets, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeFacets },
    instrumentFacets: { shortKey: 'fi', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeFacets, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeFacets },
    organizationFacets: { shortKey: 'fdc', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeFacets, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeFacets },
    projectFacets: { shortKey: 'fpj', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeFacets, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeFacets },
    processingLevelFacets: { shortKey: 'fl', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeFacets, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeFacets },
    granuleDataFormatFacets: { shortKey: 'gdf', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeFacets, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeFacets },
    gridName: { shortKey: 's2n', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeString, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeString },
    gridCoords: { shortKey: 's2c', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeGridCoords, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeGridCoords },
    shapefileId: { shortKey: 'sf', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeString, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeString },
    tagKey: { shortKey: 'tag_key', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeString, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeString },
    hasGranulesOrCwic: { shortKey: 'ac', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeHasGranulesOrCwic, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeHasGranulesOrCwic },
    autocompleteSelected: { shortKey: 'as', encode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.encodeAutocomplete, decode: _encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeAutocomplete }
};
/**
 * Helper method to decode a given paramName from URL parameters base on urlDefs keys
 * @param {object} params Object of encoded URL parameters
 * @param {string} paramName Param to decode
 */
const decodeHelp = (params, paramName) => {
    const value = params[urlDefs[paramName].shortKey];
    return urlDefs[paramName].decode(value);
};
/**
 * Given a URL param string, returns an object that matches the redux store
 * @param {string} paramString a URL encoded parameter string
 * @return {object} An object of values that match the redux store
 */
const decodeUrlParams = (paramString) => {
    // decode the paramString
    const params = qs__WEBPACK_IMPORTED_MODULE_0___default().parse(paramString, { ignoreQueryPrefix: true, parseArrays: false });
    // build the param object based on the structure in the redux store
    // e.g. map is store separately from query
    const focusedGranule = decodeHelp(params, 'focusedGranule');
    const map = decodeHelp(params, 'map');
    const spatial = {};
    spatial.point = decodeHelp(params, 'pointSearch');
    spatial.boundingBox = decodeHelp(params, 'boundingBoxSearch');
    spatial.polygon = decodeHelp(params, 'polygonSearch');
    spatial.line = decodeHelp(params, 'lineSearch');
    spatial.circle = decodeHelp(params, 'circleSearch');
    const collectionQuery = { pageNum: 1 };
    const granuleQuery = { pageNum: 1 };
    collectionQuery.spatial = spatial;
    collectionQuery.keyword = decodeHelp(params, 'keywordSearch');
    collectionQuery.temporal = decodeHelp(params, 'temporalSearch');
    collectionQuery.overrideTemporal = decodeHelp(params, 'overrideTemporalSearch');
    collectionQuery.gridName = decodeHelp(params, 'gridName');
    collectionQuery.tagKey = decodeHelp(params, 'tagKey');
    collectionQuery.hasGranulesOrCwic = decodeHelp(params, 'hasGranulesOrCwic');
    granuleQuery.gridCoords = decodeHelp(params, 'gridCoords');
    const query = {
        collection: collectionQuery,
        granule: granuleQuery
    };
    const timeline = (0,_encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeTimeline)(params);
    const featureFacets = decodeHelp(params, 'featureFacets');
    const granuleDataFormats = decodeHelp(params, 'granuleDataFormatFacets');
    const instruments = decodeHelp(params, 'instrumentFacets');
    const organizations = decodeHelp(params, 'organizationFacets');
    const platforms = decodeHelp(params, 'platformFacets');
    const processingLevels = decodeHelp(params, 'processingLevelFacets');
    const projects = decodeHelp(params, 'projectFacets');
    const scienceKeywords = (0,_encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeScienceKeywords)(params);
    const { collections, focusedCollection, project } = (0,_encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeCollections)(params);
    const cmrFacets = {
        data_center_h: organizations,
        instrument_h: instruments,
        granule_data_format_h: granuleDataFormats,
        platform_h: platforms,
        processing_level_id_h: processingLevels,
        project_h: projects,
        science_keywords_h: scienceKeywords
    };
    const shapefile = {
        shapefileId: decodeHelp(params, 'shapefileId')
    };
    const advancedSearch = (0,_encodersDecoders__WEBPACK_IMPORTED_MODULE_1__.decodeAdvancedSearch)(params);
    const autocompleteSelected = decodeHelp(params, 'autocompleteSelected');
    // Fetch collections in the project
    const { collectionIds = [] } = project || {};
    // Create a unique list of collections to fetch and remove any empty values [.filter(Boolean)]
    const uniqueCollectionList = [...new Set([
            ...collectionIds,
            focusedCollection
        ])].filter(Boolean);
    return {
        advancedSearch,
        autocompleteSelected,
        cmrFacets,
        collections,
        featureFacets,
        focusedCollection,
        focusedGranule,
        map,
        conceptId: uniqueCollectionList,
        query,
        shapefile,
        timeline
    };
};


/***/ }),

/***/ "./lib/widgets.js":
/*!************************!*\
  !*** ./lib/widgets.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   FlexiblePopupWidget: () => (/* binding */ FlexiblePopupWidget),
/* harmony export */   IFrameWidget: () => (/* binding */ IFrameWidget),
/* harmony export */   LimitPopupWidget: () => (/* binding */ LimitPopupWidget),
/* harmony export */   ParamsPopupWidget: () => (/* binding */ ParamsPopupWidget)
/* harmony export */ });
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _request__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./request */ "./lib/request.js");
/* harmony import */ var _globals__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./globals */ "./lib/globals.js");
/* harmony import */ var _globals__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_globals__WEBPACK_IMPORTED_MODULE_4__);




//import "./globals"

let unique = 0;
//
// Widget to display Earth Data Search Client inside an iframe
//
class IFrameWidget extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget {
    constructor(path) {
        super();
        this.id = path + '-' + unique;
        unique += 1;
        this.title.label = "Earthdata Search";
        this.title.closable = true;
        let div = document.createElement('div');
        div.classList.add('iframe-widget');
        let iframe = document.createElement('iframe');
        iframe.id = "iframeid";
        // set proxy to EDSC
        (0,_request__WEBPACK_IMPORTED_MODULE_3__.request)('get', path).then((res) => {
            if (res.ok) {
                iframe.src = path;
            }
            else {
                iframe.setAttribute('baseURI', _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__.PageConfig.getBaseUrl());
                if (res.status == 404) {
                }
                else if (res.status == 401) {
                }
                else {
                    path = "edsc/proxy/" + path;
                    iframe.src = path;
                }
            }
        });
        div.appendChild(iframe);
        this.node.appendChild(div);
    }
}
;
//
// Widget to display selected search parameter
//
class ParamsPopupWidget extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget {
    constructor() {
        let body = document.createElement('div');
        body.style.display = 'flex';
        body.style.flexDirection = 'column';
        let showGranuleParams = (_globals__WEBPACK_IMPORTED_MODULE_4___default().granuleParams);
        let showCollectionParams = (_globals__WEBPACK_IMPORTED_MODULE_4___default().collectionParams);
        if (showGranuleParams != null && showGranuleParams["concept_id"].length == 0) {
            showGranuleParams = null;
        }
        if (showCollectionParams != null && showCollectionParams["concept_id"].length == 0) {
            showCollectionParams = null;
        }
        body.innerHTML = "<pre>Granule search: " + JSON.stringify(showGranuleParams, null, " ") + "</pre><br>"
            + "<pre>Collection search: " + JSON.stringify(showCollectionParams, null, " ") + "</pre><br>"
            + "<pre>Results Limit: " + (_globals__WEBPACK_IMPORTED_MODULE_4___default().limit) + "</pre>";
        super({ node: body });
    }
}
//
// Popup widget to display any string message
//
class FlexiblePopupWidget extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget {
    constructor(text) {
        let body = document.createElement('div');
        body.style.display = 'flex';
        body.style.flexDirection = 'column';
        body.innerHTML = text;
        super({ node: body });
    }
}
//
// Widget with popup to set search results limit
//
class LimitPopupWidget extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget {
    constructor() {
        let body = document.createElement('div');
        body.style.display = 'flex';
        body.style.flexDirection = 'column';
        super({ node: body });
        this.getValue = this.getValue.bind(this);
        let inputLimit = document.createElement('input');
        inputLimit.id = 'inputLimit';
        inputLimit.value = String((_globals__WEBPACK_IMPORTED_MODULE_4___default().limit));
        this.node.appendChild(inputLimit);
    }
    /* sets limit */
    /**
     * Check for the following error cases in limit: some letters some numbers, negative number
     * float with letters and numbers, operations/ other characters, and value greater than maximum int
     * (9007199254740991)
     * A float is automatically rounded down to the next closest integer
     */
    getValue() {
        let limitTemp = parseInt(document.getElementById('inputLimit').value);
        if (Number.isNaN(limitTemp) || limitTemp < 0) {
            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.Notification.error("Please enter a positive integer for results limit", { autoClose: 3000 });
        }
        else if (limitTemp > Number.MAX_SAFE_INTEGER) {
            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.Notification.error("Please enter a positive integer less than 9007199254740991");
        }
        else {
            (_globals__WEBPACK_IMPORTED_MODULE_4___default().limit) = limitTemp;
        }
    }
}


/***/ }),

/***/ "./style/index.css":
/*!*************************!*\
  !*** ./style/index.css ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/styleDomAPI.js */ "./node_modules/style-loader/dist/runtime/styleDomAPI.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/insertBySelector.js */ "./node_modules/style-loader/dist/runtime/insertBySelector.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/setAttributesWithoutAttributes.js */ "./node_modules/style-loader/dist/runtime/setAttributesWithoutAttributes.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/insertStyleElement.js */ "./node_modules/style-loader/dist/runtime/insertStyleElement.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/styleTagTransform.js */ "./node_modules/style-loader/dist/runtime/styleTagTransform.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./index.css */ "./node_modules/css-loader/dist/cjs.js!./style/index.css");

      
      
      
      
      
      
      
      
      

var options = {};

options.styleTagTransform = (_node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5___default());
options.setAttributes = (_node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3___default());

      options.insert = _node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2___default().bind(null, "head");
    
options.domAPI = (_node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1___default());
options.insertStyleElement = (_node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4___default());

var update = _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default()(_node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_6__["default"], options);




       /* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (_node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_6__["default"] && _node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_6__["default"].locals ? _node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_6__["default"].locals : undefined);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.7bb7efd70b1ae8e1c62b.js.map