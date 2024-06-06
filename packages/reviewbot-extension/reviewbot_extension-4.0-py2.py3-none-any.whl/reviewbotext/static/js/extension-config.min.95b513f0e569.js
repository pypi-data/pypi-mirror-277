!function(){"use strict";{window.ReviewBot=window.ReviewBot||{},ReviewBot.ExtensionConfig=Backbone.Model.extend({defaults:{brokerURL:"",user:null},initialize(e,t){Backbone.Model.prototype.initialize.call(this,e,t),this.options=t}});const e=Backbone.View.extend({className:"rb-c-form-row",id:"reviewbot-user",events:{"click #reviewbot-user-create":"_createUser"},_templateRB4:_.template(`<div class="rb-c-form-field -is-required">
 <label class="rb-c-form-field__label" for="reviewbot-user-field"><%- labelText %></label>

 <div class="rb-c-form-field__input">
  <select class="related-object-options reviewbot-user-select"
          name="reviewbot_user"
          placeholder="<%- selectPlaceholderText %>"
          id="reviewbot-user-field"></select>
  <span class="reviewbot-user-create-details">
   <% if (!hasUser) { %><%= orHTML %><% } %>
  </span>
  <div class="rb-c-form-field__help"><%- descriptionText %></div>
 </div>
</div>`),_templateRB3:_.template(`<div class="form-row">
 <label class="required" for="reviewbot-user-field"><%- labelText %></label>
 <select class="related-object-options reviewbot-user-select"
         name="reviewbot_user"
         placeholder="<%- selectPlaceholderText %>"
         id="reviewbot-user-field"></select>
 <span class="reviewbot-user-create-details">
  <% if (!hasUser) { %><%= orHTML %><% } %>
 </span>
 <p class="help"><%- descriptionText %></p>
</div>`),_optionTemplate:_.template(`<div>
<% if (avatarURL) { %>
 <img src="<%- avatarURL %>">
<% } %>
<% if (fullname) { %>
 <span class="title"><%- fullname %></span>
 <span class="description">(<%- username %>)</span>
<% } else { %>
 <span class="title"><%- username %></span>
<% } %>
</div>`),render(){var e=this.model.get("user"),t=RB.Product?this._templateRB4:this._templateRB3,t=(this.$el.html(t({titleText:gettext("Review Bot User"),labelText:gettext("Review Bot User:"),descriptionText:gettext("Review Bot will use this user account to post reviews."),selectPlaceholderText:gettext("Select an existing user account"),orHTML:gettext('or <a href="#" id="reviewbot-user-create">create a new user for Review Bot</a>.'),hasUser:null!==e})),[]),r=[];return null!==e&&(t.push(e.id),r.push(e)),this._$select=this.$("select"),this._$select.selectize({closeAfterSelect:!0,dropdownParent:"body",hideSelected:!0,maxItems:1,preload:"focus",items:t,options:r,searchField:["fullname","username"],valueField:"id",load:(e,s)=>{var t={fullname:1,"only-fields":"avatar_url,fullname,id,username","only-links":""};0!==e.length&&(t.q=e),$.ajax({type:"GET",url:SITE_ROOT+"api/users/",data:t,success:e=>s(e.users),error:(e,t,r)=>{alert("Unexpected error when querying for users: "+r),console.error("User query failed",e,t,r),s()}})},render:{item:e=>this._optionTemplate({avatarURL:e.avatar_url,id:e.id,fullname:e.fullname,username:e.username}),option:e=>this._optionTemplate({avatarURL:e.avatar_url,id:e.id,fullname:e.fullname,username:e.username})}}),this._selectize=this._$select[0].selectize,this.listenTo(this.model,"change:user",(e,t)=>{this._setOption(t)}),this},_createUser(e){e.preventDefault(),e.stopPropagation();const t=this.$(".reviewbot-user-create-details");this._selectize.lock(),t.html('<span class="fa fa-spinner fa-pulse">'),$.ajax({type:"POST",url:this.model.options.userConfigURL,complete:()=>{this._selectize.unlock(),this._selectize.blur(),t.empty()},success:e=>{this._setOption(e)},error:(e,t,r)=>{alert("Unexpected error when creating the user: "+r),console.error("Failed to update user",e,t,r)}})},_setOption(e){this._selectize.clear(!0),this._selectize.clearOptions(),this._selectize.addOption(e),this._selectize.setValue(e.id,!0)}}),t=Backbone.View.extend({events:{"click #reviewbot-broker-status-refresh":"_onRefreshClicked"},_updatingTemplate:_.template(`<span class="fa fa-spinner fa-pulse"></span>
<%- refreshingText %>`),_connectedTemplate:_.template(`<div>
 <span class="fa fa-check"></span>
 <%- connectedText %>
</div>
<% if (workers.length === 0) { %>
 <div>
  <span class="fa fa-exclamation-triangle"></span>
  <%- workersText %>
 </div>
<% } else { %>
 <div>
  <span class="fa fa-check"></span>
  <%- workersText %>
  <ul>
   <% _.each(workers, function(worker) { %>
    <li>
     <span class="fa fa-desktop"></span>
     <%- worker.hostname %>
    </li>
   <% }); %>
  </ul>
 </div>
 <div>
  <span class="fa fa-cogs"></span>
  <%- readyText %>
  <%= configureIntegrationsHTML %>
 </div>
<% } %>
<div>
 <a href="#" id="reviewbot-broker-status-refresh"><%- refreshText %></a>
</div>`),_errorTemplate:_.template(`<div>
 <span class="fa fa-exclamation-triangle"></span>
 <%- errorText %>
</div>
<div>
 <a href="#" id="reviewbot-broker-status-refresh"><%- refreshText %></a>
</div>`),initialize(){this._updating=!1,this._connected=!1,this._rendered=!1,this._errorText="",this._workers=[],this.listenTo(this.model,"change",this._update),this._update()},render(){return this._$content=$('<div class="form-row">').appendTo(this.$el),this._rendered=!0,this._updateDisplay(),this},_updateDisplay(){if(this._rendered)if(this._updating)this._$content.html(this._updatingTemplate({refreshingText:gettext("Checking broker...")}));else if(this._connected){let e;e=0===this._workers.length?gettext("No worker nodes found."):interpolate(ngettext("%s worker node:","%s worker nodes:",this._workers.length),[this._workers.length]),this._$content.html(this._connectedTemplate({connectedText:gettext("Connected to broker."),workersText:e,refreshText:gettext("Refresh"),workers:this._workers,readyText:gettext("Review Bot is ready!"),configureIntegrationsHTML:interpolate(gettext('To configure when Review Bot tools are run, set up <a href="%s">integration configurations</a>.'),[this.model.options.integrationConfigURL])}))}else this._$content.html(this._errorTemplate({errorText:this._errorText,refreshText:gettext("Refresh")}))},_onRefreshClicked(e){e.preventDefault(),e.stopPropagation(),this._update()},_update(){this._updating||(this._updating=!0,this._updateDisplay(),$.ajax({type:"GET",url:this.model.options.workerStatusURL,success:e=>{this._workers=e.hosts||[],this._connected="success"===e.state,this._errorText=e.error||"",this._updating=!1,this._updateDisplay()},error:(e,t,r)=>{console.error("Failed to get broker status",e,t,r),this._errorText=gettext("Unable to connect to broker."),this._workers=[],this._connected=!1,this._updating=!1,this._updateDisplay()}}))}}),r=Backbone.View.extend({id:"reviewbot-broker",className:"rb-c-form-row",_templateRB4:_.template(`<div class="rb-c-form-field -is-required">
 <label class="rb-c-form-field__label" for="reviewbot-broker-field"><%- labelText %></label>

 <div class="rb-c-form-field__input">
  <input id="reviewbot-broker-field" name="reviewbot_broker_url"
         type="text" value="<%- brokerURL %>">
  <div class="rb-c-form-field__help"><%- descriptionText %></div>
 </div>
</div>`),_templateRB3:_.template(`<div class="form-row">
 <label class="required" for="reviewbot-broker-field"><%- labelText %></label>
 <input id="reviewbot-broker-field" name="reviewbot_broker_url"
        type="text" value="<%- brokerURL %>">
 <p class="help"><%- descriptionText %></p>
</div>`),render(){var e=RB.Product?this._templateRB4:this._templateRB3;return this.$el.html(e({titleText:gettext("Broker"),labelText:gettext("Broker URL:"),descriptionText:gettext("The URL to your AMQP broker."),brokerURL:this.model.get("brokerURL")})),this}}),s=Backbone.View.extend({events:{'click input[type="submit"]':"_onSaveClicked"},_templateRB4:`<form class="rb-c-form -is-aligned">
 <fieldset class="rb-c-form-fieldset">
  <div class="rb-c-form-fieldset__content">
   <div class="rb-c-form-fieldset__fields">
   </div>
  </div>
 </fieldset>
 <div class="rb-c-form__actions">
  <div class="rb-c-form__actions-primary">
   <input type="submit" class="rb-c-form__action -is-primary">
  </div>
 </div>
</form>`,_templateRB3:`<form class="rb-c-form-fieldset__fields">
</form>
<div class="submit-row">
 <input type="submit" class="rb-c-form-action -is-primary default">
</div>`,initialize(){this._userConfigView=new e({model:this.model}),this._brokerConfigView=new r({model:this.model})},render(){this._userConfigView.render(),this._brokerConfigView.render();var e=RB.Product?this._templateRB4:this._templateRB3;return this.$el.html(e),this._$form=this.$("form"),this.$(".rb-c-form-fieldset__fields").append(this._userConfigView.$el).append(this._brokerConfigView.$el),this._$saveButton=this.$('input[type="submit"]').val(gettext("Save")),this},_onSaveClicked(e){e.preventDefault(),e.stopPropagation(),this._$saveButton.prop("disabled",!0);const t=$('<span class="fa fa-spinner fa-pulse">').insertBefore(this._$saveButton);$.ajax({type:"POST",url:window.location.pathname,data:this._$form.serialize(),complete:()=>{this._$saveButton.prop("disabled",!1),t.remove()},success:e=>{"success"===e.result?(e.broker_url&&this.model.set("brokerURL",e.broker_url),e.user&&this.model.set("user",e.user)):"error"===e.result?(console.error("Failed to save Review Bot configuration",e),alert(e.error)):console.error("Unexpected response from server when saving Review Bot configuration.",e)},error:(e,t,r)=>{alert("Unexpected error when querying broker: "+r),console.error("Failed to update broker",e,t,r)}})}});ReviewBot.ExtensionConfigView=Backbone.View.extend({_templateRB4:_.template(`<header class="rb-c-content-header -is-main">
 <h1 class="rb-c-content-header__title"><%- configureText %></h1>
</header>
<div class="rb-c-page-content-box -is-content-flush"
     id="reviewbot-extension-config"></div>

<header class="rb-c-content-header -is-main">
 <h1 class="rb-c-content-header__title"><%- brokerText %></h1>
</header>
<div class="rb-c-page-content-box" id="reviewbot-broker-status"></div>`),_templateRB3:_.template(`<h1 class="title"><%- configureText %></h1>
<div id="content-main">
 <fieldset class="module aligned" id="reviewbot-extension-config"></fieldset>

 <fieldset class="module aligned" id="reviewbot-broker-status">
  <h2><%- brokerText %></h2>
 </div>
</fieldset>`),render(){var e=RB.Product?this._templateRB4:this._templateRB3;return this.$el.html(e({configureText:gettext("Configure Review Bot"),brokerText:gettext("Broker Status")})),this._view=new s({model:this.model,el:this.$("#reviewbot-extension-config")}),this._statusView=new t({model:this.model,el:this.$("#reviewbot-broker-status")}),this._view.render(),this._statusView.render(),this}})}}.call(this);
