/*! For license information please see 26149.6b55ea25441038791018.index.js.LICENSE.txt */
(self.webpackChunkrichie_education=self.webpackChunkrichie_education||[]).push([[26149],{5903:function(e,t,r){"use strict";r.d(t,{I:function(){return l},f:function(){return a}}),r(32351),r(48339),r(89327),r(91144),r(3636),r(94204),r(36008),r(12888),r(76911),r(61770),r(52508),r(94711),r(25648),r(45472),r(11021),r(92262),r(16374);var n=r(64922);function o(e){return o="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},o(e)}var i=["name","title","className","size"];function c(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function u(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?c(Object(r),!0).forEach((function(t){s(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):c(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function s(e,t,r){return(t=function(e){var t=function(e,t){if("object"!=o(e)||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,"string");if("object"!=o(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"==o(t)?t:t+""}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var a=function(e){return e.ARCHIVE="icon-archive",e.ARROW_RIGHT="icon-arrow-right",e.ARROW_RIGHT_ROUNDED="icon-arrow-right-rounded",e.BARCODE="icon-barcode",e.CAL="icon-cal",e.CALENDAR="icon-calendar",e.CAMERA="icon-camera",e.CERTIFICATE="icon-certificate",e.CHECK="icon-check",e.CHECK_ROUNDED="icon-check-rounded",e.CHECKLIST="icon-checklist",e.CHEVRON_DOWN="icon-chevron-down",e.CHEVRON_DOWN_OUTLINE="icon-chevron-down-outline",e.CHEVRON_LEFT_OUTLINE="icon-chevron-left-outline",e.CHEVRON_RIGHT_OUTLINE="icon-chevron-right-outline",e.CHEVRON_UP_OUTLINE="icon-chevron-up-outline",e.CLOCK="icon-clock",e.CREDIT_CARD="icon-creditCard",e.CROSS="icon-cross",e.DURATION="icon-duration",e.ENVELOPE="icon-envelope",e.FACEBOOK="icon-facebook",e.FILTER="icon-filter",e.GROUPS="icon-groups",e.INFO_ROUNDED="icon-info-rounded",e.LANGUAGES="icon-languages",e.LINKEDIN="icon-linkedin",e.LOGIN="icon-login",e.LOGOUT_SQUARE="icon-logout-square",e.MAGNIFYING_GLASS="icon-magnifying-glass",e.MENU="icon-menu",e.MORE="icon-more",e.ORG="icon-org",e.PACE="icon-pace",e.PLUS="icon-plus",e.QUOTE="icon-quote",e.ROUND_CLOSE="icon-round-close",e.SCHOOL="icon-school",e.SEARCH_FAIL="icon-search-fail",e.STOPWATCH="icon-stopwatch",e.THREE_VERTICAL_DOTS="icon-three-vertical-dots",e.TWITTER="icon-twitter",e.UNIVERSITY="icon-univerity",e.WARNING="icon-warning",e}({}),l=function(e){var t=e.name,r=e.title,o=e.className,c=void 0===o?"":o,s=e.size,a=void 0===s?"medium":s,l=function(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r={};for(var n in e)if({}.hasOwnProperty.call(e,n)){if(t.indexOf(n)>=0)continue;r[n]=e[n]}return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||{}.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}(e,i);return(0,n.jsxs)("svg",u(u(u({className:"icon icon--".concat(a," ").concat(c),"aria-hidden":!r||void 0},r&&{role:"img","aria-label":r}),l),{},{children:[r&&(0,n.jsx)("title",{children:r}),(0,n.jsx)("use",{href:"#".concat(t)})]}))}},62162:function(e,t,r){"use strict";r.d(t,{t:function(){return l}});var n=r(93219),o=r(43346),i=r(11199),c=r(13481),u=r(67833),s={queryKey:["profile"],apiInterface:function(){return(0,i.Q)().user.me},session:!0,messages:(0,o.YK)({errorGet:{id:"hooks.useJoanieUserProfile.errorGet",defaultMessage:[{type:0,value:"An error occurred while fetching user profile information. Please retry later."}]},errorNotFound:{id:"hooks.useJoanieUserProfile.errorNotFound",defaultMessage:[{type:0,value:"You aren't logged in."}]}})},a=r(37537),l=function(){if(n.cl){var e=(t=(0,c.w)().user,(0,u.qK)(s)(void 0,{},{enabled:!!t})).item;return e?a.A.buildEntityInterface(e):void 0}var t}},72789:function(e,t,r){"use strict";r.d(t,{U:function(){return s}}),r(32351),r(48339),r(89327),r(89886),r(94204),r(61346),r(16374),r(94711),r(82067),r(67873),r(25648),r(11021);var n=r(77810),o=r(10847),i=r(37591);function c(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=Array(t);r<t;r++)n[r]=e[r];return n}var u=function(e){var t,r,i=(0,n.useMemo)((function(){return(0,o.cq)(e)}),[e]),u=(t=(0,n.useState)(i.matches),r=2,function(e){if(Array.isArray(e))return e}(t)||function(e,t){var r=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=r){var n,o,i,c,u=[],s=!0,a=!1;try{if(i=(r=r.call(e)).next,0===t){if(Object(r)!==r)return;s=!1}else for(;!(s=(n=i.call(r)).done)&&(u.push(n.value),u.length!==t);s=!0);}catch(e){a=!0,o=e}finally{try{if(!s&&null!=r.return&&(c=r.return(),Object(c)!==c))return}finally{if(a)throw o}}return u}}(t,r)||function(e,t){if(e){if("string"==typeof e)return c(e,t);var r={}.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?c(e,t):void 0}}(t,r)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()),s=u[0],a=u[1],l=(0,n.useCallback)((function(e){return a(e.matches)}),[a]);return(0,n.useEffect)((function(){return i.addEventListener?i.addEventListener("change",l):i.addListener(l),function(){i.removeEventListener?i.removeEventListener("change",l):i.removeListener(l)}}),[i]),s},s=function(){return u("(max-width: ".concat(i.L.themes.default.theme.breakpoints.lg,")"))};t.A=u},37537:function(e,t,r){"use strict";r.d(t,{g:function(){return g},A:function(){return O}}),r(32351),r(48339),r(89327),r(91144),r(3636),r(94204),r(36008),r(12888),r(76911),r(61770),r(52508),r(94711),r(25648),r(45472),r(11021);var n=r(21492);function o(e){return o="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},o(e)}var i,c,u,s=(i={},u=function(e){var t;return!0===(null==e||null===(t=e.abilities)||void 0===t?void 0:t.sign)},(c=function(e){var t=function(e,t){if("object"!=o(e)||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,"string");if("object"!=o(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"==o(t)?t:t+""}(c=n.SH.SIGN))in i?Object.defineProperty(i,c,{value:u,enumerable:!0,configurable:!0,writable:!0}):i[c]=u,i),a=function(e){return e.DELETE="delete",e.GET="get",e.PATCH="patch",e.PUT="put",e.HAS_COURSE_ACCESS="has_course_access",e.HAS_ORGANIZATION_ACCESS="has_organization_access",e}({});function l(e){return l="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},l(e)}var f=function(e,t,r){return(t=function(e){var t=function(e,t){if("object"!=l(e)||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,"string");if("object"!=l(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"==l(t)?t:t+""}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}({},n.cL.ACCESS_TEACHER_DASHBOARD,(function(e){return Boolean(e.abilities[a.HAS_ORGANIZATION_ACCESS])||Boolean(e.abilities[a.HAS_COURSE_ACCESS])})),y=f;function p(e){return p="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},p(e)}function b(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function m(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?b(Object(r),!0).forEach((function(t){d(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):b(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function d(e,t,r){return(t=function(e){var t=function(e,t){if("object"!=p(e)||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,"string");if("object"!=p(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"==p(t)?t:t+""}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var g=m(m({},n.cL),n.SH),h=function(e,t){if(!e)return!1;if(Array.isArray(e)){if(0===e.length)return!1}else e=[e];return e.every((function(e){return(0,n.Kf)(e)?y[t](e):!!(0,n.uq)(e)&&s[t](e)}))},v=function(e,t){return!h(e,t)},O={can:h,cannot:v,buildEntityInterface:function(e){return{can:function(t){return h(e,t)},cannot:function(t){return v(e,t)}}}}},21492:function(e,t,r){"use strict";r.d(t,{Kf:function(){return c},SH:function(){return o},cL:function(){return n},uq:function(){return u}}),r(40187),r(52508),r(94711);var n=function(e){return e.ACCESS_TEACHER_DASHBOARD="access_teacher_dashboard",e}({}),o=function(e){return e.SIGN="sign",e}({}),i=["abilities","full_name","id","is_staff","is_superuser","username"],c=function(e){var t=Object.keys(e);return t.length===i.length&&t.every((function(e){return i.includes(e)}))},u=function(e){return["student_signed_on","organization_signed_on","definition","order"].every((function(t){return e.hasOwnProperty(t)}))}},53642:function(e,t,r){"use strict";function n(e){return n="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},n(e)}function o(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,i(n.key),n)}}function i(e){var t=function(e,t){if("object"!=n(e)||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var o=r.call(e,"string");if("object"!=n(o))return o;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"==n(t)?t:t+""}r.d(t,{g:function(){return c}}),r(32351),r(48339),r(89327),r(91144),r(94204),r(36008),r(12888),r(94711),r(25648),r(11021);var c=function(){return e=function e(){!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,e)},t=[{key:"getName",value:function(e){return(null==e?void 0:e.full_name)||e.username}}],null&&o(e.prototype,null),t&&o(e,t),Object.defineProperty(e,"prototype",{writable:!1}),e;var e,t}()},37591:function(e,t,r){"use strict";r.d(t,{L:function(){return n}});var n={themes:{default:{theme:{colors:{"secondary-text":"#555F6B","secondary-100":"#eff8ff","secondary-200":"#eaf3fd","secondary-300":"#e2ebf5","secondary-400":"#c0c9d3","secondary-500":"#a3abb4","secondary-600":"#79818a","secondary-700":"#656c75","secondary-800":"#454d55","secondary-900":"#242b32","info-text":"#FFFFFF","info-100":"#EBF2FC","info-200":"#8CB5EA","info-300":"#5894E1","info-400":"#377FDB","info-500":"#055FD2","info-600":"#0556BF","info-700":"#044395","info-800":"#033474","info-900":"#022858","greyscale-100":"#FAFAFB","greyscale-200":"#F3F4F4","greyscale-300":"#E7E8EA","greyscale-400":"#C2C6CA","greyscale-500":"#9EA3AA","greyscale-600":"#79818A","greyscale-700":"#555F6B","greyscale-800":"#303C4B","greyscale-900":"#0C1A2B","greyscale-000":"#FFFFFF","primary-100":"#ffcad1","primary-200":"#f19597","primary-300":"#e86a6f","primary-400":"#f2444b","primary-500":"#f72c30","primary-600":"#e81f2f","primary-700":"#d60f29","primary-800":"#c90022","primary-900":"#bb0014","success-100":"#EFFCD3","success-200":"#DBFAA9","success-300":"#BEF27C","success-400":"#A0E659","success-500":"#76D628","success-600":"#5AB81D","success-700":"#419A14","success-800":"#2C7C0C","success-900":"#1D6607","warning-100":"#FFF8CD","warning-200":"#FFEF9B","warning-300":"#FFE469","warning-400":"#FFDA43","warning-500":"#FFC805","warning-600":"#DBA603","warning-700":"#B78702","warning-800":"#936901","warning-900":"#7A5400","danger-100":"#F4B0B0","danger-200":"#EE8A8A","danger-300":"#E65454","danger-400":"#E13333","danger-500":"#DA0000","danger-600":"#C60000","danger-700":"#9B0000","danger-800":"#780000","danger-900":"#5C0000","primary-text":"#FFFFFF","success-text":"#FFFFFF","warning-text":"#FFFFFF","danger-text":"#FFFFFF",black:"#090909","dark-grey":"#232323",charcoal:"#29303b","slate-grey":"#686868","battleship-grey":"#686f7a","light-grey":"#d2d2d2",silver:"#d5dbe0",azure2:"#eceff1",smoke:"#fdfdfd",white:"#ffffff",denim:"#0067b7",firebrick6:"#f72c30","purplish-grey":"#726c74",grey32:"#525151",grey59:"#969696",grey87:"#dfdfdf",indianred3:"#df484b",midnightblue:"#141b2c",mantis:"#76ce68","mantis-darken":"#006908"},font:{sizes:{h1:"1.75rem",h2:"1.375rem",h3:"1.125rem",h4:"0.8125rem",h5:"0.625rem",h6:"0.5rem",l:"1rem",m:"0.8125rem",s:"0.6875rem"},weights:{thin:200,light:300,regular:400,medium:500,bold:600,extrabold:700,black:800},families:{base:"Hind",accent:"Montserrat"},letterSpacings:{h1:"normal",h2:"normal",h3:"normal",h4:"normal",h5:"1px",h6:"normal",l:"normal",m:"normal",s:"normal"}},spacings:{xl:"4rem",l:"3rem",b:"1.625rem",s:"1rem",t:"0.5rem",st:"0.25rem"},transitions:{"ease-in":"cubic-bezier(0.32, 0, 0.67, 0)","ease-out":"cubic-bezier(0.33, 1, 0.68, 1)","ease-in-out":"cubic-bezier(0.65, 0, 0.35, 1)",duration:"250ms"},breakpoints:{xs:0,sm:"576px",md:"768px",lg:"992px",xl:"1200px",xxl:"1400px"}},components:{tabs:{"border-bottom-color":"#E7E8EA"},button:{"font-family":"Montserrat"},dashboardListAvatar:{saturation:30,lightness:55}}},dark:{theme:{colors:{"greyscale-100":"#182536","greyscale-200":"#303C4B","greyscale-300":"#555F6B","greyscale-400":"#79818A","greyscale-500":"#9EA3AA","greyscale-600":"#C2C6CA","greyscale-700":"#E7E8EA","greyscale-800":"#F3F4F4","greyscale-900":"#FAFAFB","greyscale-000":"#0C1A2B","primary-100":"#3B4C62","primary-200":"#4D6481","primary-300":"#6381A6","primary-400":"#7FA5D5","primary-500":"#8CB5EA","primary-600":"#A3C4EE","primary-700":"#C3D8F4","primary-800":"#DDE9F8","primary-900":"#F4F8FD","success-100":"#EEF8D7","success-200":"#D9F1B2","success-300":"#BDE985","success-400":"#A0E25D","success-500":"#76D628","success-600":"#5BB520","success-700":"#43941A","success-800":"#307414","success-900":"#225D10","warning-100":"#F7F3D5","warning-200":"#F0E5AA","warning-300":"#E8D680","warning-400":"#E3C95F","warning-500":"#D9B32B","warning-600":"#BD9721","warning-700":"#9D7B1C","warning-800":"#7E6016","warning-900":"#684D12","danger-100":"#F8D0D0","danger-200":"#F09898","danger-300":"#F09898","danger-400":"#ED8585","danger-500":"#E96666","danger-600":"#DD6666","danger-700":"#C36666","danger-800":"#AE6666","danger-900":"#9D6666"}}}}}},51961:function(e,t,r){"use strict";r.r(t),r.d(t,{default:function(){return H}}),r(32351),r(48339),r(89327),r(43361),r(91144),r(92262),r(3636),r(89886),r(94204),r(71698),r(74666),r(61346),r(36008),r(16374),r(12888),r(86886),r(76911),r(61770),r(52508),r(94711),r(94644),r(82067),r(67873),r(25648),r(3484),r(81632),r(45472),r(11021);var n=r(77810),o=r(43346),i=r(25811),c=r(5903),u=r(13481),s=r(37537),a=r(62162),l=r(72789),f=(r(11909),r(8602)),y=r(69122),p=r.n(y),b=r(10847),m=r(53642),d=r(64922);function g(e){return g="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},g(e)}function h(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function v(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?h(Object(r),!0).forEach((function(t){O(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):h(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function O(e,t,r){return(t=function(e){var t=function(e,t){if("object"!=g(e)||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,"string");if("object"!=g(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"==g(t)?t:t+""}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function S(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=Array(t);r<t;r++)n[r]=e[r];return n}var E=(0,o.YK)({menuPurpose:{id:"components.DesktopUserMenu.menuPurpose",defaultMessage:[{type:0,value:"Access to your profile settings"}]}}),j=function(e){var t,r,n=e.user,i=n.urls.map((function(e){return e})),c=(0,f.WM)({items:i,onSelectedItemChange:function(e){var t=e.selectedItem;"string"==typeof t.action?b.C5.replace(t.action):t.action()}}),u=c.isOpen,s=c.highlightedIndex,a=c.getMenuProps,l=c.getItemProps,y=c.getToggleButtonProps,g=c.getLabelProps,h=n.urls.find((function(e){return"dashboard_teacher"===e.key}));return t=h?[h].concat(function(e){if(Array.isArray(e))return S(e)}(r=n.urls.filter((function(e){return"dashboard_teacher"!==e.key})))||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(r)||function(e,t){if(e){if("string"==typeof e)return S(e,t);var r={}.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?S(e,t):void 0}}(r)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()):n.urls,(0,d.jsxs)("div",{className:"user-menu user-menu--desktop selector",children:[(0,d.jsx)("label",v(v({},g()),{},{className:"offscreen",children:(0,d.jsx)(o.sA,v({},E.menuPurpose))})),(0,d.jsxs)("button",v(v({},y()),{},{className:"selector__button",children:[m.g.getName(n),(0,d.jsx)("svg",{role:"img",className:"selector__button__icon","aria-hidden":"true",children:(0,d.jsx)("use",{xlinkHref:"#icon-chevron-down"})})]})),(0,d.jsx)("ul",v(v({},a()),{},{className:"selector__list ".concat(u?"":"selector__list--is-closed"),children:u&&t.map((function(e,t){return(0,d.jsx)("li",v(v({},l({item:e,index:t})),{},{className:p()({"selector__list__item--bordered":"dashboard_teacher"===e.key}),children:"string"==typeof e.action?(0,d.jsx)("a",{className:"selector__list__link ".concat(s===t?"selector__list__link--highlighted":""),href:e.action,children:e.label}):(0,d.jsx)("button",{className:"selector__list__link\n                  ".concat(s===t?"selector__list__link--highlighted":""),children:e.label})}),e.key)}))}))]})},A=function(e){var t=e.user;return(0,d.jsxs)("div",{className:"user-menu user-menu--mobile",children:[(0,d.jsxs)("h6",{className:"user-menu__username",children:[(0,d.jsx)(c.I,{name:c.f.LOGIN}),m.g.getName(t)]}),(0,d.jsx)("ul",{className:"user-menu__list",children:t.urls.map((function(e){var t=e.key,r=e.label,n=e.action;return(0,d.jsx)("li",{className:"user-menu__list__item",children:"string"==typeof n?(0,d.jsx)("a",{href:n,children:r}):(0,d.jsx)("button",{onClick:n,children:r})},t)}))})]})};function w(e){return w="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},w(e)}function _(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function C(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?_(Object(r),!0).forEach((function(t){F(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):_(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function F(e,t,r){return(t=function(e){var t=function(e,t){if("object"!=w(e)||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,"string");if("object"!=w(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"==w(t)?t:t+""}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var P=function(e){return(0,l.A)("(min-width: 992px)")?(0,d.jsx)(j,C({},e)):(0,d.jsx)(A,C({},e))};function D(e){return D="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},D(e)}function x(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function N(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?x(Object(r),!0).forEach((function(t){R(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):x(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function R(e,t,r){return(t=function(e){var t=function(e,t){if("object"!=D(e)||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,"string");if("object"!=D(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"==D(t)?t:t+""}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function I(e,t){if(e){if("string"==typeof e)return k(e,t);var r={}.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?k(e,t):void 0}}function k(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=Array(t);r<t;r++)n[r]=e[r];return n}function T(){T=function(e,t){return new r(e,void 0,t)};var e=RegExp.prototype,t=new WeakMap;function r(e,n,o){var i=RegExp(e,n);return t.set(i,o||t.get(e)),L(i,r.prototype)}function n(e,r){var n=t.get(r);return Object.keys(n).reduce((function(t,r){var o=n[r];if("number"==typeof o)t[r]=e[o];else{for(var i=0;void 0===e[o[i]]&&i+1<o.length;)i++;t[r]=e[o[i]]}return t}),Object.create(null))}return function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),Object.defineProperty(e,"prototype",{writable:!1}),t&&L(e,t)}(r,RegExp),r.prototype.exec=function(t){var r=e.exec.call(this,t);if(r){r.groups=n(r,this);var o=r.indices;o&&(o.groups=n(o,this))}return r},r.prototype[Symbol.replace]=function(r,o){if("string"==typeof o){var i=t.get(this);return e[Symbol.replace].call(this,r,o.replace(/\$<([^>]+)>/g,(function(e,t){var r=i[t];return"$"+(Array.isArray(r)?r.join("$"):r)})))}if("function"==typeof o){var c=this;return e[Symbol.replace].call(this,r,(function(){var e=arguments;return"object"!=D(e[e.length-1])&&(e=[].slice.call(e)).push(n(e,c)),o.apply(this,e)}))}return e[Symbol.replace].call(this,r,o)},T.apply(this,arguments)}function L(e,t){return L=Object.setPrototypeOf?Object.setPrototypeOf.bind():function(e,t){return e.__proto__=t,e},L(e,t)}var M=(0,o.YK)({logIn:{id:"components.UserLogin.logIn",defaultMessage:[{type:0,value:"Log in"}]},logOut:{id:"components.UserLogin.logOut",defaultMessage:[{type:0,value:"Log out"}]},signUp:{id:"components.UserLogin.signup",defaultMessage:[{type:0,value:"Sign up"}]},spinnerText:{id:"components.UserLogin.spinnerText",defaultMessage:[{type:0,value:"Loading login status..."}]}}),B=T(/\(([a-zA-Z0-9-_]*)\)/g,{prop:1}),U=function(e,t){return e.replace(B,(function(e,r){return"string"==typeof t[r]?t[r]:e}))},H=function(e){var t=e.profileUrls,r=void 0===t?{}:t,l=(0,u.w)(),f=l.user,y=l.destroy,p=l.login,b=l.register,m=(0,o.tz)(),g=(0,a.t)(),h=function(e){return"dashboard_teacher"!==e.key||!(null==g||!g.can(s.g.ACCESS_TEACHER_DASHBOARD))},v=(0,n.useMemo)((function(){return f?[].concat(function(e){if(Array.isArray(e))return k(e)}(e=Object.entries(r).map((function(e){var t,r,n=(r=2,function(e){if(Array.isArray(e))return e}(t=e)||function(e,t){var r=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=r){var n,o,i,c,u=[],s=!0,a=!1;try{if(i=(r=r.call(e)).next,0===t){if(Object(r)!==r)return;s=!1}else for(;!(s=(n=i.call(r)).done)&&(u.push(n.value),u.length!==t);s=!0);}catch(e){a=!0,o=e}finally{try{if(!s&&null!=r.return&&(c=r.return(),Object(c)!==c))return}finally{if(a)throw o}}return u}}(t,r)||I(t,r)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()),o=n[0],i=n[1],c=i.label,u=i.action;return{key:o,label:c,action:"string"==typeof u?U(u,f):u}})).filter(h))||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(e)||I(e)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}(),[{key:"logout",label:m.formatMessage(M.logOut),action:y}]):[];var e}),[f,g]);return(0,d.jsx)("div",{className:"user-login",children:void 0===f?(0,d.jsx)(i.y,{size:"small",children:(0,d.jsx)(o.sA,N({},M.spinnerText))}):null===f?(0,d.jsxs)(n.Fragment,{children:[(0,d.jsx)("button",{onClick:b,className:"user-login__btn user-login__btn--sign-up",children:(0,d.jsx)(o.sA,N({},M.signUp))}),(0,d.jsxs)("button",{onClick:p,className:"user-login__btn user-login__btn--log-in",children:[(0,d.jsx)(c.I,{name:c.f.LOGIN,size:"small"}),(0,d.jsx)(o.sA,N({},M.logIn))]})]}):(0,d.jsx)(P,{user:N(N({},f),{},{urls:v})})})}},69122:function(e,t){var r;!function(){"use strict";var n={}.hasOwnProperty;function o(){for(var e="",t=0;t<arguments.length;t++){var r=arguments[t];r&&(e=c(e,i(r)))}return e}function i(e){if("string"==typeof e||"number"==typeof e)return e;if("object"!=typeof e)return"";if(Array.isArray(e))return o.apply(null,e);if(e.toString!==Object.prototype.toString&&!e.toString.toString().includes("[native code]"))return e.toString();var t="";for(var r in e)n.call(e,r)&&e[r]&&(t=c(t,r));return t}function c(e,t){return t?e?e+" "+t:e+t:e}e.exports?(o.default=o,e.exports=o):void 0===(r=function(){return o}.apply(t,[]))||(e.exports=r)}()},11909:function(e,t,r){"use strict";var n=r(53762),o=r(47033).find,i=r(1825),c="find",u=!0;c in[]&&Array(1)[c]((function(){u=!1})),n({target:"Array",proto:!0,forced:u},{find:function(e){return o(this,e,arguments.length>1?arguments[1]:void 0)}}),i(c)},96638:function(e,t,r){"use strict";var n=r(53762),o=r(18761).values;n({target:"Object",stat:!0},{values:function(e){return o(e)}})},43361:function(e,t,r){"use strict";r(61051)("replace")},77786:function(e,t,r){"use strict";r.d(t,{n:function(){return f}});var n=r(77810),o=r(24370),i=r(10049),c=r(21664),u=r(47396),s=class extends c.Q{#e;#t=void 0;#r;#n;constructor(e,t){super(),this.#e=e,this.setOptions(t),this.bindMethods(),this.#o()}bindMethods(){this.mutate=this.mutate.bind(this),this.reset=this.reset.bind(this)}setOptions(e){const t=this.options;this.options=this.#e.defaultMutationOptions(e),(0,u.f8)(this.options,t)||this.#e.getMutationCache().notify({type:"observerOptionsUpdated",mutation:this.#r,observer:this}),t?.mutationKey&&this.options.mutationKey&&(0,u.EN)(t.mutationKey)!==(0,u.EN)(this.options.mutationKey)?this.reset():"pending"===this.#r?.state.status&&this.#r.setOptions(this.options)}onUnsubscribe(){this.hasListeners()||this.#r?.removeObserver(this)}onMutationUpdate(e){this.#o(),this.#i(e)}getCurrentResult(){return this.#t}reset(){this.#r?.removeObserver(this),this.#r=void 0,this.#o(),this.#i()}mutate(e,t){return this.#n=t,this.#r?.removeObserver(this),this.#r=this.#e.getMutationCache().build(this.#e,this.options),this.#r.addObserver(this),this.#r.execute(e)}#o(){const e=this.#r?.state??(0,o.$)();this.#t={...e,isPending:"pending"===e.status,isSuccess:"success"===e.status,isError:"error"===e.status,isIdle:"idle"===e.status,mutate:this.mutate,reset:this.reset}}#i(e){i.j.batch((()=>{if(this.#n&&this.hasListeners()){const t=this.#t.variables,r=this.#t.context;"success"===e?.type?(this.#n.onSuccess?.(e.data,t,r),this.#n.onSettled?.(e.data,null,t,r)):"error"===e?.type&&(this.#n.onError?.(e.error,t,r),this.#n.onSettled?.(void 0,e.error,t,r))}this.listeners.forEach((e=>{e(this.#t)}))}))}},a=r(80933),l=r(97590);function f(e,t){const r=(0,a.jE)(t),[o]=n.useState((()=>new s(r,e)));n.useEffect((()=>{o.setOptions(e)}),[o,e]);const c=n.useSyncExternalStore(n.useCallback((e=>o.subscribe(i.j.batchCalls(e))),[o]),(()=>o.getCurrentResult()),(()=>o.getCurrentResult())),u=n.useCallback(((e,t)=>{o.mutate(e,t).catch(l.l)}),[o]);if(c.error&&(0,l.G)(o.options.throwOnError,[c.error]))throw c.error;return{...c,mutate:u,mutateAsync:c.mutate}}}}]);
//# sourceMappingURL=26149.6b55ea25441038791018.index.js.map