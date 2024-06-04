"use strict";(self.webpackChunkrichie_education=self.webpackChunkrichie_education||[]).push([[48631],{33180:function(e,t,r){r.d(t,{N:function(){return D},z:function(){return C}}),r(32351),r(48339),r(89327),r(91144),r(3636),r(94204),r(71698),r(74666),r(36008),r(12888),r(76911),r(61770),r(52508),r(94711),r(25648),r(45472),r(11021);var o=r(43346),a=r(77810),n=r(5903),s=r(64922),i=(0,o.YK)({dateIconAlt:{id:"components.CourseGlimpseFooter.dateIconAlt",defaultMessage:[{type:0,value:"Course date"}]}}),c=function(e){var t=e.course,r=(0,o.tz)();return(0,s.jsx)("div",{className:"course-glimpse-footer",children:(0,s.jsxs)("div",{className:"course-glimpse-footer__date",children:[(0,s.jsx)(n.I,{name:n.f.CALENDAR,title:r.formatMessage(i.dateIconAlt)}),t.state.text.charAt(0).toUpperCase()+t.state.text.substring(1)+(t.state.datetime?" ".concat(r.formatDate(new Date(t.state.datetime),{year:"numeric",month:"short",day:"numeric"})):"")]})})},u=r(81342),l=function(e){var t=e.href,r=e.to,o=e.className,a=e.tabIndex,n=e.children,i=void 0===n?null:n;return t?(0,s.jsx)("a",{href:t,className:o,tabIndex:a,children:i}):r?(0,s.jsx)(u.N_,{to:r,className:o,tabIndex:a,children:i}):i},d=r(81534),p=r(82388),f=r(57489);function g(e){return g="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},g(e)}function m(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,o)}return r}function y(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?m(Object(r),!0).forEach((function(t){b(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):m(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function b(e,t,r){return(t=function(e){var t=function(e,t){if("object"!=g(e)||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var o=r.call(e,"string");if("object"!=g(o))return o;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"==g(t)?t:t+""}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function v(e){return v="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},v(e)}function h(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,o)}return r}function O(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?h(Object(r),!0).forEach((function(t){_(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):h(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function _(e,t,r){return(t=function(e){var t=function(e,t){if("object"!=v(e)||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var o=r.call(e,"string");if("object"!=v(o))return o;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"==v(t)?t:t+""}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var j=(0,o.YK)({cover:{id:"components.CourseGlimpse.cover",defaultMessage:[{type:0,value:"Cover"}]},organizationIconAlt:{id:"components.CourseGlimpse.organizationIconAlt",defaultMessage:[{type:0,value:"Organization"}]},codeIconAlt:{id:"components.CourseGlimpse.codeIconAlt",defaultMessage:[{type:0,value:"Course code"}]},categoryLabel:{id:"components.CourseGlimpse.categoryLabel",defaultMessage:[{type:0,value:"Category"}]}}),N=function(e){var t=e.context,r=e.course,a=(0,o.tz)();return(0,s.jsxs)("div",{className:"course-glimpse","data-testid":"course-glimpse",children:[(0,s.jsx)("div",{"aria-hidden":"true",className:"course-glimpse__media",children:(0,s.jsx)(l,{tabIndex:-1,className:"course-glimpse__link",href:r.course_url,to:r.course_route,children:r.cover_image?(0,s.jsx)("img",{alt:"",sizes:r.cover_image.sizes,src:r.cover_image.src,srcSet:r.cover_image.srcset}):(0,s.jsx)("div",{className:"course-glimpse__media__empty",children:(0,s.jsx)(o.sA,O({},j.cover))})})}),(0,s.jsxs)("div",{className:"course-glimpse__content",children:[(0,s.jsxs)("div",{className:"course-glimpse__wrapper",children:[(0,s.jsx)("h3",{className:"course-glimpse__title",children:(0,s.jsx)(l,{className:"course-glimpse__link",href:r.course_url,to:r.course_route,children:(0,s.jsx)("span",{className:"course-glimpse__title-text",children:r.title})})}),r.organization.image?(0,s.jsx)("div",{className:"course-glimpse__organization-logo",children:(0,s.jsx)("img",{alt:"",sizes:r.organization.image.sizes,src:r.organization.image.src,srcSet:r.organization.image.srcset})}):null,(0,s.jsxs)("div",{className:"course-glimpse__metadata course-glimpse__metadata--organization",children:[(0,s.jsx)(n.I,{name:n.f.ORG,title:a.formatMessage(j.organizationIconAlt),size:"small"}),(0,s.jsx)("span",{className:"title",children:r.organization.title})]}),(0,s.jsxs)("div",{className:"course-glimpse__metadata course-glimpse__metadata--code",children:[(0,s.jsx)(n.I,{name:n.f.BARCODE,title:a.formatMessage(j.codeIconAlt),size:"small"}),(0,s.jsx)("span",{children:r.code||"-"})]})]}),r.icon?(0,s.jsx)("div",{className:"course-glimpse__icon",children:(0,s.jsxs)("span",{className:"category-badge",children:[(0,s.jsx)("img",{alt:"",className:"category-badge__icon",sizes:r.icon.sizes,src:r.icon.src,srcSet:r.icon.srcset}),(0,s.jsx)("span",{className:"offscreen",children:(0,s.jsx)(o.sA,O({},j.categoryLabel))}),(0,s.jsx)("span",{className:"category-badge__title",children:r.icon.title})]})}):null,(0,s.jsx)(c,{context:t,course:r})]})]})},P=function(e,t){return e.context===t.context&&e.course.id===t.course.id},R=(0,a.memo)(N,P),C=function(e,t,r){return e.map((function(e){return function(e,t,r){return(0,p.zY)(e)?function(e,t,r){var o={courseId:e.course.id,courseProductRelationId:e.id},a=r?(0,d.tW)(f.B.ORGANIZATION_PRODUCT,y(y({},o),{},{organizationId:r})):(0,d.tW)(f.B.COURSE_PRODUCT,o);return{id:e.id,code:e.course.code,title:e.product.title,cover_image:e.course.cover?{src:e.course.cover.src}:null,organization:{title:e.organizations[0].title,image:e.organizations[0].logo||null},product_id:e.product.id,course_route:a,state:e.product.state}}(e,0,r):function(e){return void 0!==e.organization_highlighted}(e)?function(e){return{id:e.id,code:e.code,course_url:e.absolute_url,cover_image:e.cover_image,title:e.title,organization:{title:e.organization_highlighted,image:e.organization_highlighted_cover_image},icon:e.icon,state:e.state,duration:e.duration,effort:e.effort,categories:e.categories,organizations:e.organizations}}(e):function(e,t,r){var o={courseId:e.id},a=r?(0,d.tW)(f.B.ORGANIZATION_COURSE_GENERAL_INFORMATION,y(y({},o),{},{organizationId:r})):(0,d.tW)(f.B.COURSE_GENERAL_INFORMATION,o);return{id:e.id,code:e.code,course_route:a,cover_image:e.cover?{src:e.cover.src}:null,title:e.title,organization:{title:e.organizations[0].title,image:e.organizations[0].logo||null},state:e.state,nb_course_runs:e.course_run_ids.length}}(e,0,r)}(e,0,r)}))};function S(e){return S="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},S(e)}function I(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,o)}return r}function T(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?I(Object(r),!0).forEach((function(t){A(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):I(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function A(e,t,r){return(t=function(e){var t=function(e,t){if("object"!=S(e)||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var o=r.call(e,"string");if("object"!=S(o))return o;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"==S(t)?t:t+""}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var x=(0,o.YK)({courseCount:{id:"components.CourseGlimpseList.courseCount",defaultMessage:[{type:0,value:"Showing "},{type:2,style:null,value:"start"},{type:0,value:" to "},{type:2,style:null,value:"end"},{type:0,value:" of "},{type:2,style:null,value:"courseCount"},{type:0,value:" "},{type:6,pluralType:"cardinal",value:"courseCount",offset:0,options:{one:{value:[{type:0,value:"course"}]},other:{value:[{type:0,value:"courses"}]}}},{type:0,value:" matching your search"}]},offscreenCourseCount:{id:"components.CourseGlimpseList.offscreenCourseCount",defaultMessage:[{type:2,style:null,value:"courseCount"},{type:0,value:" "},{type:6,pluralType:"cardinal",value:"courseCount",offset:0,options:{one:{value:[{type:0,value:"course"}]},other:{value:[{type:0,value:"courses"}]}}},{type:0,value:" matching your search"}]}}),D=function(e){var t=e.context,r=e.courses,a=e.meta,n=e.className,i=["course-glimpse-list"];return n&&i.push(n),(0,s.jsxs)("div",{className:i.join(" "),children:[a&&(0,s.jsxs)("div",{className:"course-glimpse-list__header",children:[(0,s.jsx)("div",{className:"offscreen","data-testid":"course-glimpse-sr-count","aria-live":"polite","aria-atomic":"true",children:(0,s.jsx)(o.sA,T(T({},x.offscreenCourseCount),{},{values:{courseCount:a.total_count}}))}),(0,s.jsx)("div",{className:"course-glimpse-list__count list__count-description","aria-hidden":"true",children:(0,s.jsx)(o.sA,T(T({},x.courseCount),{},{values:{courseCount:a.total_count,end:a.offset+a.count,start:a.offset+1}}))})]}),(0,s.jsx)("div",{className:"course-glimpse-list__content",children:r.map((function(e){return(0,s.jsx)(R,{context:t,course:e},function(e){return e.product_id?[e.product_id,e.code].join("-"):e.code}(e))}))})]})}},29267:function(e,t,r){r.d(t,{a:function(){return b}}),r(32351),r(48339),r(89327),r(91144),r(3636),r(94204),r(36008),r(12888),r(76911),r(61770),r(52508),r(94711),r(25648),r(45472),r(11021),r(92262),r(71698),r(12710);var o=r(77810),a=r(49306),n=r.n(a),s=r(43346),i=r(14278),c=r(48916),u=r(5903),l=r(64922),d=["className","bodyOpenClassName","overlayClassName","children","hasCloseButton","title"];function p(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,o)}return r}function f(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?p(Object(r),!0).forEach((function(t){g(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):p(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function g(e,t,r){return(t=function(e){var t=function(e,t){if("object"!=m(e)||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var o=r.call(e,"string");if("object"!=m(o))return o;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"==m(t)?t:t+""}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function m(e){return m="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},m(e)}var y=(0,s.YK)({closeDialog:{id:"components.Modal.closeDialog",defaultMessage:[{type:0,value:"Close dialog"}]}}),b=function(e){var t=e.className,r=e.bodyOpenClassName,a=e.overlayClassName,p=e.children,g=e.hasCloseButton,b=void 0===g||g,v=e.title,h=function(e,t){if(null==e)return{};var r,o,a=function(e,t){if(null==e)return{};var r={};for(var o in e)if({}.hasOwnProperty.call(e,o)){if(t.indexOf(o)>=0)continue;r[o]=e[o]}return r}(e,t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);for(o=0;o<n.length;o++)r=n[o],t.indexOf(r)>=0||{}.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}(e,d),O=(0,s.tz)(),_=function(e){var t=e.base,r=e.classes;if(t&&r){if("object"===m(r))return f(f({},r),{},{base:t.concat(" ",r.base)});if("string"==typeof r&&r.trim())return t.concat(" ",r)}return t||r||void 0},j=(0,o.useMemo)((function(){var e=document.getElementById("modal-exclude");if(e)return e;throw new Error("Failed to get #modal-exclude to enable an accessible <ReactModal />.")}),[]),N=["modal__header"];return v&&N.push("modal__header--filled"),(0,l.jsxs)(n(),f(f({appElement:j,className:_({base:"modal",classes:t}),bodyOpenClassName:_({base:"has-opened-modal",classes:r}),overlayClassName:_({base:"modal__overlay",classes:a})},h),{},{children:[(0,l.jsxs)("header",{className:N.join(" "),children:[c.M.isString(v)&&(0,l.jsx)("h2",{children:v}),!c.M.isString(v)&&v,b&&(0,l.jsxs)(i.$n,{"aria-label":O.formatMessage(y.closeDialog),className:"modal__closeButton",onClick:function(e){var t;return null===(t=h.onRequestClose)||void 0===t?void 0:t.call(h,e)},title:O.formatMessage(y.closeDialog),color:"tertiary",size:"small",children:[(0,l.jsx)(u.I,{name:u.f.ROUND_CLOSE}),(0,l.jsx)("span",{className:"offscreen",children:(0,l.jsx)(s.sA,f({},y.closeDialog))})]})]}),p]}))}},74980:function(e,t,r){r.d(t,{W:function(){return m},d:function(){return y}}),r(32351),r(48339),r(89327),r(91144),r(3636),r(89886),r(94204),r(74666),r(61346),r(36008),r(16374),r(12888),r(76911),r(61770),r(52508),r(94711),r(82067),r(67873),r(25648),r(45472),r(11021),r(11548),r(32900),r(37268);var o=r(77810),a=r(43346),n=r(95909),s=r(10847),i=r(64922);function c(e){return c="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},c(e)}function u(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,o)}return r}function l(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?u(Object(r),!0).forEach((function(t){d(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):u(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function d(e,t,r){return(t=function(e){var t=function(e,t){if("object"!=c(e)||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var o=r.call(e,"string");if("object"!=c(o))return o;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"==c(t)?t:t+""}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function p(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=r){var o,a,n,s,i=[],c=!0,u=!1;try{if(n=(r=r.call(e)).next,0===t){if(Object(r)!==r)return;c=!1}else for(;!(c=(o=n.call(r)).done)&&(i.push(o.value),i.length!==t);c=!0);}catch(e){u=!0,a=e}finally{try{if(!c&&null!=r.return&&(s=r.return(),Object(s)!==s))return}finally{if(u)throw a}}return i}}(e,t)||function(e,t){if(e){if("string"==typeof e)return f(e,t);var r={}.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?f(e,t):void 0}}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function f(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,o=Array(t);r<t;r++)o[r]=e[r];return o}var g=(0,a.YK)({currentlyReadingLastPageN:{id:"components.PaginateCourseSearch.currentlyReadingLastPageN",defaultMessage:[{type:0,value:"Currently reading last page "},{type:1,value:"page"}]},currentlyReadingPageN:{id:"components.PaginateCourseSearch.currentlyReadingPageN",defaultMessage:[{type:0,value:"Currently reading page "},{type:1,value:"page"}]},lastPageN:{id:"components.PaginateCourseSearch.lastPageN",defaultMessage:[{type:0,value:"Last page "},{type:1,value:"page"}]},nextPageN:{id:"components.PaginateCourseSearch.nextPageN",defaultMessage:[{type:0,value:"Next page "},{type:1,value:"page"}]},pageN:{id:"components.PaginateCourseSearch.pageN",defaultMessage:[{type:0,value:"Page "},{type:1,value:"page"}]},pagination:{id:"components.PaginateCourseSearch.pagination",defaultMessage:[{type:0,value:"Pagination"}]},previousPageN:{id:"components.PaginateCourseSearch.previousPageN",defaultMessage:[{type:0,value:"Previous page "},{type:1,value:"page"}]}}),m=function(e){var t=e.itemsPerPage,r=void 0===t?10:t,a=(0,o.useMemo)((function(){var e=new URL(window.location.href);return e.searchParams.has("page")?Number(e.searchParams.get("page")):1}),[]),n=p((0,o.useState)(),2),i=n[0],c=n[1],u=p((0,o.useState)(a),2),l=u[0],d=u[1];return{maxPage:i,setMaxPage:c,currentPage:l,setCurrentPage:d,itemsPerPage:r,onPageChange:function(e){(0,s.W2)({behavior:"smooth",top:0}),d(e)},setItemsCount:function(e){c(Math.ceil(e/r))}}},y=function(e){var t=e.onPageChange,r=e.maxPage,c=void 0===r?0:r,u=e.currentPage,d=e.renderPageHref,f=e.updateUrl,m=void 0===f||f,y=(0,a.tz)(),b=p((0,n.W6)(),2)[1];if(c<=1)return null;var v=[1,u-2==3?u-3:-1,u-2,u-1,u,u+1,u+2,u+3===c-1?u+3:-1,c].filter((function(e){return e>0})).filter((function(e){return e<=c})).filter((function(e,t,r){return e!==r[t-1]}));return(0,i.jsx)("div",{className:"pagination","data-testid":"pagination",children:(0,i.jsx)("nav",{"aria-label":y.formatMessage(g.pagination),children:(0,i.jsx)("ul",{className:"pagination__list",children:v.map((function(e,r){return(0,i.jsxs)(o.Fragment,{children:[e>(v[r-1]||0)+1&&(0,i.jsx)("li",{className:"pagination__item pagination__item--placeholder",children:"..."}),e===u?(0,i.jsx)("li",{className:"pagination__item pagination__item--current",children:(0,i.jsxs)("span",{className:"pagination__page-number",children:[(0,i.jsx)("span",{className:"offscreen",children:e===c?(0,i.jsx)(a.sA,l(l({},g.currentlyReadingLastPageN),{},{values:{page:e}})):(0,i.jsx)(a.sA,l(l({},g.currentlyReadingPageN),{},{values:{page:e}}))}),(0,i.jsx)("span",{"aria-hidden":!0,children:1===e?(0,i.jsx)(a.sA,l(l({},g.pageN),{},{values:{page:e}})):e})]})}):(0,i.jsx)("li",{className:"pagination__item",children:(0,i.jsxs)("a",{href:d?d(e):"?page=".concat(e),className:"pagination__page-number",onClick:function(r){if(!r.metaKey&&!r.ctrlKey&&!r.shiftKey&&(r.preventDefault(),t(e),m)){var o=new URL(window.location.href);o.searchParams.set("page",String(e)),b({},"",s.C5.pathname+"?"+o.searchParams.toString())}},children:[(0,i.jsx)("span",{className:"offscreen",children:e===c?(0,i.jsx)(a.sA,l(l({},g.lastPageN),{},{values:{page:e}})):e===u-1?(0,i.jsx)(a.sA,l(l({},g.previousPageN),{},{values:{page:e}})):e===u+1?(0,i.jsx)(a.sA,l(l({},g.nextPageN),{},{values:{page:e}})):(0,i.jsx)(a.sA,l(l({},g.pageN),{},{values:{page:e}}))}),(0,i.jsx)("span",{"aria-hidden":!0,children:1===e?(0,i.jsx)(a.sA,l(l({},g.pageN),{},{values:{page:e}})):e})]})})]},e)}))})})})}},79935:function(e,t,r){r.d(t,{B:function(){return a}}),r(94711),r(45472);var o=r(77810),a=function(e){var t=e.root,r=e.target,a=e.onIntersect,n=e.threshold,s=void 0===n?.99:n,i=e.rootMargin,c=void 0===i?"0px":i,u=e.enabled,l=void 0===u||u;(0,o.useEffect)((function(){if(l&&IntersectionObserver){var e=new IntersectionObserver((function(e){return e.forEach((function(e){return e.isIntersecting&&a()}))}),{root:null==t?void 0:t.current,rootMargin:c,threshold:s}),o=null==r?void 0:r.current;if(o)return e.observe(o),function(){e.unobserve(o)}}}),[r.current,l,a])}},57489:function(e,t,r){r.d(t,{B:function(){return i},M:function(){return c}}),r(32351),r(48339),r(89327),r(94204),r(94711),r(25648),r(11021),r(91144),r(36008),r(12888);var o,a=r(43346);function n(e){return n="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},n(e)}function s(e,t,r){return(t=function(e){var t=function(e,t){if("object"!=n(e)||!e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var o=r.call(e,"string");if("object"!=n(o))return o;throw new TypeError("@@toPrimitive must return a primitive value.")}return String(e)}(e);return"symbol"==n(t)?t:t+""}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var i=function(e){return e.ROOT="/teacher",e.TEACHER_COURSES="/teacher/courses",e.ORGANIZATION="/teacher/organizations/:organizationId",e.ORGANIZATION_CONTRACTS="/teacher/organizations/:organizationId/contracts",e.ORGANIZATION_COURSES="/teacher/organizations/:organizationId/courses",e.ORGANIZATION_PRODUCT="/teacher/organizations/:organizationId/courses/:courseId/products/:courseProductRelationId",e.ORGANIZATION_COURSE_CONTRACTS="/teacher/organizations/:organizationId/courses/:courseId/contracts",e.ORGANIZATION_PRODUCT_CONTRACTS="/teacher/organizations/:organizationId/courses/:courseId/products/:courseProductRelationId/contracts",e.ORGANIZATION_COURSE_PRODUCT_LEARNER_LIST="/teacher/organizations/:organizationId/courses/:courseId/products/:courseProductRelationId/learners",e.ORGANIZATION_COURSE_GENERAL_INFORMATION="/teacher/organizations/:organizationId/courses/:courseId/information",e.COURSE="/teacher/courses/:courseId",e.COURSE_GENERAL_INFORMATION="/teacher/courses/:courseId/information",e.COURSE_PRODUCT="/teacher/courses/:courseId/products/:courseProductRelationId",e.COURSE_PRODUCT_LEARNER_LIST="/teacher/courses/:courseId/products/:courseProductRelationId/learners",e.COURSE_PRODUCT_CONTRACTS="/teacher/courses/:courseId/products/:courseProductRelationId/contracts",e}({}),c=(0,a.YK)((s(s(s(s(s(s(s(s(s(s(o={},i.ROOT,{id:"components.TeacherDashboard.TeacherDashboardRoutes.root.label",defaultMessage:[{type:0,value:"Teacher dashboard"}]}),i.TEACHER_COURSES,{id:"components.TeacherDashboard.TeacherDashboardRoutes.profile.courses.label",defaultMessage:[{type:0,value:"All my courses"}]}),i.ORGANIZATION,{id:"components.TeacherDashboard.TeacherDashboardRoutes.organization.label",defaultMessage:[{type:1,value:"organizationTitle"}]}),i.ORGANIZATION_COURSES,{id:"components.TeacherDashboard.TeacherDashboardRoutes.organization.courses.label",defaultMessage:[{type:0,value:"Courses"}]}),i.ORGANIZATION_CONTRACTS,{id:"components.TeacherDashboard.TeacherDashboardRoutes.organization.contracts.label",defaultMessage:[{type:0,value:"Contracts"}]}),i.ORGANIZATION_COURSE_CONTRACTS,{id:"components.TeacherDashboard.TeacherDashboardRoutes.organization.course.contracts.label",defaultMessage:[{type:0,value:"Contracts"}]}),i.ORGANIZATION_PRODUCT_CONTRACTS,{id:"components.TeacherDashboard.TeacherDashboardRoutes.organization.course.product.contracts.label",defaultMessage:[{type:0,value:"Contracts"}]}),i.ORGANIZATION_COURSE_GENERAL_INFORMATION,{id:"components.TeacherDashboard.TeacherDashboardRoutes.organization.course.generalInformation.label",defaultMessage:[{type:0,value:"General information"}]}),i.ORGANIZATION_PRODUCT,{id:"components.TeacherDashboard.TeacherDashboardRoutes.organization.course.product.label",defaultMessage:[{type:0,value:"General information"}]}),i.ORGANIZATION_COURSE_PRODUCT_LEARNER_LIST,{id:"components.TeacherDashboard.TeacherDashboardRoutes.organization.course.product.learnerList.label",defaultMessage:[{type:0,value:"Learners"}]}),s(s(s(s(s(o,i.COURSE,{id:"components.TeacherDashboard.TeacherDashboardRoutes.course.label",defaultMessage:[{type:1,value:"courseTitle"}]}),i.COURSE_GENERAL_INFORMATION,{id:"components.TeacherDashboard.TeacherDashboardRoutes.generalInformation.label",defaultMessage:[{type:0,value:"General information"}]}),i.COURSE_PRODUCT,{id:"components.TeacherDashboard.TeacherDashboardRoutes.course.product.label",defaultMessage:[{type:0,value:"General information"}]}),i.COURSE_PRODUCT_LEARNER_LIST,{id:"components.TeacherDashboard.TeacherDashboardRoutes.course.product.learnerList.label",defaultMessage:[{type:0,value:"Learners"}]}),i.COURSE_PRODUCT_CONTRACTS,{id:"components.TeacherDashboard.TeacherDashboardRoutes.course.product.contracts.label",defaultMessage:[{type:0,value:"Contracts"}]})))}}]);
//# sourceMappingURL=48631.6b55ea25441038791018.index.js.map