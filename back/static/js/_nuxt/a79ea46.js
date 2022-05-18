(window.webpackJsonp=window.webpackJsonp||[]).push([[11],{706:function(e,t,l){"use strict";l(25),l(37);var n=l(3),o=l.n(n),r={name:"AdminTaskForm",props:{value:{type:Object,required:!0},errors:{type:Object,required:!0},newHireReadOnly:{type:Boolean,default:!1},personalize:{type:Boolean,default:!1},noNewHire:{type:Boolean,default:!1},showLastField:{type:Boolean,default:!0},fullReadOnly:{type:Boolean,default:!1}},data:function(e){return{menu1:!1,states:[{name:e.$t("hrTask.low"),id:1},{name:e.$t("hrTask.medium"),id:2},{name:e.$t("hrTask.high"),id:3}]}},computed:{errorMessages:function(){return JSON.parse(JSON.stringify(this.errors))},pickSomeone:function(){return this.$store.state.slackPeople.map((function(e){return e.name+" ("+e.id+")"}))},computedDateFormattedMomentjs:function(){var e="";return this.value.date?(e=o()(this.value.date),"nl"===this.$store.state.org.language?e.format("dddd, D MMMM YYYY"):e.format("dddd, MMMM Do YYYY")):e}},watch:{errors:function(e){"content"in e&&this.$store.dispatch("showSnackbar","Content: "+e.content[0])},value:{handler:function(e){this.$emit("input",e)},deep:!0},"value.slack":function(e){this.value.email_slack=e},"value.email":function(e){this.value.email_slack=e},"value.assigned_to":function(e){this.value.assigned_to_id=e.id},"value.new_hire":function(e){this.value.new_hire_id=e.id}}},d=l(23),c=l(24),m=l.n(c),v=l(126),f=l(644),h=l(872),k=l(216),y=l(34),_=l(65),component=Object(d.a)(r,(function(){var e=this,t=e.$createElement,l=e._self._c||t;return l("div",{staticStyle:{width:"100%"}},[l("v-col",{staticClass:"py-0",attrs:{sm:"12"}},[l("v-text-field",{attrs:{label:e.$t("forms.name"),disabled:e.fullReadOnly,"error-messages":e.errorMessages.name},on:{keyup:function(t){e.errorMessages.name=""}},model:{value:e.value.name,callback:function(t){e.$set(e.value,"name",t)},expression:"value.name"}})],1),e._v(" "),e.noNewHire?e._e():l("v-col",{staticClass:"py-0",attrs:{sm:"12"}},[l("v-autocomplete",{attrs:{items:e.$store.state.newhires.all,disabled:e.newHireReadOnly||e.fullReadOnly,label:e.$t("hrTask.newHire"),"item-value":"email","return-object":"","item-text":"full_name"},model:{value:e.value.new_hire,callback:function(t){e.$set(e.value,"new_hire",t)},expression:"value.new_hire"}})],1),e._v(" "),l("v-col",{staticClass:"py-0",attrs:{sm:"12"}},[l("v-autocomplete",{attrs:{items:e.$store.state.admins,label:e.$t("hrTask.assignedTo"),disabled:e.fullReadOnly,"return-object":"","item-value":"email","item-text":"full_name"},model:{value:e.value.assigned_to,callback:function(t){e.$set(e.value,"assigned_to",t)},expression:"value.assigned_to"}})],1),e._v(" "),l("v-col",{staticClass:"py-0",attrs:{sm:"12"}},[l("v-menu",{attrs:{disabled:e.fullReadOnly,"close-on-content-click":!1,"max-width":"290"},scopedSlots:e._u([{key:"activator",fn:function(t){var n=t.on;return[l("v-text-field",e._g({attrs:{disabled:e.fullReadOnly,label:e.$t("hrTask.due"),"error-messages":e.errorMessages.date,readonly:"","prepend-icon":"event"},on:{keyup:function(t){e.errorMessages.date=""}},model:{value:e.computedDateFormattedMomentjs,callback:function(t){e.computedDateFormattedMomentjs=t},expression:"computedDateFormattedMomentjs"}},n))]}}]),model:{value:e.menu1,callback:function(t){e.menu1=t},expression:"menu1"}},[e._v(" "),l("v-date-picker",{attrs:{locale:e.$store.state.org.locale,disabled:e.fullReadOnly},on:{change:function(t){e.menu1=!1}},model:{value:e.value.date,callback:function(t){e.$set(e.value,"date",t)},expression:"value.date"}})],1)],1),e._v(" "),l("v-col",{staticClass:"py-0",attrs:{sm:"12"}},[l("v-select",{attrs:{items:e.states,label:e.$t("hrTask.priority"),disabled:e.fullReadOnly,"hide-details":"","prepend-icon":"far fa-flag","item-text":"name","item-value":"id"},model:{value:e.value.priority,callback:function(t){e.$set(e.value,"priority",t)},expression:"value.priority"}})],1),e._v(" "),e.showLastField?l("v-col",{staticStyle:{"margin-top":"10px"},attrs:{sm:"12"}},[l("VTextAreaEmoji",{attrs:{label:e.$t("hrTask.moreDetails"),personalize:e.personalize,emoji:!0,disabled:e.fullReadOnly},model:{value:e.value.comment,callback:function(t){e.$set(e.value,"comment",t)},expression:"value.comment"}})],1):e._e(),e._v(" "),e.showLastField?l("v-col",{staticClass:"py-0",attrs:{sm:"12"}},[l("v-select",{attrs:{items:[{text:e.$t("hrTask.doNotNotify"),option:"0"},{text:e.$t("hrTask.sendEmail"),option:"1"},{text:e.$t("hrTask.sendSlack"),option:"2"}],label:e.$t("hrTask.notify"),disabled:e.fullReadOnly,"hide-details":"","item-text":"text","item-value":"option"},model:{value:e.value.option,callback:function(t){e.$set(e.value,"option",t)},expression:"value.option"}})],1):e._e(),e._v(" "),e.showLastField&&"1"===e.value.option?l("v-col",{staticClass:"py-0",staticStyle:{"margin-top":"10px"},attrs:{sm:"12"}},[l("v-text-field",{attrs:{label:e.$t("hrTask.email"),type:"email"},model:{value:e.value.email,callback:function(t){e.$set(e.value,"email",t)},expression:"value.email"}})],1):e._e(),e._v(" "),e.showLastField&&"2"===e.value.option?l("v-col",{staticClass:"py-0",staticStyle:{"margin-top":"10px"},attrs:{sm:"12"}},[l("v-autocomplete",{attrs:{items:e.pickSomeone,label:e.$t("hrTask.pick")},model:{value:e.value.slack,callback:function(t){e.$set(e.value,"slack",t)},expression:"value.slack"}})],1):e._e()],1)}),[],!1,null,null,null);t.a=component.exports;m()(component,{VAutocomplete:v.a,VCol:f.a,VDatePicker:h.a,VMenu:k.a,VSelect:y.a,VTextField:_.a})},892:function(e,t,l){"use strict";l.r(t);l(7);var n={layout:"admin",components:{HRTaskForm:l(706).a},data:function(){return{loading:!1,saving:!1,submittingForm:!1,errors:{},employee:{},adminTask:{user:this.$store.state.newhires.all[0],assigned_to:this.$store.state.admins[0],date:"",priority:1,option:"0",slack_email:""}}},methods:{saveAdminTask:function(){var e=this;this.saving=!0,this.$hrtasks.create(this.adminTask).then((function(data){e.$router.push({name:"admin-hrtasks-id",params:{id:data.id}}),e.$store.dispatch("showSnackbar",e.$t("hrTask.created"))})).catch((function(t){e.errors=t})).finally((function(){e.saving=!1}))}}},o=l(23),r=l(24),d=l.n(r),c=l(140),m=l(652),v=l(648),component=Object(o.a)(n,(function(){var e=this,t=e.$createElement,l=e._self._c||t;return l("TemplateCompInner",[l("template",{slot:"header"},[l("h1",{staticClass:"heading",staticStyle:{"margin-top":"10px"}},[e._v("\n      "+e._s(e.$t("hrTask.addNewAdminTask"))+"\n    ")])]),e._v(" "),l("template",{slot:"formpart"},[l("v-container",{attrs:{"grid-list-md":"",fluid:"",wrap:""}},[l("v-row",{attrs:{wrap:""}},[l("HRTaskForm",{attrs:{errors:e.errors},model:{value:e.adminTask,callback:function(t){e.adminTask=t},expression:"adminTask"}})],1)],1)],1),e._v(" "),l("template",{slot:"footer"},[l("v-btn",{staticStyle:{float:"right"},attrs:{loading:e.saving,color:"primary"},on:{click:e.saveAdminTask}},[e._v("\n      "+e._s(e.$t("buttons.add"))+"\n    ")])],1)],2)}),[],!1,null,"191f5d22",null);t.default=component.exports;d()(component,{VBtn:c.a,VContainer:m.a,VRow:v.a})}}]);