"use strict";
(() => {
  var __defProp = Object.defineProperty, __defProps = Object.defineProperties, __getOwnPropDesc = Object.getOwnPropertyDescriptor, __getOwnPropDescs = Object.getOwnPropertyDescriptors;
  var __getOwnPropSymbols = Object.getOwnPropertySymbols;
  var __hasOwnProp = Object.prototype.hasOwnProperty, __propIsEnum = Object.prototype.propertyIsEnumerable;
  var __defNormalProp = (obj, key, value) => key in obj ? __defProp(obj, key, { enumerable: !0, configurable: !0, writable: !0, value }) : obj[key] = value, __spreadValues = (a3, b3) => {
    for (var prop in b3 || (b3 = {}))
      __hasOwnProp.call(b3, prop) && __defNormalProp(a3, prop, b3[prop]);
    if (__getOwnPropSymbols)
      for (var prop of __getOwnPropSymbols(b3))
        __propIsEnum.call(b3, prop) && __defNormalProp(a3, prop, b3[prop]);
    return a3;
  }, __spreadProps = (a3, b3) => __defProps(a3, __getOwnPropDescs(b3));
  var __decorateClass = (decorators, target, key, kind) => {
    for (var result = kind > 1 ? void 0 : kind ? __getOwnPropDesc(target, key) : target, i5 = decorators.length - 1, decorator; i5 >= 0; i5--)
      (decorator = decorators[i5]) && (result = (kind ? decorator(target, key, result) : decorator(result)) || result);
    return kind && result && __defProp(target, key, result), result;
  };
  var __async = (__this, __arguments, generator) => new Promise((resolve, reject) => {
    var fulfilled = (value) => {
      try {
        step(generator.next(value));
      } catch (e9) {
        reject(e9);
      }
    }, rejected = (value) => {
      try {
        step(generator.throw(value));
      } catch (e9) {
        reject(e9);
      }
    }, step = (x2) => x2.done ? resolve(x2.value) : Promise.resolve(x2.value).then(fulfilled, rejected);
    step((generator = generator.apply(__this, __arguments)).next());
  });

  // <define:SVG_ICONS_FONTAWESOME>
  var define_SVG_ICONS_FONTAWESOME_default = { faAngleLeft: '<svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="angle-left" class="svg-inline--fa fa-angle-left" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"><path fill="currentColor" d="M41.4 233.4c-12.5 12.5-12.5 32.8 0 45.3l160 160c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L109.3 256 246.6 118.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-160 160z"></path></svg>', faAngleRight: '<svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="angle-right" class="svg-inline--fa fa-angle-right" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"><path fill="currentColor" d="M278.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-160 160c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L210.7 256 73.4 118.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l160 160z"></path></svg>', faFilePen: '<svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="file-pen" class="svg-inline--fa fa-file-pen" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path fill="currentColor" d="M0 64C0 28.7 28.7 0 64 0H224V128c0 17.7 14.3 32 32 32H384V285.7l-86.8 86.8c-10.3 10.3-17.5 23.1-21 37.2l-18.7 74.9c-2.3 9.2-1.8 18.8 1.3 27.5H64c-35.3 0-64-28.7-64-64V64zm384 64H256V0L384 128zM549.8 235.7l14.4 14.4c15.6 15.6 15.6 40.9 0 56.6l-29.4 29.4-71-71 29.4-29.4c15.6-15.6 40.9-15.6 56.6 0zM311.9 417L441.1 287.8l71 71L382.9 487.9c-4.1 4.1-9.2 7-14.9 8.4l-60.1 15c-5.5 1.4-11.2-.2-15.2-4.2s-5.6-9.7-4.2-15.2l15-60.1c1.4-5.6 4.3-10.8 8.4-14.9z"></path></svg>', faRetweet: '<svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="retweet" class="svg-inline--fa fa-retweet" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path fill="currentColor" d="M272 416c17.7 0 32-14.3 32-32s-14.3-32-32-32H160c-17.7 0-32-14.3-32-32V192h32c12.9 0 24.6-7.8 29.6-19.8s2.2-25.7-6.9-34.9l-64-64c-12.5-12.5-32.8-12.5-45.3 0l-64 64c-9.2 9.2-11.9 22.9-6.9 34.9s16.6 19.8 29.6 19.8l32 0 0 128c0 53 43 96 96 96H272zM304 96c-17.7 0-32 14.3-32 32s14.3 32 32 32l112 0c17.7 0 32 14.3 32 32l0 128H416c-12.9 0-24.6 7.8-29.6 19.8s-2.2 25.7 6.9 34.9l64 64c12.5 12.5 32.8 12.5 45.3 0l64-64c9.2-9.2 11.9-22.9 6.9-34.9s-16.6-19.8-29.6-19.8l-32 0V192c0-53-43-96-96-96L304 96z"></path></svg>', faThumbtack: '<svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="thumbtack" class="svg-inline--fa fa-thumbtack" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path fill="currentColor" d="M32 32C32 14.3 46.3 0 64 0H320c17.7 0 32 14.3 32 32s-14.3 32-32 32H290.5l11.4 148.2c36.7 19.9 65.7 53.2 79.5 94.7l1 3c3.3 9.8 1.6 20.5-4.4 28.8s-15.7 13.3-26 13.3H32c-10.3 0-19.9-4.9-26-13.3s-7.7-19.1-4.4-28.8l1-3c13.8-41.5 42.8-74.8 79.5-94.7L93.5 64H64C46.3 64 32 49.7 32 32zM160 384h64v96c0 17.7-14.3 32-32 32s-32-14.3-32-32V384z"></path></svg>' };

  // node_modules/@lit/reactive-element/css-tag.js
  var t = globalThis, e = t.ShadowRoot && (t.ShadyCSS === void 0 || t.ShadyCSS.nativeShadow) && "adoptedStyleSheets" in Document.prototype && "replace" in CSSStyleSheet.prototype, s = Symbol(), o = /* @__PURE__ */ new WeakMap(), n = class {
    constructor(t7, e9, o7) {
      if (this._$cssResult$ = !0, o7 !== s)
        throw Error("CSSResult is not constructable. Use `unsafeCSS` or `css` instead.");
      this.cssText = t7, this.t = e9;
    }
    get styleSheet() {
      let t7 = this.o, s4 = this.t;
      if (e && t7 === void 0) {
        let e9 = s4 !== void 0 && s4.length === 1;
        e9 && (t7 = o.get(s4)), t7 === void 0 && ((this.o = t7 = new CSSStyleSheet()).replaceSync(this.cssText), e9 && o.set(s4, t7));
      }
      return t7;
    }
    toString() {
      return this.cssText;
    }
  }, r = (t7) => new n(typeof t7 == "string" ? t7 : t7 + "", void 0, s), i = (t7, ...e9) => {
    let o7 = t7.length === 1 ? t7[0] : e9.reduce((e10, s4, o8) => e10 + ((t8) => {
      if (t8._$cssResult$ === !0)
        return t8.cssText;
      if (typeof t8 == "number")
        return t8;
      throw Error("Value passed to 'css' function must be a 'css' function result: " + t8 + ". Use 'unsafeCSS' to pass non-literal values, but take care to ensure page security.");
    })(s4) + t7[o8 + 1], t7[0]);
    return new n(o7, t7, s);
  }, S = (s4, o7) => {
    if (e)
      s4.adoptedStyleSheets = o7.map((t7) => t7 instanceof CSSStyleSheet ? t7 : t7.styleSheet);
    else
      for (let e9 of o7) {
        let o8 = document.createElement("style"), n5 = t.litNonce;
        n5 !== void 0 && o8.setAttribute("nonce", n5), o8.textContent = e9.cssText, s4.appendChild(o8);
      }
  }, c = e ? (t7) => t7 : (t7) => t7 instanceof CSSStyleSheet ? ((t8) => {
    let e9 = "";
    for (let s4 of t8.cssRules)
      e9 += s4.cssText;
    return r(e9);
  })(t7) : t7;

  // node_modules/@lit/reactive-element/reactive-element.js
  var { is: i2, defineProperty: e2, getOwnPropertyDescriptor: r2, getOwnPropertyNames: h, getOwnPropertySymbols: o2, getPrototypeOf: n2 } = Object, a = globalThis, c2 = a.trustedTypes, l = c2 ? c2.emptyScript : "", p = a.reactiveElementPolyfillSupport, d = (t7, s4) => t7, u = { toAttribute(t7, s4) {
    switch (s4) {
      case Boolean:
        t7 = t7 ? l : null;
        break;
      case Object:
      case Array:
        t7 = t7 == null ? t7 : JSON.stringify(t7);
    }
    return t7;
  }, fromAttribute(t7, s4) {
    let i5 = t7;
    switch (s4) {
      case Boolean:
        i5 = t7 !== null;
        break;
      case Number:
        i5 = t7 === null ? null : Number(t7);
        break;
      case Object:
      case Array:
        try {
          i5 = JSON.parse(t7);
        } catch (t8) {
          i5 = null;
        }
    }
    return i5;
  } }, f = (t7, s4) => !i2(t7, s4), y = { attribute: !0, type: String, converter: u, reflect: !1, hasChanged: f }, _a, _b;
  (_a = Symbol.metadata) != null || (Symbol.metadata = Symbol("metadata")), (_b = a.litPropertyMetadata) != null || (a.litPropertyMetadata = /* @__PURE__ */ new WeakMap());
  var b = class extends HTMLElement {
    static addInitializer(t7) {
      var _a7;
      this._$Ei(), ((_a7 = this.l) != null ? _a7 : this.l = []).push(t7);
    }
    static get observedAttributes() {
      return this.finalize(), this._$Eh && [...this._$Eh.keys()];
    }
    static createProperty(t7, s4 = y) {
      if (s4.state && (s4.attribute = !1), this._$Ei(), this.elementProperties.set(t7, s4), !s4.noAccessor) {
        let i5 = Symbol(), r7 = this.getPropertyDescriptor(t7, i5, s4);
        r7 !== void 0 && e2(this.prototype, t7, r7);
      }
    }
    static getPropertyDescriptor(t7, s4, i5) {
      var _a7;
      let { get: e9, set: h3 } = (_a7 = r2(this.prototype, t7)) != null ? _a7 : { get() {
        return this[s4];
      }, set(t8) {
        this[s4] = t8;
      } };
      return { get() {
        return e9 == null ? void 0 : e9.call(this);
      }, set(s5) {
        let r7 = e9 == null ? void 0 : e9.call(this);
        h3.call(this, s5), this.requestUpdate(t7, r7, i5);
      }, configurable: !0, enumerable: !0 };
    }
    static getPropertyOptions(t7) {
      var _a7;
      return (_a7 = this.elementProperties.get(t7)) != null ? _a7 : y;
    }
    static _$Ei() {
      if (this.hasOwnProperty(d("elementProperties")))
        return;
      let t7 = n2(this);
      t7.finalize(), t7.l !== void 0 && (this.l = [...t7.l]), this.elementProperties = new Map(t7.elementProperties);
    }
    static finalize() {
      if (this.hasOwnProperty(d("finalized")))
        return;
      if (this.finalized = !0, this._$Ei(), this.hasOwnProperty(d("properties"))) {
        let t8 = this.properties, s4 = [...h(t8), ...o2(t8)];
        for (let i5 of s4)
          this.createProperty(i5, t8[i5]);
      }
      let t7 = this[Symbol.metadata];
      if (t7 !== null) {
        let s4 = litPropertyMetadata.get(t7);
        if (s4 !== void 0)
          for (let [t8, i5] of s4)
            this.elementProperties.set(t8, i5);
      }
      this._$Eh = /* @__PURE__ */ new Map();
      for (let [t8, s4] of this.elementProperties) {
        let i5 = this._$Eu(t8, s4);
        i5 !== void 0 && this._$Eh.set(i5, t8);
      }
      this.elementStyles = this.finalizeStyles(this.styles);
    }
    static finalizeStyles(s4) {
      let i5 = [];
      if (Array.isArray(s4)) {
        let e9 = new Set(s4.flat(1 / 0).reverse());
        for (let s5 of e9)
          i5.unshift(c(s5));
      } else
        s4 !== void 0 && i5.push(c(s4));
      return i5;
    }
    static _$Eu(t7, s4) {
      let i5 = s4.attribute;
      return i5 === !1 ? void 0 : typeof i5 == "string" ? i5 : typeof t7 == "string" ? t7.toLowerCase() : void 0;
    }
    constructor() {
      super(), this._$Ep = void 0, this.isUpdatePending = !1, this.hasUpdated = !1, this._$Em = null, this._$Ev();
    }
    _$Ev() {
      var _a7;
      this._$Eg = new Promise((t7) => this.enableUpdating = t7), this._$AL = /* @__PURE__ */ new Map(), this._$E_(), this.requestUpdate(), (_a7 = this.constructor.l) == null || _a7.forEach((t7) => t7(this));
    }
    addController(t7) {
      var _a7, _b3;
      ((_a7 = this._$ES) != null ? _a7 : this._$ES = []).push(t7), this.renderRoot !== void 0 && this.isConnected && ((_b3 = t7.hostConnected) == null || _b3.call(t7));
    }
    removeController(t7) {
      var _a7;
      (_a7 = this._$ES) == null || _a7.splice(this._$ES.indexOf(t7) >>> 0, 1);
    }
    _$E_() {
      let t7 = /* @__PURE__ */ new Map(), s4 = this.constructor.elementProperties;
      for (let i5 of s4.keys())
        this.hasOwnProperty(i5) && (t7.set(i5, this[i5]), delete this[i5]);
      t7.size > 0 && (this._$Ep = t7);
    }
    createRenderRoot() {
      var _a7;
      let t7 = (_a7 = this.shadowRoot) != null ? _a7 : this.attachShadow(this.constructor.shadowRootOptions);
      return S(t7, this.constructor.elementStyles), t7;
    }
    connectedCallback() {
      var _a7, _b3;
      (_a7 = this.renderRoot) != null || (this.renderRoot = this.createRenderRoot()), this.enableUpdating(!0), (_b3 = this._$ES) == null || _b3.forEach((t7) => {
        var _a8;
        return (_a8 = t7.hostConnected) == null ? void 0 : _a8.call(t7);
      });
    }
    enableUpdating(t7) {
    }
    disconnectedCallback() {
      var _a7;
      (_a7 = this._$ES) == null || _a7.forEach((t7) => {
        var _a8;
        return (_a8 = t7.hostDisconnected) == null ? void 0 : _a8.call(t7);
      });
    }
    attributeChangedCallback(t7, s4, i5) {
      this._$AK(t7, i5);
    }
    _$EO(t7, s4) {
      var _a7;
      let i5 = this.constructor.elementProperties.get(t7), e9 = this.constructor._$Eu(t7, i5);
      if (e9 !== void 0 && i5.reflect === !0) {
        let r7 = (((_a7 = i5.converter) == null ? void 0 : _a7.toAttribute) !== void 0 ? i5.converter : u).toAttribute(s4, i5.type);
        this._$Em = t7, r7 == null ? this.removeAttribute(e9) : this.setAttribute(e9, r7), this._$Em = null;
      }
    }
    _$AK(t7, s4) {
      var _a7;
      let i5 = this.constructor, e9 = i5._$Eh.get(t7);
      if (e9 !== void 0 && this._$Em !== e9) {
        let t8 = i5.getPropertyOptions(e9), r7 = typeof t8.converter == "function" ? { fromAttribute: t8.converter } : ((_a7 = t8.converter) == null ? void 0 : _a7.fromAttribute) !== void 0 ? t8.converter : u;
        this._$Em = e9, this[e9] = r7.fromAttribute(s4, t8.type), this._$Em = null;
      }
    }
    requestUpdate(t7, s4, i5, e9 = !1, r7) {
      var _a7;
      if (t7 !== void 0) {
        if (i5 != null || (i5 = this.constructor.getPropertyOptions(t7)), !((_a7 = i5.hasChanged) != null ? _a7 : f)(e9 ? r7 : this[t7], s4))
          return;
        this.C(t7, s4, i5);
      }
      this.isUpdatePending === !1 && (this._$Eg = this._$EP());
    }
    C(t7, s4, i5) {
      var _a7;
      this._$AL.has(t7) || this._$AL.set(t7, s4), i5.reflect === !0 && this._$Em !== t7 && ((_a7 = this._$Ej) != null ? _a7 : this._$Ej = /* @__PURE__ */ new Set()).add(t7);
    }
    _$EP() {
      return __async(this, null, function* () {
        this.isUpdatePending = !0;
        try {
          yield this._$Eg;
        } catch (t8) {
          Promise.reject(t8);
        }
        let t7 = this.scheduleUpdate();
        return t7 != null && (yield t7), !this.isUpdatePending;
      });
    }
    scheduleUpdate() {
      return this.performUpdate();
    }
    performUpdate() {
      var _a7;
      if (!this.isUpdatePending)
        return;
      if (!this.hasUpdated) {
        if (this._$Ep) {
          for (let [t9, s5] of this._$Ep)
            this[t9] = s5;
          this._$Ep = void 0;
        }
        let t8 = this.constructor.elementProperties;
        if (t8.size > 0)
          for (let [s5, i5] of t8)
            i5.wrapped !== !0 || this._$AL.has(s5) || this[s5] === void 0 || this.C(s5, this[s5], i5);
      }
      let t7 = !1, s4 = this._$AL;
      try {
        t7 = this.shouldUpdate(s4), t7 ? (this.willUpdate(s4), (_a7 = this._$ES) == null || _a7.forEach((t8) => {
          var _a8;
          return (_a8 = t8.hostUpdate) == null ? void 0 : _a8.call(t8);
        }), this.update(s4)) : this._$ET();
      } catch (s5) {
        throw t7 = !1, this._$ET(), s5;
      }
      t7 && this._$AE(s4);
    }
    willUpdate(t7) {
    }
    _$AE(t7) {
      var _a7;
      (_a7 = this._$ES) == null || _a7.forEach((t8) => {
        var _a8;
        return (_a8 = t8.hostUpdated) == null ? void 0 : _a8.call(t8);
      }), this.hasUpdated || (this.hasUpdated = !0, this.firstUpdated(t7)), this.updated(t7);
    }
    _$ET() {
      this._$AL = /* @__PURE__ */ new Map(), this.isUpdatePending = !1;
    }
    get updateComplete() {
      return this.getUpdateComplete();
    }
    getUpdateComplete() {
      return this._$Eg;
    }
    shouldUpdate(t7) {
      return !0;
    }
    update(t7) {
      this._$Ej && (this._$Ej = this._$Ej.forEach((t8) => this._$EO(t8, this[t8]))), this._$ET();
    }
    updated(t7) {
    }
    firstUpdated(t7) {
    }
  }, _a2;
  b.elementStyles = [], b.shadowRootOptions = { mode: "open" }, b[d("elementProperties")] = /* @__PURE__ */ new Map(), b[d("finalized")] = /* @__PURE__ */ new Map(), p == null || p({ ReactiveElement: b }), ((_a2 = a.reactiveElementVersions) != null ? _a2 : a.reactiveElementVersions = []).push("2.0.1");

  // node_modules/lit-html/lit-html.js
  var t2 = globalThis, i3 = t2.trustedTypes, s2 = i3 ? i3.createPolicy("lit-html", { createHTML: (t7) => t7 }) : void 0, e3 = "$lit$", h2 = `lit$${(Math.random() + "").slice(9)}$`, o3 = "?" + h2, n3 = `<${o3}>`, r3 = document, l2 = () => r3.createComment(""), c3 = (t7) => t7 === null || typeof t7 != "object" && typeof t7 != "function", a2 = Array.isArray, u2 = (t7) => a2(t7) || typeof (t7 == null ? void 0 : t7[Symbol.iterator]) == "function", d2 = `[ 	
\f\r]`, f2 = /<(?:(!--|\/[^a-zA-Z])|(\/?[a-zA-Z][^>\s]*)|(\/?$))/g, v = /-->/g, _ = />/g, m = RegExp(`>|${d2}(?:([^\\s"'>=/]+)(${d2}*=${d2}*(?:[^ 	
\f\r"'\`<>=]|("|')|))|$)`, "g"), p2 = /'/g, g = /"/g, $ = /^(?:script|style|textarea|title)$/i, y2 = (t7) => (i5, ...s4) => ({ _$litType$: t7, strings: i5, values: s4 }), x = y2(1), b2 = y2(2), w = Symbol.for("lit-noChange"), T = Symbol.for("lit-nothing"), A = /* @__PURE__ */ new WeakMap(), E = r3.createTreeWalker(r3, 129);
  function C(t7, i5) {
    if (!Array.isArray(t7) || !t7.hasOwnProperty("raw"))
      throw Error("invalid template strings array");
    return s2 !== void 0 ? s2.createHTML(i5) : i5;
  }
  var P = (t7, i5) => {
    let s4 = t7.length - 1, o7 = [], r7, l3 = i5 === 2 ? "<svg>" : "", c4 = f2;
    for (let i6 = 0; i6 < s4; i6++) {
      let s5 = t7[i6], a3, u3, d3 = -1, y3 = 0;
      for (; y3 < s5.length && (c4.lastIndex = y3, u3 = c4.exec(s5), u3 !== null); )
        y3 = c4.lastIndex, c4 === f2 ? u3[1] === "!--" ? c4 = v : u3[1] !== void 0 ? c4 = _ : u3[2] !== void 0 ? ($.test(u3[2]) && (r7 = RegExp("</" + u3[2], "g")), c4 = m) : u3[3] !== void 0 && (c4 = m) : c4 === m ? u3[0] === ">" ? (c4 = r7 != null ? r7 : f2, d3 = -1) : u3[1] === void 0 ? d3 = -2 : (d3 = c4.lastIndex - u3[2].length, a3 = u3[1], c4 = u3[3] === void 0 ? m : u3[3] === '"' ? g : p2) : c4 === g || c4 === p2 ? c4 = m : c4 === v || c4 === _ ? c4 = f2 : (c4 = m, r7 = void 0);
      let x2 = c4 === m && t7[i6 + 1].startsWith("/>") ? " " : "";
      l3 += c4 === f2 ? s5 + n3 : d3 >= 0 ? (o7.push(a3), s5.slice(0, d3) + e3 + s5.slice(d3) + h2 + x2) : s5 + h2 + (d3 === -2 ? i6 : x2);
    }
    return [C(t7, l3 + (t7[s4] || "<?>") + (i5 === 2 ? "</svg>" : "")), o7];
  }, V = class _V {
    constructor({ strings: t7, _$litType$: s4 }, n5) {
      let r7;
      this.parts = [];
      let c4 = 0, a3 = 0, u3 = t7.length - 1, d3 = this.parts, [f3, v2] = P(t7, s4);
      if (this.el = _V.createElement(f3, n5), E.currentNode = this.el.content, s4 === 2) {
        let t8 = this.el.content.firstChild;
        t8.replaceWith(...t8.childNodes);
      }
      for (; (r7 = E.nextNode()) !== null && d3.length < u3; ) {
        if (r7.nodeType === 1) {
          if (r7.hasAttributes())
            for (let t8 of r7.getAttributeNames())
              if (t8.endsWith(e3)) {
                let i5 = v2[a3++], s5 = r7.getAttribute(t8).split(h2), e9 = /([.?@])?(.*)/.exec(i5);
                d3.push({ type: 1, index: c4, name: e9[2], strings: s5, ctor: e9[1] === "." ? k : e9[1] === "?" ? H : e9[1] === "@" ? I : R }), r7.removeAttribute(t8);
              } else
                t8.startsWith(h2) && (d3.push({ type: 6, index: c4 }), r7.removeAttribute(t8));
          if ($.test(r7.tagName)) {
            let t8 = r7.textContent.split(h2), s5 = t8.length - 1;
            if (s5 > 0) {
              r7.textContent = i3 ? i3.emptyScript : "";
              for (let i5 = 0; i5 < s5; i5++)
                r7.append(t8[i5], l2()), E.nextNode(), d3.push({ type: 2, index: ++c4 });
              r7.append(t8[s5], l2());
            }
          }
        } else if (r7.nodeType === 8)
          if (r7.data === o3)
            d3.push({ type: 2, index: c4 });
          else {
            let t8 = -1;
            for (; (t8 = r7.data.indexOf(h2, t8 + 1)) !== -1; )
              d3.push({ type: 7, index: c4 }), t8 += h2.length - 1;
          }
        c4++;
      }
    }
    static createElement(t7, i5) {
      let s4 = r3.createElement("template");
      return s4.innerHTML = t7, s4;
    }
  };
  function N(t7, i5, s4 = t7, e9) {
    var _a7, _b2, _c;
    if (i5 === w)
      return i5;
    let h3 = e9 !== void 0 ? (_a7 = s4._$Co) == null ? void 0 : _a7[e9] : s4._$Cl, o7 = c3(i5) ? void 0 : i5._$litDirective$;
    return (h3 == null ? void 0 : h3.constructor) !== o7 && ((_b2 = h3 == null ? void 0 : h3._$AO) == null || _b2.call(h3, !1), o7 === void 0 ? h3 = void 0 : (h3 = new o7(t7), h3._$AT(t7, s4, e9)), e9 !== void 0 ? ((_c = s4._$Co) != null ? _c : s4._$Co = [])[e9] = h3 : s4._$Cl = h3), h3 !== void 0 && (i5 = N(t7, h3._$AS(t7, i5.values), h3, e9)), i5;
  }
  var S2 = class {
    constructor(t7, i5) {
      this._$AV = [], this._$AN = void 0, this._$AD = t7, this._$AM = i5;
    }
    get parentNode() {
      return this._$AM.parentNode;
    }
    get _$AU() {
      return this._$AM._$AU;
    }
    u(t7) {
      var _a7;
      let { el: { content: i5 }, parts: s4 } = this._$AD, e9 = ((_a7 = t7 == null ? void 0 : t7.creationScope) != null ? _a7 : r3).importNode(i5, !0);
      E.currentNode = e9;
      let h3 = E.nextNode(), o7 = 0, n5 = 0, l3 = s4[0];
      for (; l3 !== void 0; ) {
        if (o7 === l3.index) {
          let i6;
          l3.type === 2 ? i6 = new M(h3, h3.nextSibling, this, t7) : l3.type === 1 ? i6 = new l3.ctor(h3, l3.name, l3.strings, this, t7) : l3.type === 6 && (i6 = new L(h3, this, t7)), this._$AV.push(i6), l3 = s4[++n5];
        }
        o7 !== (l3 == null ? void 0 : l3.index) && (h3 = E.nextNode(), o7++);
      }
      return E.currentNode = r3, e9;
    }
    p(t7) {
      let i5 = 0;
      for (let s4 of this._$AV)
        s4 !== void 0 && (s4.strings !== void 0 ? (s4._$AI(t7, s4, i5), i5 += s4.strings.length - 2) : s4._$AI(t7[i5])), i5++;
    }
  }, M = class _M {
    get _$AU() {
      var _a7, _b2;
      return (_b2 = (_a7 = this._$AM) == null ? void 0 : _a7._$AU) != null ? _b2 : this._$Cv;
    }
    constructor(t7, i5, s4, e9) {
      var _a7;
      this.type = 2, this._$AH = T, this._$AN = void 0, this._$AA = t7, this._$AB = i5, this._$AM = s4, this.options = e9, this._$Cv = (_a7 = e9 == null ? void 0 : e9.isConnected) != null ? _a7 : !0;
    }
    get parentNode() {
      let t7 = this._$AA.parentNode, i5 = this._$AM;
      return i5 !== void 0 && (t7 == null ? void 0 : t7.nodeType) === 11 && (t7 = i5.parentNode), t7;
    }
    get startNode() {
      return this._$AA;
    }
    get endNode() {
      return this._$AB;
    }
    _$AI(t7, i5 = this) {
      t7 = N(this, t7, i5), c3(t7) ? t7 === T || t7 == null || t7 === "" ? (this._$AH !== T && this._$AR(), this._$AH = T) : t7 !== this._$AH && t7 !== w && this._(t7) : t7._$litType$ !== void 0 ? this.g(t7) : t7.nodeType !== void 0 ? this.$(t7) : u2(t7) ? this.T(t7) : this._(t7);
    }
    k(t7) {
      return this._$AA.parentNode.insertBefore(t7, this._$AB);
    }
    $(t7) {
      this._$AH !== t7 && (this._$AR(), this._$AH = this.k(t7));
    }
    _(t7) {
      this._$AH !== T && c3(this._$AH) ? this._$AA.nextSibling.data = t7 : this.$(r3.createTextNode(t7)), this._$AH = t7;
    }
    g(t7) {
      var _a7;
      let { values: i5, _$litType$: s4 } = t7, e9 = typeof s4 == "number" ? this._$AC(t7) : (s4.el === void 0 && (s4.el = V.createElement(C(s4.h, s4.h[0]), this.options)), s4);
      if (((_a7 = this._$AH) == null ? void 0 : _a7._$AD) === e9)
        this._$AH.p(i5);
      else {
        let t8 = new S2(e9, this), s5 = t8.u(this.options);
        t8.p(i5), this.$(s5), this._$AH = t8;
      }
    }
    _$AC(t7) {
      let i5 = A.get(t7.strings);
      return i5 === void 0 && A.set(t7.strings, i5 = new V(t7)), i5;
    }
    T(t7) {
      a2(this._$AH) || (this._$AH = [], this._$AR());
      let i5 = this._$AH, s4, e9 = 0;
      for (let h3 of t7)
        e9 === i5.length ? i5.push(s4 = new _M(this.k(l2()), this.k(l2()), this, this.options)) : s4 = i5[e9], s4._$AI(h3), e9++;
      e9 < i5.length && (this._$AR(s4 && s4._$AB.nextSibling, e9), i5.length = e9);
    }
    _$AR(t7 = this._$AA.nextSibling, i5) {
      var _a7;
      for ((_a7 = this._$AP) == null ? void 0 : _a7.call(this, !1, !0, i5); t7 && t7 !== this._$AB; ) {
        let i6 = t7.nextSibling;
        t7.remove(), t7 = i6;
      }
    }
    setConnected(t7) {
      var _a7;
      this._$AM === void 0 && (this._$Cv = t7, (_a7 = this._$AP) == null || _a7.call(this, t7));
    }
  }, R = class {
    get tagName() {
      return this.element.tagName;
    }
    get _$AU() {
      return this._$AM._$AU;
    }
    constructor(t7, i5, s4, e9, h3) {
      this.type = 1, this._$AH = T, this._$AN = void 0, this.element = t7, this.name = i5, this._$AM = e9, this.options = h3, s4.length > 2 || s4[0] !== "" || s4[1] !== "" ? (this._$AH = Array(s4.length - 1).fill(new String()), this.strings = s4) : this._$AH = T;
    }
    _$AI(t7, i5 = this, s4, e9) {
      let h3 = this.strings, o7 = !1;
      if (h3 === void 0)
        t7 = N(this, t7, i5, 0), o7 = !c3(t7) || t7 !== this._$AH && t7 !== w, o7 && (this._$AH = t7);
      else {
        let e10 = t7, n5, r7;
        for (t7 = h3[0], n5 = 0; n5 < h3.length - 1; n5++)
          r7 = N(this, e10[s4 + n5], i5, n5), r7 === w && (r7 = this._$AH[n5]), o7 || (o7 = !c3(r7) || r7 !== this._$AH[n5]), r7 === T ? t7 = T : t7 !== T && (t7 += (r7 != null ? r7 : "") + h3[n5 + 1]), this._$AH[n5] = r7;
      }
      o7 && !e9 && this.O(t7);
    }
    O(t7) {
      t7 === T ? this.element.removeAttribute(this.name) : this.element.setAttribute(this.name, t7 != null ? t7 : "");
    }
  }, k = class extends R {
    constructor() {
      super(...arguments), this.type = 3;
    }
    O(t7) {
      this.element[this.name] = t7 === T ? void 0 : t7;
    }
  }, H = class extends R {
    constructor() {
      super(...arguments), this.type = 4;
    }
    O(t7) {
      this.element.toggleAttribute(this.name, !!t7 && t7 !== T);
    }
  }, I = class extends R {
    constructor(t7, i5, s4, e9, h3) {
      super(t7, i5, s4, e9, h3), this.type = 5;
    }
    _$AI(t7, i5 = this) {
      var _a7;
      if ((t7 = (_a7 = N(this, t7, i5, 0)) != null ? _a7 : T) === w)
        return;
      let s4 = this._$AH, e9 = t7 === T && s4 !== T || t7.capture !== s4.capture || t7.once !== s4.once || t7.passive !== s4.passive, h3 = t7 !== T && (s4 === T || e9);
      e9 && this.element.removeEventListener(this.name, this, s4), h3 && this.element.addEventListener(this.name, this, t7), this._$AH = t7;
    }
    handleEvent(t7) {
      var _a7, _b2;
      typeof this._$AH == "function" ? this._$AH.call((_b2 = (_a7 = this.options) == null ? void 0 : _a7.host) != null ? _b2 : this.element, t7) : this._$AH.handleEvent(t7);
    }
  }, L = class {
    constructor(t7, i5, s4) {
      this.element = t7, this.type = 6, this._$AN = void 0, this._$AM = i5, this.options = s4;
    }
    get _$AU() {
      return this._$AM._$AU;
    }
    _$AI(t7) {
      N(this, t7);
    }
  };
  var Z = t2.litHtmlPolyfillSupport, _a3;
  Z == null || Z(V, M), ((_a3 = t2.litHtmlVersions) != null ? _a3 : t2.litHtmlVersions = []).push("3.0.2");
  var j = (t7, i5, s4) => {
    var _a7, _b2;
    let e9 = (_a7 = s4 == null ? void 0 : s4.renderBefore) != null ? _a7 : i5, h3 = e9._$litPart$;
    if (h3 === void 0) {
      let t8 = (_b2 = s4 == null ? void 0 : s4.renderBefore) != null ? _b2 : null;
      e9._$litPart$ = h3 = new M(i5.insertBefore(l2(), t8), t8, void 0, s4 != null ? s4 : {});
    }
    return h3._$AI(t7), h3;
  };

  // node_modules/lit-element/lit-element.js
  var s3 = class extends b {
    constructor() {
      super(...arguments), this.renderOptions = { host: this }, this._$Do = void 0;
    }
    createRenderRoot() {
      var _a7, _b2;
      let t7 = super.createRenderRoot();
      return (_b2 = (_a7 = this.renderOptions).renderBefore) != null || (_a7.renderBefore = t7.firstChild), t7;
    }
    update(t7) {
      let i5 = this.render();
      this.hasUpdated || (this.renderOptions.isConnected = this.isConnected), super.update(t7), this._$Do = j(i5, this.renderRoot, this.renderOptions);
    }
    connectedCallback() {
      var _a7;
      super.connectedCallback(), (_a7 = this._$Do) == null || _a7.setConnected(!0);
    }
    disconnectedCallback() {
      var _a7;
      super.disconnectedCallback(), (_a7 = this._$Do) == null || _a7.setConnected(!1);
    }
    render() {
      return w;
    }
  }, _a4;
  s3._$litElement$ = !0, s3["finalized"] = !0, (_a4 = globalThis.litElementHydrateSupport) == null || _a4.call(globalThis, { LitElement: s3 });
  var r4 = globalThis.litElementPolyfillSupport;
  r4 == null || r4({ LitElement: s3 });
  var _a5;
  ((_a5 = globalThis.litElementVersions) != null ? _a5 : globalThis.litElementVersions = []).push("4.0.1");

  // tooldrawer/lib/livereloader.ts
  var Livereloader = class {
    constructor(config) {
      this._stale = !1;
      this._disabled = !1;
      this._listener = (event) => {
        this._shouldReload(event.data) && (this._stale = !0, this._disabled || this._reload());
      };
      this.artifactName = config.artifactName, new BroadcastChannel("live-reload").addEventListener(
        "message",
        this._listener
      );
      let workerPort = new SharedWorker(config.workerJs, {
        name: "livereload-worker"
      }).port;
      workerPort.start(), workerPort.postMessage(config);
    }
    get disabled() {
      return this._disabled;
    }
    set disabled(disabled) {
      this._disabled = disabled, !disabled && this._stale && this._reload();
    }
    _reload() {
      location.reload(), this._stale = !1;
    }
    _shouldReload(message) {
      switch (message.type) {
        case "restart":
          return !0;
        case "reload":
          return message.path === this.artifactName;
        default:
          return !1;
      }
    }
  };

  // tooldrawer/lib/marshall.ts
  var Marshall = class {
    constructor(propMap) {
      this.propMap = propMap;
    }
    serialize(value) {
      return JSON.stringify(
        Object.keys(this.propMap).reduce(
          (pick, name) => __spreadProps(__spreadValues({}, pick), { [name]: value[name] }),
          {}
        )
      );
    }
    /**
     * Deserialize saved state.
     *
     * Note that this may throw various exceptions if deserialization fails.
     */
    deserialize(serialized) {
      let data = JSON.parse(serialized != null ? serialized : ""), value = {};
      for (let prop in this.propMap) {
        let { validate } = this.propMap[prop];
        validate(data[prop]), value[prop] = data[prop];
      }
      return value;
    }
  }, marshallTypes = {
    boolean: {
      type: Boolean,
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      validate(v2) {
        if (typeof v2 != "boolean")
          throw new Error(`${v2} is not an boolean`);
      }
    },
    number: {
      type: Number,
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      validate(v2) {
        if (typeof v2 != "number" || isNaN(v2))
          throw new Error(`${v2} is not an number`);
      }
    }
  };

  // node_modules/@lit/reactive-element/decorators/custom-element.js
  var t3 = (t7) => (e9, o7) => {
    o7 !== void 0 ? o7.addInitializer(() => {
      customElements.define(t7, e9);
    }) : customElements.define(t7, e9);
  };

  // node_modules/@lit/reactive-element/decorators/property.js
  var o4 = { attribute: !0, type: String, converter: u, reflect: !1, hasChanged: f }, r5 = (t7 = o4, e9, r7) => {
    let { kind: n5, metadata: i5 } = r7, s4 = globalThis.litPropertyMetadata.get(i5);
    if (s4 === void 0 && globalThis.litPropertyMetadata.set(i5, s4 = /* @__PURE__ */ new Map()), s4.set(r7.name, t7), n5 === "accessor") {
      let { name: o7 } = r7;
      return { set(r8) {
        let n6 = e9.get.call(this);
        e9.set.call(this, r8), this.requestUpdate(o7, n6, t7);
      }, init(e10) {
        return e10 !== void 0 && this.C(o7, void 0, t7), e10;
      } };
    }
    if (n5 === "setter") {
      let { name: o7 } = r7;
      return function(r8) {
        let n6 = this[o7];
        e9.call(this, r8), this.requestUpdate(o7, n6, t7);
      };
    }
    throw Error("Unsupported decorator location: " + n5);
  };
  function n4(t7) {
    return (e9, o7) => typeof o7 == "object" ? r5(t7, e9, o7) : ((t8, e10, o8) => {
      let r7 = e10.hasOwnProperty(o8);
      return e10.constructor.createProperty(o8, r7 ? __spreadProps(__spreadValues({}, t8), { wrapped: !0 }) : t8), r7 ? Object.getOwnPropertyDescriptor(e10, o8) : void 0;
    })(t7, e9, o7);
  }

  // node_modules/@lit/reactive-element/decorators/state.js
  function r6(r7) {
    return n4(__spreadProps(__spreadValues({}, r7), { state: !0, attribute: !1 }));
  }

  // node_modules/@lit/reactive-element/decorators/event-options.js
  function t4(t7) {
    return (n5, o7) => {
      let c4 = typeof n5 == "function" ? n5 : n5[o7];
      Object.assign(c4, t7);
    };
  }

  // node_modules/@lit/reactive-element/decorators/base.js
  var e4 = (e9, t7, c4) => (c4.configurable = !0, c4.enumerable = !0, Reflect.decorate && typeof t7 != "object" && Object.defineProperty(e9, t7, c4), c4);

  // node_modules/@lit/reactive-element/decorators/query.js
  function e5(e9, r7) {
    return (n5, s4, i5) => {
      let o7 = (t7) => {
        var _a7, _b2;
        return (_b2 = (_a7 = t7.renderRoot) == null ? void 0 : _a7.querySelector(e9)) != null ? _b2 : null;
      };
      if (r7) {
        let { get: e10, set: u3 } = typeof s4 == "object" ? n5 : i5 != null ? i5 : (() => {
          let t7 = Symbol();
          return { get() {
            return this[t7];
          }, set(e11) {
            this[t7] = e11;
          } };
        })();
        return e4(n5, s4, { get() {
          if (r7) {
            let t7 = e10.call(this);
            return t7 === void 0 && (t7 = o7(this), u3.call(this, t7)), t7;
          }
          return o7(this);
        } });
      }
      return e4(n5, s4, { get() {
        return o7(this);
      } });
    };
  }

  // node_modules/lit-html/directive.js
  var t5 = { ATTRIBUTE: 1, CHILD: 2, PROPERTY: 3, BOOLEAN_ATTRIBUTE: 4, EVENT: 5, ELEMENT: 6 }, e6 = (t7) => (...e9) => ({ _$litDirective$: t7, values: e9 }), i4 = class {
    constructor(t7) {
    }
    get _$AU() {
      return this._$AM._$AU;
    }
    _$AT(t7, e9, i5) {
      this._$Ct = t7, this._$AM = e9, this._$Ci = i5;
    }
    _$AS(t7, e9) {
      return this.update(t7, e9);
    }
    update(t7, e9) {
      return this.render(...e9);
    }
  };

  // node_modules/lit-html/directives/class-map.js
  var e7 = e6(class extends i4 {
    constructor(t7) {
      var _a7;
      if (super(t7), t7.type !== t5.ATTRIBUTE || t7.name !== "class" || ((_a7 = t7.strings) == null ? void 0 : _a7.length) > 2)
        throw Error("`classMap()` can only be used in the `class` attribute and must be the only part in the attribute.");
    }
    render(t7) {
      return " " + Object.keys(t7).filter((s4) => t7[s4]).join(" ") + " ";
    }
    update(s4, [i5]) {
      var _a7, _b2;
      if (this.it === void 0) {
        this.it = /* @__PURE__ */ new Set(), s4.strings !== void 0 && (this.st = new Set(s4.strings.join(" ").split(/\s/).filter((t7) => t7 !== "")));
        for (let t7 in i5)
          i5[t7] && !((_a7 = this.st) != null && _a7.has(t7)) && this.it.add(t7);
        return this.render(i5);
      }
      let r7 = s4.element.classList;
      for (let t7 of this.it)
        t7 in i5 || (r7.remove(t7), this.it.delete(t7));
      for (let t7 in i5) {
        let s5 = !!i5[t7];
        s5 === this.it.has(t7) || (_b2 = this.st) != null && _b2.has(t7) || (s5 ? (r7.add(t7), this.it.add(t7)) : (r7.remove(t7), this.it.delete(t7)));
      }
      return w;
    }
  });

  // tooldrawer/components/controllers/window-event-listener.ts
  var WindowEventListenerController = class {
    constructor(host, options) {
      this._connected = !1;
      this._windowEventListeners = /* @__PURE__ */ new Map();
      this._listener = (event) => {
        var _a7;
        (_a7 = this._windowEventListeners.get(event.type)) == null || _a7.map((listener) => listener.call(this.host, event));
      };
      this.host = host, this.options = options != null ? options : {}, host.addController(this);
    }
    hostConnected() {
      for (let [eventType] of this._windowEventListeners)
        window.addEventListener(eventType, this._listener, this.options);
      this._connected = !0;
    }
    hostDisconnected() {
      this._removeHandlers(), this._connected = !1;
    }
    add(eventType, listener) {
      let listeners = this._windowEventListeners.get(eventType);
      listeners ? listeners.push(listener) : (this._connected && window.addEventListener(eventType, this._listener, this.options), this._windowEventListeners.set(eventType, [listener]));
    }
    clear() {
      this._removeHandlers(), this._windowEventListeners.clear();
    }
    _removeHandlers() {
      for (let [eventType] of this._windowEventListeners)
        window.removeEventListener(eventType, this._listener, this.options);
    }
  };

  // tooldrawer/components/widget.ts
  function WidgetMixin(Base) {
    class WidgetClass extends Base {
      constructor() {
        super(...arguments);
        this.widgetRole = "widget";
        this.label = "";
      }
    }
    return __decorateClass([
      n4({ attribute: !1 })
    ], WidgetClass.prototype, "widgetRole", 2), __decorateClass([
      n4()
    ], WidgetClass.prototype, "label", 2), __decorateClass([
      n4()
    ], WidgetClass.prototype, "tooltip", 2), WidgetClass;
  }

  // tooldrawer/components/drag-handle.ts
  var DragEvent = class extends Event {
    constructor(type_, init) {
      super(type_, init);
      this.clientX = init.clientX, this.clientY = init.clientY;
    }
  }, DragHandle = class extends s3 {
    constructor() {
      super(...arguments);
      this._dragging = !1;
      this._windowEventListeners = new WindowEventListenerController(this, {
        passive: !0,
        capture: !0
      });
    }
    render() {
      return x`
      <div
        id="handle"
        aria-hidden="true"
        title="Drag to reposition"
        @mousedown=${this._onmousedown}
        @touchstart=${this._ontouchstart}
      >
        <div id="icon"></div>
      </div>
      ${this._dragging ? x`<div id="cover"></div>` : null}
    `;
    }
    _onmousedown(event) {
      event.buttons === 1 && (event.preventDefault(), this._windowEventListeners.add("mousemove", this._onmousemove), this._windowEventListeners.add("mouseup", this._dragStop), this._drag("drag-start", event));
    }
    _onmousemove(event) {
      event.buttons !== 1 ? this._dragStop() : this._drag("drag-move", event);
    }
    _ontouchstart(event) {
      event.targetTouches.length === 1 && (this._windowEventListeners.add("touchmove", this._ontouchmove), this._windowEventListeners.add("touchend", this._dragStop), this._windowEventListeners.add("touchcancel", this._dragStop), this._drag("drag-start", event.targetTouches[0]));
    }
    _ontouchmove(event) {
      event.targetTouches.length !== 1 ? this._dragStop() : this._drag("drag-move", event.targetTouches[0]);
    }
    _drag(eventType, pos) {
      this._dragging = !0, this.dispatchEvent(
        new DragEvent(eventType, {
          bubbles: !0,
          composed: !0,
          clientX: pos.clientX,
          clientY: pos.clientY
        })
      );
    }
    _dragStop() {
      this._dragging = !1, this._windowEventListeners.clear(), this.dispatchEvent(
        new Event("drag-stop", { bubbles: !0, composed: !0 })
      );
    }
  };
  DragHandle.styles = i`
    #handle {
      --dot-size: 6px;
      --margin: 2px;
      cursor: grab;
      width: calc(2 * var(--dot-size) + 2 * var(--margin));
      height: 100%;
      display: flex;
    }
    #icon {
      margin: var(--margin);
      flex-grow: 1;
      background: radial-gradient(currentcolor 35%, transparent 45%) left /
        var(--dot-size) var(--dot-size) repeat space;
    }

    #cover {
      position: fixed;
      top: 0;
      left: 0;
      bottom: 0;
      right: 0;
      z-index: 10000;
      cursor: grabbing;
    }
  `, __decorateClass([
    r6()
  ], DragHandle.prototype, "_dragging", 2), __decorateClass([
    t4({ passive: !0, capture: !0 })
  ], DragHandle.prototype, "_ontouchstart", 1), DragHandle = __decorateClass([
    t3("lektor-drag-handle")
  ], DragHandle);

  // node_modules/lit-html/directives/unsafe-html.js
  var e8 = class extends i4 {
    constructor(i5) {
      if (super(i5), this.et = T, i5.type !== t5.CHILD)
        throw Error(this.constructor.directiveName + "() can only be used in child bindings");
    }
    render(r7) {
      if (r7 === T || r7 == null)
        return this.vt = void 0, this.et = r7;
      if (r7 === w)
        return r7;
      if (typeof r7 != "string")
        throw Error(this.constructor.directiveName + "() called with a non-string value");
      if (r7 === this.et)
        return this.vt;
      this.et = r7;
      let s4 = [r7];
      return s4.raw = s4, this.vt = { _$litType$: this.constructor.resultType, strings: s4, values: [] };
    }
  };
  e8.directiveName = "unsafeHTML", e8.resultType = 1;
  var o5 = e6(e8);

  // node_modules/lit-html/directives/unsafe-svg.js
  var t6 = class extends e8 {
  };
  t6.directiveName = "unsafeSVG", t6.resultType = 2;
  var o6 = e6(t6);

  // tooldrawer/components/icon.ts
  var iconSvg = new Map(
    Object.entries(define_SVG_ICONS_FONTAWESOME_default != null ? define_SVG_ICONS_FONTAWESOME_default : {}).map(([name, svg]) => [
      name,
      x`${o6(svg)}`
    ])
  );
  iconSvg.size > 0 || console.warn("No icon data is available");
  var LektorIcon = class extends s3 {
    constructor() {
      super(...arguments);
      this.icon = "";
    }
    render() {
      return iconSvg.get(this.icon);
    }
  };
  LektorIcon.styles = i`
    :host {
      width: 1em;
      display: flex;
      place-items: center stretch;
    }
  `, __decorateClass([
    n4()
  ], LektorIcon.prototype, "icon", 2), LektorIcon = __decorateClass([
    t3("lektor-icon")
  ], LektorIcon);

  // tooldrawer/components/drawer.ts
  var LektorDrawer = class extends WidgetMixin(s3) {
    constructor() {
      super();
      this.widgetRole = "menubar";
      this.open = !0;
      this.clientY = 5;
      this._closing = !1;
      new WindowEventListenerController(this).add("resize", this._clampPosition), this._hostStyle = getComputedStyle(this);
    }
    firstUpdated() {
      this._clampPosition();
    }
    willUpdate(changedProperties) {
      this._closing = changedProperties.has("open") && !this.open && this.hasUpdated && this._drawer.matches(":hover"), changedProperties.has("clientY") && this._clampPosition();
    }
    /**
     * Clamp vertical position of tool drawer to ensure that it is visible.
     */
    _clampPosition() {
      if (this.hasUpdated) {
        let marginTop = parseInt(this._hostStyle.marginTop), marginBottom = parseInt(this._hostStyle.marginBottom), ymax = window.innerHeight - this._drawer.offsetHeight - marginBottom;
        this.clientY = Math.max(marginTop, Math.min(ymax, this.clientY));
      }
    }
    render() {
      var _a7;
      return x`
      <div
        id="drawer"
        role="menubar"
        class=${e7({
        open: this.open,
        closing: this._closing
      })}
        style="top: ${this.clientY}px;"
        @keydown=${this._onkeydown}
        @mouseleave=${this._closing ? this._mouseleave : T}
        title=${((_a7 = this.tooltip) != null ? _a7 : this.label) || T}
        aria-label=${this.label}
      >
        ${this._renderToggle()}
        <slot></slot>
        ${this._renderDragHandle()}
      </div>
    `;
    }
    _mouseleave() {
      this._closing = !1;
    }
    _onkeydown(event) {
      let navKeyFocusNextMap = {
        ArrowLeft: (cur) => cur.previousElementSibling,
        ArrowRight: (cur) => cur.nextElementSibling,
        Home: (cur) => {
          var _a7;
          return (_a7 = cur.parentElement) == null ? void 0 : _a7.firstElementChild;
        },
        End: (cur) => {
          var _a7;
          return (_a7 = cur.parentElement) == null ? void 0 : _a7.lastElementChild;
        },
        ArrowUp: () => null,
        ArrowDown: () => null
      };
      if (event.code in navKeyFocusNextMap) {
        let keycode = event.code, focused = event.target, focusNext = navKeyFocusNextMap[keycode](focused);
        event.preventDefault(), focusNext instanceof HTMLElement && focusNext.focus();
      }
    }
    _renderToggle() {
      return x`
      <div
        id="toggle"
        class="control"
        title="Click to hide/show drawer"
        aria-hidden="true"
        @click=${this._toggle}
      >
        <lektor-icon id="icon-open" .icon=${"faAngleRight"}></lektor-icon>
        <lektor-icon id="icon-closed" .icon=${"faAngleLeft"}></lektor-icon>
        <lektor-icon id="icon-hovered" .icon=${"faThumbtack"}></lektor-icon>
      </div>
    `;
    }
    _toggle() {
      this.open = !this.open, this.dispatchEvent(new Event("change", { bubbles: !0 }));
    }
    _renderDragHandle() {
      return x`
      <lektor-drag-handle
        class="control"
        @drag-start=${this._ondragstart}
        @drag-move=${this._ondragmove}
        @drag-stop=${this._ondragstop}
      ></lektor-drag-handle>
    `;
    }
    _ondragstart(event) {
      this._dragOffset = this.clientY - event.clientY;
    }
    _ondragmove(event) {
      this.clientY = event.clientY + this._dragOffset;
    }
    _ondragstop() {
      this.dispatchEvent(new Event("change", { bubbles: !0 }));
    }
  };
  LektorDrawer.styles = i`
    :host {
      /* The top and bottom margins of the host are used to set
       * limits the drag range of the drawer. */
      margin: 5px 0px;
    }
    #drawer {
      position: fixed;
      right: 0;
      z-index: 1000;

      min-height: 32px; /* 2rem */
      color: var(--lektor-drawer-color, hsl(336, 16%, 50%));
      background-color: var(--lektor-drawer-bg, hsla(24, 5%, 85%, 0.87));
      border: 1px solid var(--lektor-drawer-border-color, hsl(24, 2%, 67%));
      border-right: none;
      border-radius: 3px 0 0 3px;

      display: flex;

      /* move drawer off-screen to the right just enough to leave the toggle control visible */
      transform: translateX(calc(100% - 17px));
      transition: transform 0.5s ease-out;
    }
    #drawer.open,
    #drawer:not(.closing):where(:hover, :active, :focus-within) {
      /* open drawer */
      transform: none;
    }

    .control:is(:hover, :active) {
      color: var(--lektor-drawer-hover-color, hsl(336, 43%, 33%));
    }

    #toggle {
      cursor: pointer;
      display: flex;
      align-items: center;
    }
    lektor-icon {
      width: 12px;
      margin: 2px;
    }
    #drawer:not(.open) #icon-open,
    #drawer:where(.open, .closing, :not(:hover, :active, :focus-within))
      #icon-hovered,
    #drawer:where(.open, :not(.closing):where(:hover, :active, :focus-within))
      #icon-closed {
      display: none;
    }

    ::slotted(*) {
      font-size: 28px;
    }

    slot {
      margin: 3px;
      display: flex;
      align-items: center;
      gap: 3px;
    }
  `, __decorateClass([
    n4({ attribute: !1 })
  ], LektorDrawer.prototype, "widgetRole", 2), __decorateClass([
    n4({ type: Boolean, reflect: !0 })
  ], LektorDrawer.prototype, "open", 2), __decorateClass([
    n4({ attribute: !1 })
  ], LektorDrawer.prototype, "clientY", 2), __decorateClass([
    r6()
  ], LektorDrawer.prototype, "_closing", 2), __decorateClass([
    e5("#drawer", !0)
  ], LektorDrawer.prototype, "_drawer", 2), LektorDrawer = __decorateClass([
    t3("lektor-drawer")
  ], LektorDrawer);

  // tooldrawer/components/css/button.ts
  var button_default = i`
  .button {
    --default-color: hsl(336, 33%, 43%);
    --default-border-color: hsl(24, 2%, 80%);

    padding: 2px 3px;
    border: 1px outset
      var(--lektor-button-border-color, var(--default-border-color));
    border-radius: 3px;

    color: var(--lektor-button-color, var(--default-color));
    background-color: var(--lektor-button-bg, hsl(24, 5%, 93%));

    aspect-ratio: 1/1;
    cursor: pointer;
  }
  .button:hover {
    color: var(--lektor-button-hover-color, var(--default-color));
    background-color: var(--lektor-button-hover-bg, hsl(24, 7%, 98%));
    border-color: var(--lektor-button-border-hover-color, hsl(24, 2%, 67%));
  }
  .button:active,
  .button.active:not(:hover) {
    color: var(--lektor-button-active-color, var(--default-color));
    background-color: var(--lektor-button-active-bg, hsl(24, 5%, 87%));
    border-color: var(
      --lektor-button-border-active-color,
      var(--default-border-color)
    );
  }
  .button:active,
  .button.active {
    border-style: inset;
  }

  .button {
    display: flex;
    justify-content: center;
    align-items: center;
  }
`;

  // tooldrawer/components/link-button.ts
  var LinkButton = class extends WidgetMixin(s3) {
    constructor() {
      super(...arguments);
      this.href = "";
      this.widgetRole = "link";
    }
    render() {
      var _a7;
      return x`
      <a
        href=${this.href}
        class="button"
        role=${this.widgetRole !== "link" ? this.widgetRole : T}
        title=${((_a7 = this.tooltip) != null ? _a7 : this.label) || T}
        aria-label=${this.label}
      >
        <slot></slot>
      </a>
    `;
    }
  };
  LinkButton.shadowRootOptions = __spreadProps(__spreadValues({}, s3.shadowRootOptions), {
    delegatesFocus: !0
  }), LinkButton.styles = button_default, __decorateClass([
    n4()
  ], LinkButton.prototype, "href", 2), __decorateClass([
    n4({ attribute: !1 })
  ], LinkButton.prototype, "widgetRole", 2), LinkButton = __decorateClass([
    t3("lektor-link-button")
  ], LinkButton);

  // tooldrawer/components/css/visually-hidden.ts
  var visually_hidden_default = i`
  .visually-hidden {
    position: absolute;
    height: 1px;
    width: 1px;
    clip: rect(0 0 0 0);
    clip-path: inset(50%);
    overflow: hidden;
    white-space: nowrap;
  }
`;

  // tooldrawer/components/checkbox-button.ts
  var CheckboxButton = class extends WidgetMixin(s3) {
    constructor() {
      super(...arguments);
      this.checked = !1;
      this.widgetRole = "checkbox";
    }
    render() {
      var _a7;
      return x`
      <input
        id="cb"
        type="checkbox"
        class="visually-hidden"
        .checked=${this.checked}
        @change=${this._onchange}
        @keyup=${this._onkeyup}
        role=${this.widgetRole !== "checkbox" ? this.widgetRole : T}
        aria-checked=${this.widgetRole === "switch" ? this.checked : T}
      />
      <label
        for="cb"
        class=${e7({ button: !0, active: this.checked })}
        title=${((_a7 = this.tooltip) != null ? _a7 : this.label) || T}
      >
        <span class="visually-hidden">${this.label}</span>
        <slot></slot>
      </label>
    `;
    }
    _onchange() {
      this.checked = this._checkbox.checked, this.dispatchEvent(new Event("change", { bubbles: !0 }));
    }
    _onkeyup(event) {
      event.code === "Enter" && (event.preventDefault(), this.checked = !this.checked);
    }
  };
  CheckboxButton.shadowRootOptions = __spreadProps(__spreadValues({}, s3.shadowRootOptions), {
    delegatesFocus: !0
  }), CheckboxButton.styles = [
    button_default,
    visually_hidden_default,
    i`
      /*
       * Attempt to replicate browser's native focus style for the label
       *
       * https://css-tricks.com/copy-the-browsers-native-focus-styles/
       */
      input:focus-visible + label {
        outline: 5px auto black;
        outline-offset: 1px;
        outline-color: Highlight;
        outline-color: -webkit-focus-ring-color;
      }
    `
  ], __decorateClass([
    n4({ type: Boolean, reflect: !0 })
  ], CheckboxButton.prototype, "checked", 2), __decorateClass([
    n4({ attribute: !1 })
  ], CheckboxButton.prototype, "widgetRole", 2), __decorateClass([
    e5("input", !0)
  ], CheckboxButton.prototype, "_checkbox", 2), CheckboxButton = __decorateClass([
    t3("lektor-checkbox-button")
  ], CheckboxButton);

  // tooldrawer/components/livereload-widget.ts
  var LivereloadWidget = class extends WidgetMixin(s3) {
    constructor() {
      super(...arguments);
      this.livereloadDisabled = !0;
      this.widgetRole = "switch";
      this._queryParam = new QueryParamController(this, {
        paramName: "livereload"
      });
    }
    willUpdate() {
      this.livereloader && (this.livereloader.disabled = this.livereloadDisabled);
    }
    render() {
      return x`
      <lektor-checkbox-button
        .checked=${!this.livereloadDisabled}
        @change=${this._onchange}
        .widgetRole=${this.widgetRole}
        .label=${this.label}
        .tooltip=${this.tooltip}
      >
        <lektor-icon icon="faRetweet"></lektor-icon>
      </lektor-checkbox-button>
    `;
    }
    _onchange() {
      this.livereloadDisabled = this._queryParam.disabled = !this._checkbox.checked, this.dispatchEvent(new Event("change", { bubbles: !0 }));
    }
  };
  LivereloadWidget.shadowRootOptions = __spreadProps(__spreadValues({}, s3.shadowRootOptions), {
    delegatesFocus: !0
  }), LivereloadWidget.styles = i`
    lektor-icon {
      position: relative;
    }
    lektor-checkbox-button:not([checked]) lektor-icon::before {
      /* red slash over icon when unchecked */
      --slash-color: var(--lektor-button-slash-color, hsl(349, 80%, 45%));
      content: "";
      position: absolute;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(
        to left top,
        transparent 45%,
        var(--slash-color) 46%,
        var(--slash-color) 54%,
        transparent 55%
      );
      opacity: 0.9;
    }
  `, __decorateClass([
    n4({ attribute: !1 })
  ], LivereloadWidget.prototype, "livereloadDisabled", 2), __decorateClass([
    n4({ attribute: !1 })
  ], LivereloadWidget.prototype, "livereloader", 2), __decorateClass([
    n4({ attribute: !1 })
  ], LivereloadWidget.prototype, "widgetRole", 2), __decorateClass([
    e5("lektor-checkbox-button", !0)
  ], LivereloadWidget.prototype, "_checkbox", 2), LivereloadWidget = __decorateClass([
    t3("lektor-livereload-widget")
  ], LivereloadWidget);
  var QueryParamController = class {
    constructor(host, { paramName }) {
      this._update = () => {
        let disabled = this.disabled;
        !!this.host.livereloadDisabled !== disabled && (this.host.livereloadDisabled = disabled, this.host.dispatchEvent(new Event("change", { bubbles: !0 })));
      };
      this.host = host, this.paramName = paramName, host.addController(this);
    }
    hostConnected() {
      window.addEventListener("popstate", this._update), window.addEventListener("load", this._update), this._update();
    }
    hostDisconnected() {
      window.removeEventListener("popstate", this._update), window.removeEventListener("load", this._update), this.host.livereloadDisabled = !0;
    }
    get disabled() {
      let value = new URLSearchParams(location.search).get(this.paramName);
      return /^(false|no|0)$/i.test(value || "");
    }
    set disabled(value) {
      if (!!value !== this.disabled) {
        let url = new URL(window.location.href);
        value ? url.searchParams.set(this.paramName, "false") : url.searchParams.delete(this.paramName), window.history.pushState(null, "", url.href);
      }
    }
  };

  // tooldrawer/index.ts
  var _a6, { editUrl, livereloadConfig } = (_a6 = globalThis.TOOLDRAWER_CONFIG) != null ? _a6 : {};
  window === window.top && (editUrl || livereloadConfig) && document.addEventListener(
    "DOMContentLoaded",
    () => {
      j(tooldrawer({ editUrl, livereloadConfig }), document.body), persistDrawerState(document.getElementsByTagName("lektor-drawer")[0]);
    },
    { once: !0 }
  );
  function tooldrawer({ editUrl: editUrl2, livereloadConfig: livereloadConfig2 }) {
    let tools = new Array();
    if (editUrl2 && tools.push(x`
      <lektor-link-button
        .href=${editUrl2}
        .widgetRole=${"menuitem"}
        .label=${"Edit Page"}
      >
        <lektor-icon icon="faFilePen"></lektor-icon>
      </lektor-link-button>
    `), livereloadConfig2) {
      let livereloader = new Livereloader(livereloadConfig2);
      tools.push(x`
      <lektor-livereload-widget
        .widgetRole=${"menuitemcheckbox"}
        .label=${"Enable Live-Reload"}
        .livereloader=${livereloader}
      ></lektor-livereload-widget>
    `);
    }
    return x`
    <lektor-drawer .widgetRole=${"menubar"} .label=${"Lektor Controls"}>
      ${tools}
    </lektor-drawer>
  `;
  }
  function persistDrawerState(drawer) {
    var _a7;
    let storage = localStorage, storageKey = "com.getlektor--tooldrawer-state", marshall = new Marshall({
      open: marshallTypes.boolean,
      clientY: marshallTypes.number
    });
    try {
      let savedState = marshall.deserialize(
        (_a7 = storage.getItem(storageKey)) != null ? _a7 : "{}"
      );
      Object.assign(drawer, savedState);
    } catch (err) {
      console.log("ignoring invalid saved drawer state: %o", err);
    }
    drawer.addEventListener("change", () => {
      storage.setItem(storageKey, marshall.serialize(drawer));
    });
  }
})();
/*! Bundled license information:

@lit/reactive-element/css-tag.js:
  (**
   * @license
   * Copyright 2019 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

@lit/reactive-element/reactive-element.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

lit-html/lit-html.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

lit-element/lit-element.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

lit-html/is-server.js:
  (**
   * @license
   * Copyright 2022 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

@lit/reactive-element/decorators/custom-element.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

@lit/reactive-element/decorators/property.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

@lit/reactive-element/decorators/state.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

@lit/reactive-element/decorators/event-options.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

@lit/reactive-element/decorators/base.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

@lit/reactive-element/decorators/query.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

@lit/reactive-element/decorators/query-all.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

@lit/reactive-element/decorators/query-async.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

@lit/reactive-element/decorators/query-assigned-elements.js:
  (**
   * @license
   * Copyright 2021 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

@lit/reactive-element/decorators/query-assigned-nodes.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

lit-html/directive.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

lit-html/directives/class-map.js:
  (**
   * @license
   * Copyright 2018 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

lit-html/directives/unsafe-html.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)

lit-html/directives/unsafe-svg.js:
  (**
   * @license
   * Copyright 2017 Google LLC
   * SPDX-License-Identifier: BSD-3-Clause
   *)
*/
//# sourceMappingURL=tooldrawer.js.map
