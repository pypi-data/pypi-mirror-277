(this.webpackJsonpui_v2=this.webpackJsonpui_v2||[]).push([[12],{1311:function(e,t,n){"use strict";var a=n(7),i=n(0),c=n.n(i),r=n(1);t.a=function(e){var t=e.children,n=c.a.useRef(null),i=c.a.useState(!1),o=Object(a.a)(i,2),s=o[0],l=o[1];return c.a.useEffect((function(){if(s){var e=n.current.parentNode.parentNode.parentNode;"notes-toolbar-popover"!==e.id&&(e.id="notes-toolbar-popover")}else l(!0)}),[s]),Object(r.jsx)("div",{ref:n,children:t})}},1312:function(e,t,n){},1315:function(e,t,n){"use strict";var a=n(0),i=n.n(a),c=n(72),r=n(5),o=n(144),s=n(353),l=n(622),d=n(386),u=n(222),m=n(73),v=(n(987),n(1));function j(e){return Object(v.jsxs)("div",{className:"FeedItem",children:[Object(v.jsxs)("div",{className:"FeedItem__title",children:[Object(v.jsx)(r.f,{name:"calendar",fontSize:10,box:!0}),Object(v.jsx)(r.n,{tint:50,size:10,weight:700,children:e.date.split("_").join(" ")})]}),Object(v.jsx)("div",{className:"FeedItem__content",children:e.data.map((function(e){return Object(v.jsxs)("div",{className:"FeedItem__content__item",children:[Object(v.jsxs)("div",{className:"FeedItem__content__item__leftBox",children:[Object(v.jsx)(r.n,{tint:50,size:12,className:"FeedItem__content__item__leftBox__date",children:e.date}),Object(v.jsx)(r.n,{size:12,tint:100,className:"FeedItem__content__item__leftBox__label",children:"Started a run:"}),Object(v.jsx)(s.a,{title:e.active?"In Progress":"Finished",children:Object(v.jsx)("div",{className:"FeedItem__content__item__leftBox__indicatorBox",children:Object(v.jsx)(d.a,{className:"Table__status_indicator",status:e.active?"success":"alert"})})})]}),Object(v.jsxs)("div",{className:"FeedItem__content__item__itemBox",children:[Object(v.jsx)(u.a,{experimentName:e.experiment,experimentId:e.experimentId}),Object(v.jsx)(r.n,{size:10,children:"/"}),Object(v.jsx)(s.a,{title:e.name,children:Object(v.jsx)("div",{className:"FeedItem__content__item__itemBox__runName",children:Object(v.jsx)(l.a,{to:m.a.Run_Detail.replace(":runHash",e.hash),component:o.b,children:e.name})})})]})]},e.name)}))})]})}var f=i.a.memo(j);n(988);function b(e){var t=e.data,n=e.loadMore,a=e.isLoading,i=e.totalRunsCount,o=void 0===i?0:i,s=e.fetchedCount,l=void 0===s?0:s,d=e.archivedRunsCount,u=void 0===d?0:d;return o&&o!==u?Object(v.jsxs)("div",{className:"ContributionsFeed",children:[Object(v.jsx)(r.n,{size:14,component:"h3",tint:100,weight:700,children:"Activity"}),a&&c.a.isEmpty(t)?Object(v.jsx)("div",{className:"flex fac fjc",children:Object(v.jsx)(r.l,{size:"24px"})}):Object(v.jsxs)(v.Fragment,{children:[Object.keys(t).map((function(e){return Object(v.jsxs)("div",{className:"ContributionsFeed__content",children:[Object(v.jsx)(r.n,{className:"ContributionsFeed__content-title",component:"h3",tint:100,weight:700,children:e.split("_").join(" ")}),Object.keys(t[e]).map((function(n){return Object(v.jsx)(f,{date:n,data:t[e][n]},n)}))]},e)})),l<o-u?Object(v.jsx)(r.c,{variant:"outlined",fullWidth:!0,size:"small",onClick:a?void 0:n,children:a?"Loading...":"Show more activity"}):null]})]}):null}var p=i.a.memo(b);t.a=p},1318:function(e,t,n){"use strict";var a=n(0),i=n(95),c=n(18),r=n.n(c),o=n(5);var s=function(e,t){var n=null===e||void 0===e?void 0:e.substring(1).split("");3===n.length&&(n=[n[0],n[0],n[1],n[1],n[2],n[2]]);var a=+("0x"+n.join(""));return"rgba("+[a>>16&255,a>>8&255,255&a].join(",")+","+t||!1},l=(n(989),n(1));function d(e){var t=e.label,n=e.badge,c=void 0===n?{value:""}:n,d=e.count,u=e.icon,m=e.iconBgColor,v=void 0===m?"#000000":m,j=e.cardBgColor,f=void 0===j?s(v,.1):j,b=e.onMouseOver,p=e.onMouseLeave,h=e.navLink,x=e.highlighted,_=e.outlined,O=void 0!==_&&_,g=e.isLoading,N=void 0!==g&&g,C=Object(i.h)(),y=a.useCallback((function(e){"function"===typeof b&&b(e,"card")}),[b]),E={card:{borderColor:O?v:"transparent",backgroundColor:x?v:f},iconWrapper:{backgroundColor:x?"#fff":v},iconColor:x?v:"#fff",label:x?{color:"#fff"}:{},count:x?{color:"#fff"}:{}};return Object(l.jsxs)("div",{onClick:function(){return h&&C.push(h)},onMouseLeave:p,onMouseOver:function(){return y(t)},className:r()("StatisticsCard",{highlighted:x}),style:E.card,children:[(null===c||void 0===c?void 0:c.value)&&Object(l.jsx)(o.n,{component:"p",className:"StatisticsCard__badge",weight:600,size:8,style:c.style,children:c.value}),u&&Object(l.jsx)("div",{className:"StatisticsCard__iconWrapper",style:E.iconWrapper,children:Object(l.jsx)(o.f,{name:u,color:E.iconColor})}),Object(l.jsxs)("div",{className:"StatisticsCard__info",children:[Object(l.jsx)(o.n,{className:"StatisticsCard__info__label",size:10,weight:600,style:E.label,children:t}),Object(l.jsx)(o.n,{className:"StatisticsCard__info__count",size:16,weight:600,style:E.count,children:Object(l.jsx)("span",{children:N?"--":d})})]})]})}d.displayName="StatisticsCard";var u=a.memo(d);t.a=u},1321:function(e,t,n){"use strict";var a=n(0),i=n(976),c=n(72),r=n(977),o=n(698),s=n(707),l=n(5),d=n(11),u=(n(1312),n(1));function m(e){var t=e.title,n=void 0===t?"Run Properties":t,a=e.defaultName,m=e.defaultDescription,v=e.onSave,j=Object(r.a)({initialValues:{name:null!==a&&void 0!==a?a:"",description:null!==m&&void 0!==m?m:""},onSubmit:c.a.noop,validationSchema:i.a({name:i.b().required("Name is a required field")})}),f=j.values,b=j.errors,p=j.touched,h=j.setFieldValue,x=j.setFieldTouched;function _(e,t){var n;h(t,null===e||void 0===e||null===(n=e.target)||void 0===n?void 0:n.value,!0).then((function(){x(t,!0)}))}return Object(u.jsx)(d.a,{children:Object(u.jsxs)("div",{className:"NameAndDescriptionCard",children:[Object(u.jsxs)("div",{className:"NameAndDescriptionCard__header",children:[Object(u.jsx)(l.n,{component:"h4",weight:600,size:14,tint:100,children:n}),Object(u.jsx)(o.a,{onClick:function(){v(f.name,f.description)},disabled:!c.a.isEmpty(b)||f.name===a&&f.description===m,variant:"contained",color:"primary",className:"NameAndDescriptionCard__saveBtn",children:"Save"})]}),Object(u.jsxs)("div",{className:"NameAndDescriptionCard__content",children:[Object(u.jsx)("div",{className:"NameAndDescriptionCard__content__nameBox",children:Object(u.jsx)(s.a,{variant:"outlined",className:"TextField__OutLined__Medium NameAndDescriptionCard__content__nameBox__nameInput",value:f.name,onChange:function(e){return _(e,"name")},error:!(!p.name||!b.name),helperText:p.name&&b.name,label:"Name"})}),Object(u.jsx)("div",{className:"NameAndDescriptionCard__content__descriptionBox",children:Object(u.jsx)(s.a,{variant:"outlined",multiline:!0,label:"Description",type:"textarea",className:"NameAndDescriptionCard__content__descriptionBox__descriptionInput",value:f.description,onChange:function(e){return _(e,"description")},error:!(!p.description||!b.description),helperText:p.description&&b.description})})]})]})})}var v=Object(a.memo)(m);t.a=v},1323:function(e,t,n){"use strict";var a=n(2),i=n(0),c=n(18),r=n.n(c),o=n(353),s=(n(990),n(1));function l(e){var t=e.data,n=void 0===t?[]:t,c=e.width,l=void 0===c?"100%":c,d=e.height,u=void 0===d?8:d,m=e.onMouseOver,v=e.onMouseLeave,j=i.useCallback((function(e){"function"===typeof m&&m(e,"bar")}),[m]),f=i.useMemo((function(){for(var e=[],t=0;t<n.length;t++){var a,i,c=n[t],r=(null===(a=e[t-1])||void 0===a?void 0:a.left)||0,o=(null===(i=n[t-1])||void 0===i?void 0:i.percent)||0,s={width:"".concat(c.percent.toFixed(2),"%"),left:0===t?0:r+o,backgroundColor:c.color};e.push(s)}return e}),[n]);return Object(s.jsx)("div",{className:"StatisticsBar",style:{width:l,height:u},children:Object.values(n).map((function(e,t){var n=e.percent,i=e.color,c=e.label,l=void 0===c?"":c,d=e.highlighted;return n?Object(s.jsx)(o.a,{title:l,children:Object(s.jsx)("div",{className:r()("StatisticsBar__item",{highlighted:d}),style:Object(a.a)(Object(a.a)({},f[t]),{},{left:f[t].left+"%"}),onMouseLeave:v,onMouseOver:function(){return j(l)}})},"".concat(l,"-").concat(i)):null}))})}l.displayName="StatisticsBar";var d=i.memo(l);t.a=d},1324:function(e,t,n){"use strict";var a=n(7),i=n(0),c=n.n(i),r=n(95),o=n(736),s=n(5),l=n(1);var d=function(e){var t=e.when,n=e.message,i=void 0===n?"Changes you made may not be saved.":n,d=e.confirmBtnText,u=void 0===d?"Leave":d,m=c.a.useState(!1),v=Object(a.a)(m,2),j=v[0],f=v[1],b=c.a.useState(""),p=Object(a.a)(b,2),h=p[0],x=p[1],_=c.a.useState(!1),O=Object(a.a)(_,2),g=O[0],N=O[1],C=Object(r.h)();function y(e){return t?(null===e||void 0===e||e.preventDefault(),e&&(e.returnValue="Your changes is not saved. Do you still want to leave"),""):void 0}function E(){f(!1)}return c.a.useEffect((function(){return g&&(C.push(h),N(!1)),window.addEventListener("beforeunload",y),function(){window.removeEventListener("beforeunload",y)}}),[g,t]),Object(l.jsxs)(l.Fragment,{children:[Object(l.jsx)(r.a,{when:t,message:function(e){return!!g||(function(e){f(!0),x(e)}(e.pathname),!1)}}),Object(l.jsx)(o.a,{open:j,onCancel:E,onSubmit:function(){E(),h&&N(!0)},text:i,icon:Object(l.jsx)(s.f,{name:"warning-contained"}),statusType:"warning",confirmBtnText:u,title:"Are you sure"})]})};t.a=d},1360:function(e,t,n){"use strict";n.d(t,"b",(function(){return d.a}));var a=n(0),i=n.n(a),c=n(985),r=n(5),o=n(11),s=n(17),l=n(14),d=n(953);var u=function(e){var t=i.a.useRef(d.a).current,n=t.experimentContributionsState((function(e){return e}));return i.a.useEffect((function(){n.data||t.fetchExperimentContributions(e)}),[n.data]),i.a.useEffect((function(){return function(){t.destroy()}}),[]),{experimentContributionsState:n}},m=(n(1562),n(1));function v(e){var t,n,a=e.experimentId,i=e.experimentName,d=u(a).experimentContributionsState;var v=new Date;return Object(m.jsx)(o.a,{children:Object(m.jsxs)("div",{className:"ExperimentContributions",children:[Object(m.jsx)(r.n,{component:"h2",size:18,weight:600,tint:100,children:"Contributions"}),Object(m.jsx)("div",{className:"ExperimentContributions__HeatMap",children:Object(m.jsx)(c.a,{startDate:function(e,t){var n=new Date(e);return n.setDate(n.getDate()+t),n}(v,-300),endDate:v,onCellClick:function(){Object(l.b)(s.a.dashboard.activityCellClick)},additionalQuery:' and run.experiment == "'.concat(i,'"'),data:Object.keys(null!==(t=null===(n=d.data)||void 0===n?void 0:n.activity_map)&&void 0!==t?t:{}).map((function(e){var t;return[new Date(e),null===(t=d.data)||void 0===t?void 0:t.activity_map[e]]}))})})]})})}var j=i.a.memo(v);t.a=j},1562:function(e,t,n){},1563:function(e,t,n){},1564:function(e,t,n){},1565:function(e,t,n){},1566:function(e,t,n){},1567:function(e,t,n){},1568:function(e,t,n){},1569:function(e,t,n){},1587:function(e,t,n){"use strict";n.r(t);var a=n(7),i=n(0),c=n.n(i),r=n(17),o=n(14),s=n(1360),l=n(18),d=n.n(l),u=n(95),m=n(144),v=n(5),j=(n(1563),n(1));var f=function(e){var t,n=e.sidebarRef,i=e.overviewSectionRef,r=e.setContainerHeight,o=e.overviewSectionContentRef,s=e.description,l=Object(u.k)().url,f=c.a.useRef(null),b=c.a.useState(!1),p=Object(a.a)(b,2),h=p[0],x=p[1],_=c.a.useState(0),O=Object(a.a)(_,2),g=O[0],N=O[1];return c.a.useEffect((function(){var e;N(null===f||void 0===f||null===(e=f.current)||void 0===e?void 0:e.offsetHeight)}),[null===f||void 0===f||null===(t=f.current)||void 0===t?void 0:t.offsetHeight,h]),c.a.useEffect((function(){var e,t,a;(null===o||void 0===o||null===(e=o.current)||void 0===e?void 0:e.offsetHeight)>(null===n||void 0===n||null===(t=n.current)||void 0===t?void 0:t.childNodes[0].offsetHeight)?r("100%"):r((null===n||void 0===n||null===(a=n.current)||void 0===a?void 0:a.childNodes[0].offsetHeight)+40)}),[g]),Object(j.jsx)("div",{className:"ExperimentOverviewSidebar ScrollBar__hidden",ref:n,onScroll:function(e){var t;null===i||void 0===i||null===(t=i.current)||void 0===t||t.scrollTo(0,e.target.scrollTop)},children:Object(j.jsx)("div",{className:"ExperimentOverviewSidebar__wrapper",children:Object(j.jsxs)("div",{className:"ExperimentOverviewSidebar__section ExperimentOverviewSidebar__section__descriptionBox",children:[Object(j.jsxs)("div",{className:"ExperimentOverviewSidebar__section__descriptionBox__header",children:[Object(j.jsx)(v.n,{weight:600,size:18,tint:100,component:"h3",children:"Description"}),Object(j.jsx)(m.c,{to:"".concat(l.split("/").slice(0,-1).join("/"),"/settings"),children:Object(j.jsx)(v.c,{withOnlyIcon:!0,size:"small",color:"secondary",children:Object(j.jsx)(v.f,{name:"edit"})})})]}),Object(j.jsx)("div",{className:d()("ExperimentOverviewSidebar__section__descriptionBox__description",{showAll:h},{hasMore:g>=72&&!h}),ref:f,children:Object(j.jsx)(v.n,{tint:70,children:s||"No description"})}),g>=72&&Object(j.jsx)("div",{className:"ExperimentOverviewSidebar__section__descriptionBox__seeMoreButtonBox",onClick:function(){x(!h)},children:Object(j.jsx)(v.n,{size:12,weight:600,children:h?"See less":"See more"})})]})})})},b=n(1318),p=n(1323),h=n(20),x=n(953);n(1564);function _(e){var t=e.experimentName,n=i.useState({source:"",id:""}),c=Object(a.a)(n,2),r=c[0],o=c[1],s=i.useRef(x.a).current.experimentContributionsState((function(e){return e})),l=i.useMemo((function(){var e,t;return{totalRunsCount:(null===(e=s.data)||void 0===e?void 0:e.num_runs)||0,archivedRuns:(null===(t=s.data)||void 0===t?void 0:t.num_archived_runs)||0}}),[s]),d=l.totalRunsCount,u=l.archivedRuns,m=i.useMemo((function(){return{runs:{label:"runs",icon:"runs",count:d-u,iconBgColor:"#1473E6",navLink:"/runs?select=".concat(Object(h.c)({query:"run.experiment == '".concat(t,"'")}))},archived:{label:"archived",icon:"archive",count:u,iconBgColor:"#606986",navLink:"/runs?select=".concat(Object(h.c)({query:"run.archived == True and run.experiment == '".concat(t,"'")}))}}}),[d,u,t]),f=i.useMemo((function(){var e,n;return{active:{label:"Active",count:(null===(e=s.data)||void 0===e?void 0:e.num_active_runs)||0,icon:"runs",iconBgColor:"#18AB6D",navLink:"/runs?select=".concat(Object(h.c)({query:"run.active == True and run.experiment == '".concat(t,"'")}))},finished:{label:"Finished",icon:"runs",count:d-((null===(n=s.data)||void 0===n?void 0:n.num_active_runs)||0),iconBgColor:"#83899e",navLink:"/runs?select=".concat(Object(h.c)({query:"run.active == False and run.experiment == '".concat(t,"'")}))}}}),[s,t,d]),_=i.useMemo((function(){return Object.values(f).map((function(e){var t=e.label,n=e.iconBgColor,a=void 0===n?"#000":n,i=e.count;return{highlighted:r.id===t,label:t,color:a,percent:0===d?0:i/d*100}}))}),[f,d,r]),O=i.useCallback((function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"";o({source:t,id:e})}),[]),g=i.useCallback((function(){o({source:"",id:""})}),[]);return Object(j.jsxs)("div",{className:"ExperimentStatistics",children:[Object(j.jsxs)(v.n,{className:"ExperimentStatistics__totalRuns",component:"p",tint:100,weight:700,size:14,children:["Total runs: ",d]}),Object(j.jsx)("div",{className:"ExperimentStatistics__cards",children:Object.values(m).map((function(e){var t=e.label,n=e.icon,a=e.count,i=e.iconBgColor,c=e.navLink;return Object(j.jsx)(b.a,{label:t,icon:n,count:a,navLink:c,iconBgColor:i,onMouseOver:O,onMouseLeave:g,highlighted:!!c&&r.id===t,isLoading:s.loading},t)}))}),Object(j.jsx)(v.n,{className:"ExperimentStatistics__trackedSequences",component:"p",tint:100,weight:700,size:14,children:"Runs status"}),Object(j.jsx)("div",{className:"ExperimentStatistics__cards",children:Object.values(f).map((function(e){var t=e.label,n=e.icon,a=e.count,i=e.iconBgColor,c=e.navLink;return Object(j.jsx)(b.a,{label:t,icon:n,count:a,navLink:c,iconBgColor:i,onMouseOver:O,onMouseLeave:g,highlighted:!!c&&"card"===r.source&&r.id===t,outlined:r.id===t,isLoading:s.loading},t)}))}),Object(j.jsx)("div",{className:"ExperimentStatistics__bar",children:Object(j.jsx)(p.a,{data:_,onMouseOver:O,onMouseLeave:g})})]})}_.displayName="ExperimentStatistics";var O=i.memo(_),g=n(2),N=n(1315),C=n(6),y=n(65),E=n.n(y),w=n(72),S=n(76),R=n(8),k=n.n(R),M=n(27),D=n(847),T=n(752);var B=function(){var e=Object(D.b)().call,t=Object(T.a)(function(){var t=Object(M.a)(k.a.mark((function t(n,a){return k.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,e(n,a);case 2:return t.abrupt("return",t.sent);case 3:case"end":return t.stop()}}),t)})));return function(e,n){return t.apply(this,arguments)}}()),n=t.fetchData;return{fetchExperimentContributionsFeed:function(e,t){return n({experimentId:e,queryParams:t})},experimentContributionsFeedState:t.state,destroy:t.destroy}}();var L=function(e,t){var n,i,r=c.a.useState([]),o=Object(a.a)(r,2),s=o[0],l=o[1],d=c.a.useRef(B).current,u=d.experimentContributionsFeedState((function(e){return e})),m=c.a.useRef(x.a).current.experimentContributionsState((function(e){return e}));c.a.useEffect((function(){return w.a.isEmpty(u.data)&&d.fetchExperimentContributionsFeed(e,{limit:25}),function(){return d.destroy()}}),[]),c.a.useEffect((function(){var e;if(null===(e=u.data)||void 0===e?void 0:e.length){var t=[].concat(Object(C.a)(s),Object(C.a)(u.data));l(t)}}),[u.data]);var v=c.a.useMemo((function(){var n={};s.length&&((null===s||void 0===s?void 0:s.reduce((function(e,t){var n=E()(1e3*t.creation_time).format(S.h);return e.includes(n)||t.archived||e.push(n),e}),[])).forEach((function(e){n[e]={}})),null===s||void 0===s||s.forEach((function(a){if(!a.archived){var i,c,r=E()(1e3*a.creation_time).format(S.h),o=E()(1e3*a.creation_time).format(S.g),s={name:a.name,date:E()(1e3*a.creation_time).format(S.i),hash:a.run_id,creation_time:a.creation_time,experiment:t,experimentId:e};(null===(i=n[r])||void 0===i||null===(c=i[o])||void 0===c?void 0:c.length)?n[r][o].push(s):n[r][o]=[s]}})));return n}),[s,t,e]);return{isLoading:u.loading,data:v,totalRunsCount:null===(n=m.data)||void 0===n?void 0:n.num_runs,archivedRunsCount:null===(i=m.data)||void 0===i?void 0:i.num_archived_runs,fetchedCount:s.length,loadMore:function(){u.data&&!u.loading&&d.fetchExperimentContributionsFeed(e,{limit:25,offset:s[s.length-1].run_id})}}};function I(e){var t=e.experimentId,n=e.experimentName,a=L(t,n);return Object(j.jsx)(N.a,Object(g.a)({},a))}var F=c.a.memo(I);n(1565);var H=function(e){var t=c.a.useRef(null),n=c.a.useRef(null),i=c.a.useRef(null),l=c.a.useState(0),d=Object(a.a)(l,2),u=d[0],m=d[1];return c.a.useEffect((function(){o.a(r.a.experiment.tabs.overview.tabView)}),[]),Object(j.jsxs)("div",{className:"ExperimentOverviewTab",ref:n,onScroll:function(e){var n;null===t||void 0===t||null===(n=t.current)||void 0===n||n.scrollTo(0,e.target.scrollTop)},children:[Object(j.jsx)("div",{className:"ExperimentOverviewTab__content",ref:i,style:{height:u},children:Object(j.jsxs)("div",{className:"ExperimentOverviewTab__content__section",children:[Object(j.jsx)(O,{experimentName:e.experimentName}),Object(j.jsx)(s.a,{experimentId:e.experimentId,experimentName:e.experimentName}),Object(j.jsx)(F,{experimentId:e.experimentId,experimentName:e.experimentName})]})}),Object(j.jsx)(f,{sidebarRef:t,overviewSectionRef:n,setContainerHeight:m,overviewSectionContentRef:i,description:e.description})]})};t.default=H},1590:function(e,t,n){"use strict";n.r(t),n.d(t,"experimentRunsEngine",(function(){return z}));var a=n(0),i=n.n(a),c=n(11),r=n(72),o=n(18),s=n.n(o),l=n(623),d=n(5),u=n(377),m=n(15),v=n(382),j=n(25),f=(n(1566),n(1));var b=function(e){var t=e.experimentName,n=e.experimentId,a=A(t,n),i=a.tableRef,c=a.tableColumns,o=a.tableData,b=a.loading,p=a.selectedRows,h=a.comparisonQuery,x=a.onRowSelect,_=a.loadMore,O=a.isInfiniteLoading,g=a.totalRunsCount;return Object(f.jsxs)("div",{className:"ExperimentRunsTable",children:[Object(f.jsxs)("div",{className:"ExperimentRunsTable__header",children:[Object(f.jsxs)("div",{className:"ExperimentRunsTable__header__titleBox",children:[Object(f.jsx)(d.n,{className:"ExperimentRunsTable__header__titleBox__title",component:"h3",size:14,weight:700,tint:100,children:r.a.isEmpty(p)?"Experiment Runs":"Selected Runs (".concat(Object.values(p).length,")")}),r.a.isEmpty(p)?b?Object(f.jsx)(l.a,{variant:"rect",height:17,width:50}):Object(f.jsx)(d.n,{component:"h3",size:14,weight:700,tint:100,children:r.a.isEmpty(o)?"(0)":" (".concat(null===o||void 0===o?void 0:o.length,"/").concat(g,")")}):null]}),(null===o||void 0===o?void 0:o.length)>0?Object(f.jsx)("div",{className:"ExperimentRunsTable__header__comparisonPopover",children:Object(f.jsx)(v.a,{appName:"experiment",query:h,disabled:0===Object.keys(p).length})}):null]}),Object(f.jsxs)("div",{className:s()("ExperimentRunsTable__table",{"ExperimentRunsTable__table--loading":b,"ExperimentRunsTable__table--empty":0===o.length}),children:[r.a.isEmpty(o)&&b?Object(f.jsx)(d.l,{}):Object(f.jsx)(u.a,{custom:!0,allowInfiniteLoading:!0,isInfiniteLoading:!1,showRowClickBehaviour:!1,infiniteLoadHandler:_,showResizeContainerActionBar:!1,ref:i,data:o,columns:c,appName:j.b.RUNS,multiSelect:!0,topHeader:!0,noColumnActions:!0,hideHeaderActions:!0,isLoading:!1,height:"100%",rowHeight:m.e.sm,illustrationConfig:{size:"large",title:"No experiment runs"},selectedRows:p,onRowSelect:x}),O&&Object(f.jsx)("div",{className:"Infinite_Loader",children:Object(f.jsx)(d.l,{})})]})]})},p=n(2),h=n(4),x=n(6),_=n(7),O=n(65),g=n.n(O),N=n(228),C=n(76),y=n(1360),E=n(87),w=n(97),S=n(62),R=n(93),k=n(32),M=n(145),D=n(20),T=n(8),B=n.n(T),L=n(27),I=n(378),F=n(752),H=n(146);var z=function(){var e=Object(I.e)().call,t=Object(F.a)(function(){var t=Object(L.a)(B.a.mark((function t(n){return B.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.t0=H.d,t.next=3,e(n);case 3:return t.t1=t.sent,t.abrupt("return",(0,t.t0)(t.t1));case 5:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}()),n=t.fetchData;return{fetchExperimentRuns:function(e){return n(e)},experimentRunsState:t.state,destroy:t.destroy}}();var A=function(e,t){var n,a,c,o,s=i.a.useRef(null),l=i.a.useRef(null),u=i.a.useState([]),m=Object(_.a)(u,2),v=m[0],j=m[1],b=i.a.useState(!1),O=Object(_.a)(b,2),T=O[0],B=O[1],L=i.a.useRef(z).current,I=i.a.useRef(y.b).current,F=I.experimentContributionsState((function(e){return e})),H=L.experimentRunsState((function(e){return e})),A=i.a.useState({}),P=Object(_.a)(A,2),q=P[0],J=P[1],V=i.a.useState(""),W=Object(_.a)(V,2),Y=W[0],Q=W[1];i.a.useEffect((function(){return r.a.isEmpty(H.data)&&L.fetchExperimentRuns({limit:50,exclude_params:!0,q:"run.experiment == '".concat(e,"'")}),function(){L.destroy(),I.destroy()}}),[]),i.a.useEffect((function(){r.a.isEmpty(F.data)&&I.fetchExperimentContributions(t)}),[F.data]),i.a.useEffect((function(){H.data&&L.destroy(),F.data&&I.destroy()}),[t]),i.a.useEffect((function(){var e;if(null===(e=H.data)||void 0===e?void 0:e.length){var t=[].concat(Object(x.a)(v),Object(x.a)(H.data));j(t),l.current=t}}),[H.data]);var U=i.a.useMemo((function(){if(v){var e=[],t=[],n={};return v.forEach((function(a){var i=a.hash;a.traces.metric.forEach((function(a){var c=Object(E.a)(a.name,a.context);if(n.hasOwnProperty(c))n[c][i]=[a.values.last_step,a.values.last];else{n[c]=Object(h.a)({},i,[a.values.last_step,a.values.last]);var r=Object(w.a)(a.context),o=Object(S.a)(a.name),s={key:c,content:Object(f.jsx)(d.b,{monospace:!0,size:"xSmall",label:""===r?"Empty context":r}),topHeader:o?Object(R.a)(a.name):a.name,name:a.name,context:r,isSystem:o};o?t.push(s):e.push(s)}}))})),{columns:r.a.orderBy(e,["name","context"],["asc","asc"]).concat(r.a.orderBy(t,["name","context"],["asc","asc"])),values:n}}return{columns:[],values:[]}}),[v]),K=i.a.useMemo((function(){return v?v.map((function(e,t){var n=e.props,a=e.hash,i=Object(D.c)({hash:a}),c={key:i,selectKey:i,index:t,run:{content:Object(f.jsx)(N.a,{run:n.name,runHash:a,active:n.active})},date:g()(1e3*n.creation_time).format(C.f),duration:Object(M.a)(1e3*n.creation_time,n.end_time?1e3*n.end_time:Date.now())};return U.columns.forEach((function(e){var t,n=null!==(t=U.values[e.key][a])&&void 0!==t?t:[null,null],i=Object(_.a)(n,2),r=i[0],o=i[1];c[e.key]={content:null===r?"--":e.isSystem?Object(k.a)(o):"step: ".concat(null!==r&&void 0!==r?r:"-"," / value: ").concat(Object(k.a)(o))}})),c})):[]}),[v,U]),G=i.a.useMemo((function(){return[{key:"run",content:Object(f.jsx)("span",{children:"Name"}),topHeader:"Run",pin:"left"},{key:"date",content:Object(f.jsx)("span",{children:"Date"}),topHeader:"Run"},{key:"duration",content:Object(f.jsx)("span",{children:"Duration"}),topHeader:"Run"}].concat(U.columns)}),[U]),X=i.a.useCallback((function(t){var n=t.actionType,a=t.data,i=Object(p.a)({},q);switch(n){case"single":q[a.key]?i=r.a.omit(q,a.key):i[a.key]=!0;break;case"selectAll":Array.isArray(a)?a.forEach((function(e){q[e.key]||(i[e.key]=!0)})):Object.values(a).reduce((function(e,t){return e.concat(t.items)}),[]).forEach((function(e){q[e.selectKey]||(i[e.selectKey]=!0)}));break;case"removeAll":Array.isArray(a)&&(i={})}J(i),Q("run.hash in [".concat(Object.keys(i).map((function(e){return'"'.concat(JSON.parse(Object(D.b)(e)).hash,'"')})).join(", "),'] and run.experiment == "').concat(e,'"'))}),[q,K]);return i.a.useEffect((function(){var e;null===(e=s.current)||void 0===e||e.updateData({newData:K,newColumns:G})}),[K,G]),{data:v,tableData:K,tableColumns:G,tableRef:s,loading:H.loading,isInfiniteLoading:T,selectedRows:q,comparisonQuery:Y,onRowSelect:X,loadMore:function(){var t;H.data&&!H.loading&&(B(!0),L.fetchExperimentRuns({limit:50,exclude_params:!0,offset:null===(t=l.current[l.current.length-1])||void 0===t?void 0:t.hash,q:"run.experiment == '".concat(e,"'")}).finally((function(){return B(!1)})))},totalRunsCount:(null!==(n=null===F||void 0===F||null===(a=F.data)||void 0===a?void 0:a.num_runs)&&void 0!==n?n:0)-(null!==(c=null===F||void 0===F||null===(o=F.data)||void 0===o?void 0:o.num_archived_runs)&&void 0!==c?c:0)}},P=b;n(1567);function q(e){var t=e.experimentName,n=e.experimentId;return Object(f.jsx)(c.a,{children:Object(f.jsx)("div",{className:"ExperimentRunsTab",children:Object(f.jsx)("div",{className:"ExperimentRunsTab__content",children:Object(f.jsx)(P,{experimentName:t,experimentId:n})})})})}var J=Object(a.memo)(q);t.default=J},1593:function(e,t,n){"use strict";n.r(t),n.d(t,"experimentNotesEngine",(function(){return C}));var a=n(2),i=n(7),c=n(0),r=n.n(c),o=n(65),s=n.n(o),l=n(974),d=n.n(l),u=n(18),m=n.n(u),v=n(353),j=n(5),f=n(1324),b=n(76),p=n(29),h=n(17),x=n(1311),_=n(14),O=n(1317),g=n(847),N=n(752);var C=function(){var e=Object(N.a)((function(e){return Object(g.e)(e)})),t=e.fetchData,n=e.state,i=e.destroy;return{fetchExperimentNote:function(e){return t(e)},createExperimentNote:function(e,t){return Object(g.a)(e,{content:t}).then((function(e){n.setState((function(n){return Object(a.a)(Object(a.a)({},n),{},{data:[Object(a.a)({content:t},e)]})})),O.b.onNotificationAdd({id:Date.now(),messages:["Note successfully created"],severity:"success"})})).catch((function(e){return O.b.onNotificationAdd({id:Date.now(),messages:[e.message||"Something went wrong"],severity:"error"})}))},updateExperimentNote:function(e,t,i){return Object(g.h)(e,t,{content:i}).then((function(e){n.setState((function(t){return Object(a.a)(Object(a.a)({},t),{},{data:[Object(a.a)(Object(a.a)({},t.data[0]),{},{updated_at:e.updated_at})]})})),O.b.onNotificationAdd({id:Date.now(),messages:["Note successfully updated"],severity:"success"})})).catch((function(e){O.b.onNotificationAdd({id:Date.now(),messages:[e.message||"Something went wrong"],severity:"error"})}))},experimentNoteState:n,destroy:i}}();var y=function(e){var t,n=r.a.useRef(C).current,a=n.experimentNoteState((function(e){return e}));return r.a.useEffect((function(){var t;(null===a||void 0===a||null===(t=a.data)||void 0===t?void 0:t[0])||n.fetchExperimentNote(e),(null===a||void 0===a?void 0:a.data)&&n.destroy()}),[e]),r.a.useEffect((function(){return function(){return n.destroy()}}),[]),{noteData:null===a||void 0===a||null===(t=a.data)||void 0===t?void 0:t[0],isLoading:a.loading,onNoteCreate:function(t){return n.createExperimentNote(e,t.content)},onNoteUpdate:function(t){var i,c;return n.updateExperimentNote(e,"".concat(null===a||void 0===a||null===(i=a.data)||void 0===i||null===(c=i[0])||void 0===c?void 0:c.id),t.content)}}},E=(n(1568),n(1));function w(e){var t,n=y(e.experimentId),c=n.isLoading,o=n.noteData,l=n.onNoteCreate,u=n.onNoteUpdate,O=r.a.useState(""),g=Object(i.a)(O,2),N=g[0],C=g[1],w=r.a.useState(!0),S=Object(i.a)(w,2),R=S[0],k=S[1],M=r.a.useState(null),D=Object(i.a)(M,2),T=D[0],B=D[1],L=r.a.useRef(null);r.a.useEffect((function(){var e;L.current&&(C((null===o||void 0===o?void 0:o.id)?null===o||void 0===o?void 0:o.content:""),B(Object(a.a)(Object(a.a)({},null===(e=L.current)||void 0===e?void 0:e.theme()),p.c)))}),[o]);var I=r.a.useCallback((function(){k(!0),(null===o||void 0===o?void 0:o.id)?u({content:L.current.value()}).catch((function(){return k(!1)})):l({content:L.current.value()}).catch((function(){return k(!1)}))}),[null===o||void 0===o?void 0:o.id,e.experimentId]),F=r.a.useCallback((function(e){var t=N===e();R!==t&&k(t)}),[R,N]);return r.a.useEffect((function(){_.a(h.a.experiment.tabs.notes.tabView)}),[]),Object(E.jsxs)("section",{className:"ExperimentNotesTab",children:[Object(E.jsx)(f.a,{when:!R}),Object(E.jsxs)("div",{className:m()("ExperimentNotesTab__Editor",{isLoading:c}),children:[Object(E.jsxs)("div",{className:"ExperimentNotesTab__Editor__actionPanel",children:[Object(E.jsxs)("div",{className:"ExperimentNotesTab__Editor__actionPanel__info",children:[(null===o||void 0===o?void 0:o.created_at)&&Object(E.jsx)(v.a,{title:"Created at",children:Object(E.jsxs)("div",{className:"ExperimentNotesTab__Editor__actionPanel__info-field",children:[Object(E.jsx)(j.f,{name:"calendar"}),Object(E.jsx)(j.n,{tint:70,children:"".concat(s.a.utc(null===o||void 0===o?void 0:o.created_at).local().format(b.j))})]})}),(null===o||void 0===o?void 0:o.updated_at)&&Object(E.jsx)(v.a,{title:"Updated at",children:Object(E.jsxs)("div",{className:"ExperimentNotesTab__Editor__actionPanel__info-field",children:[Object(E.jsx)(j.f,{name:"time"}),Object(E.jsx)(j.n,{tint:70,children:"".concat(s.a.utc(null===o||void 0===o?void 0:o.updated_at).local().format(b.j))})]})})]}),Object(E.jsx)(v.a,{title:"Save Note",children:Object(E.jsx)("div",{children:Object(E.jsx)(j.c,{disabled:R||c,variant:"contained",size:"small",onClick:I,className:"ExperimentNotesTab__Editor__actionPanel__saveBtn",children:"Save"})})})]}),Object(E.jsx)(d.a,{ref:L,className:"ExperimentNotesTab__Editor__container",value:N,placeholder:"Leave your Note",theme:T||(null===(t=L.current)||void 0===t?void 0:t.theme()),disableExtensions:["table","image","container_notice"],tooltip:function(e){var t=e.children;return Object(E.jsx)(x.a,{children:t})},onChange:F}),c&&Object(E.jsx)("div",{className:"ExperimentNotesTab__spinnerWrapper",children:Object(E.jsx)(j.l,{})})]})]})}var S=r.a.memo(w);t.default=S},1596:function(e,t,n){"use strict";n.r(t);var a=n(0),i=n.n(a),c=n(11),r=n(1321),o=n(17),s=n(14),l=(n(1569),n(1));function d(e){var t=e.experimentName,n=e.description,a=e.updateExperiment;return i.a.useEffect((function(){s.a(o.a.experiment.tabs.settings.tabView)}),[]),Object(l.jsx)(c.a,{children:Object(l.jsx)("div",{className:"ExperimentSettingsTab",children:Object(l.jsx)("div",{className:"ExperimentSettingsTab__actionCardsCnt",children:Object(l.jsx)(r.a,{title:"Experiment Properties",defaultName:null!==t&&void 0!==t?t:"",defaultDescription:null!==n&&void 0!==n?n:"",onSave:function(e,t){a(e,t)}})})})})}var u=Object(a.memo)(d);t.default=u},736:function(e,t,n){"use strict";var a=n(0),i=n.n(a),c=n(700),r=n(5),o=n(218),s=(n(739),n(1));function l(e){return Object(s.jsx)(o.a,{children:Object(s.jsxs)(c.a,{open:e.open,onClose:e.onCancel,"aria-labelledby":"dialog-title","aria-describedby":"dialog-description",PaperProps:{elevation:10},className:"ConfirmModal ConfirmModal__".concat(e.statusType),children:[Object(s.jsxs)("div",{className:"ConfirmModal__Body",children:[Object(s.jsx)(r.c,{size:"small",className:"ConfirmModal__Close__Icon",color:"secondary",withOnlyIcon:!0,onClick:e.onCancel,children:Object(s.jsx)(r.f,{name:"close"})}),Object(s.jsxs)("div",{className:"ConfirmModal__Title__Container",children:[Object(s.jsx)("div",{className:"ConfirmModal__Icon",children:e.icon}),e.title&&Object(s.jsx)(r.n,{size:16,tint:100,component:"h4",weight:600,children:e.title})]}),Object(s.jsxs)("div",{children:[e.description&&Object(s.jsx)(r.n,{className:"ConfirmModal__description",weight:400,component:"p",id:"dialog-description",children:e.description}),Object(s.jsxs)("div",{children:[e.text&&Object(s.jsx)(r.n,{className:"ConfirmModal__text",weight:400,component:"p",size:14,id:"dialog-description",children:e.text||""}),e.children&&e.children]})]})]}),Object(s.jsxs)("div",{className:"ConfirmModal__Footer",children:[Object(s.jsx)(r.c,{onClick:e.onCancel,className:"ConfirmModal__CancelButton",children:e.cancelBtnText}),Object(s.jsx)(r.c,{onClick:e.onSubmit,color:"primary",variant:"contained",className:"ConfirmModal__ConfirmButton",autoFocus:!0,children:e.confirmBtnText})]})]})})}l.defaultProps={confirmBtnText:"Confirm",cancelBtnText:"Cancel",statusType:"info"},l.displayName="ConfirmModal",t.a=i.a.memo(l)},739:function(e,t,n){},953:function(e,t,n){"use strict";var a=n(847),i=n(752);t.a=function(){var e=Object(i.a)(a.d),t=e.fetchData;return{fetchExperimentContributions:function(e){return t(e)},experimentContributionsState:e.state,destroy:e.destroy}}()},985:function(e,t,n){"use strict";var a=n(6),i=(n(0),n(65)),c=n.n(i),r=n(95),o=n(353),s=n(5),l=n(11),d=n(17),u=n(76),m=n(14),v=n(20),j=(n(986),n(1)),f=[0,1,2,3,4];t.a=function(e){var t=e.data,n=e.startDate,i=e.endDate,b=e.cellSize,p=void 0===b?12:b,h=e.cellSpacing,x=void 0===h?4:h,_=e.scaleRange,O=void 0===_?4:_,g=e.onCellClick,N=e.additionalQuery,C=void 0===N?"":N,y=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],E=Object(r.h)();n=new Date(n.getFullYear(),n.getMonth(),n.getDate()),i=new Date(i.getFullYear(),i.getMonth(),i.getDate());for(var w=n;0!==w.getDay();)w=L(w,-1);for(var S=i;0!==S.getDay();)S=L(S,1);0===S.getDay()&&(S=L(S,7));var R=Math.floor(Math.abs((w-S)/864e5)),k=function(){var e=0;return Object(a.a)(Array(R).keys()).forEach((function(t){var n=M(t);e=n>e?n:e})),e}();function M(e){for(var n=I(e),a=0,i=0;i<t.length;i++){var c,r,o;(null===(c=t[i])||void 0===c?void 0:c[0].getFullYear())===n.getFullYear()&&(null===(r=t[i])||void 0===r?void 0:r[0].getMonth())===n.getMonth()&&(null===(o=t[i])||void 0===o?void 0:o[0].getDate())===n.getDate()&&(a+=t[i][1])}return a}var D=[].concat(Object(a.a)(y.slice(w.getMonth())),Object(a.a)(y.slice(0,w.getMonth()))),T={width:"".concat(R/7*p+(R/7-1)*x-50,"px")},B={gridTemplateColumns:"repeat(".concat(R/7,", 1fr)"),gridTemplateRows:"repeat(7, 1fr)",width:"".concat(R/7*p+(R/7-1)*x,"px"),height:"".concat(7*p+6*x,"px"),gridColumnGap:"".concat(x,"px"),gridRowGap:"".concat(x,"px")};function L(e,t){var n=new Date(e);return n.setDate(n.getDate()+t),n}function I(e){var t=Math.floor(e/7);return L(w,7*t+e%7)}function F(e){var t,n=M(e),a=I(e),r=n?(t=n,Math.ceil(t/k*O)):0,s=" ".concat(n," tracked run").concat(1!==n?"s":""," on ").concat(y[a.getMonth()]," ").concat(a.getDate(),", ").concat(a.getFullYear());return Object(j.jsx)(l.a,{children:Object(j.jsx)("div",{className:"CalendarHeatmap__cell__wrapper",children:+i<+I(e)?Object(j.jsx)("div",{className:"CalendarHeatmap__cell CalendarHeatmap__cell--dummy"}):Object(j.jsx)(o.a,{title:s,children:Object(j.jsx)("div",{className:"CalendarHeatmap__cell CalendarHeatmap__cell--scale-".concat(r||0),onClick:function(e){if(e.stopPropagation(),g(),r){var t=a.getTime(),n=Object(v.c)({query:"datetime(".concat(c()(t).format(u.d),") <= run.created_at < datetime(").concat(c()(t).add(1,"day").format(u.d),") ").concat(C)});m.b(d.a.dashboard.activityCellClick),E.push("/runs?select=".concat(n))}},role:"navigation"})})})},e)}return Object(j.jsxs)("div",{className:"CalendarHeatmap",children:[Object(j.jsxs)("div",{className:"CalendarHeatmap__map",children:[Object(j.jsx)("div",{}),Object(j.jsx)("div",{className:"CalendarHeatmap__map__axis CalendarHeatmap__map__axis--x",style:T,children:D.slice(0,10).map((function(e,t){return Object(j.jsx)("div",{className:"CalendarHeatmap__map__axis__tick--x",children:e},t)}))}),Object(j.jsx)("div",{className:"CalendarHeatmap__map__axis CalendarHeatmap__map__axis--y",children:["S","M","T","W","T","F","S"].map((function(e,t){return Object(j.jsx)("div",{className:"CalendarHeatmap__map__axis__tick--y",children:e},t)}))}),Object(j.jsx)("div",{className:"CalendarHeatmap__map__grid",style:B,children:Object(a.a)(Array(R).keys()).map((function(e){return F(e)}))})]}),Object(j.jsxs)("div",{className:"CalendarHeatmap__cell__info",children:[Object(j.jsx)(s.n,{weight:400,size:12,children:"Less"}),f.map((function(e){return Object(j.jsx)("div",{style:{width:p,height:p},className:"CalendarHeatmap__cell__wrapper",children:Object(j.jsx)("div",{className:"CalendarHeatmap__cell CalendarHeatmap__cell--scale-".concat(e)})},e)})),Object(j.jsx)(s.n,{weight:400,size:12,children:"More"})]})]})}},986:function(e,t,n){},987:function(e,t,n){},988:function(e,t,n){},989:function(e,t,n){},990:function(e,t,n){}}]);
//# sourceMappingURL=ExperimentOverviewTab.js.map?version=675e5628fbc19619aa9a