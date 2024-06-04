let he = null;
async function Bt() {
  return he || (he = (await import("./re_viewer-DOCTrs8v.js")).WebHandle, he);
}
function Dt() {
  const l = new Uint8Array(16);
  return crypto.getRandomValues(l), Array.from(l).map((e) => e.toString(16).padStart(2, "0")).join("");
}
class Ht {
  /** @type {(import("./re_viewer.js").WebHandle) | null} */
  #e = null;
  /** @type {HTMLCanvasElement | null} */
  #n = null;
  /** @type {'ready' | 'starting' | 'stopped'} */
  #t = "stopped";
  /**
   * Start the viewer.
   *
   * @param {string | string[]} [rrd] URLs to `.rrd` files or WebSocket connections to our SDK.
   * @param {HTMLElement} [parent] The element to attach the canvas onto.
   * @param {boolean} [hide_welcome_screen] Whether to hide the welcome screen.
   * @returns {Promise<void>}
   */
  async start(e, t = document.body, n = !1) {
    if (this.#t !== "stopped")
      return;
    this.#t = "starting", this.#n = document.createElement("canvas"), this.#n.id = Dt(), t.append(this.#n);
    let i = await Bt();
    if (this.#t === "starting" && (this.#e = new i(), await this.#e.start(
      this.#n.id,
      void 0,
      void 0,
      void 0,
      n
    ), this.#t === "starting")) {
      if (this.#e.has_panicked())
        throw new Error(`Web viewer crashed: ${this.#e.panic_message()}`);
      this.#t = "ready", e && this.open(e);
    }
  }
  /**
   * Returns `true` if the viewer is ready to connect to data sources.
   */
  get ready() {
    return this.#t === "ready";
  }
  /**
   * Open a recording.
   *
   * The viewer must have been started via `WebViewer.start`.
   *
   * @see {WebViewer.start}
   *
   * @param {string | string[]} rrd URLs to `.rrd` files or WebSocket connections to our SDK.
   * @param {{ follow_if_http?: boolean }} options
   *        - follow_if_http: Whether Rerun should open the resource in "Following" mode when streaming
   *        from an HTTP url. Defaults to `false`. Ignored for non-HTTP URLs.
   */
  open(e, t = {}) {
    if (!this.#e)
      throw new Error(`attempted to open \`${e}\` in a stopped viewer`);
    const n = Array.isArray(e) ? e : [e];
    for (const i of n)
      if (this.#e.add_receiver(i, t.follow_if_http), this.#e.has_panicked())
        throw new Error(`Web viewer crashed: ${this.#e.panic_message()}`);
  }
  /**
   * Close a recording.
   *
   * The viewer must have been started via `WebViewer.start`.
   *
   * @see {WebViewer.start}
   *
   * @param {string | string[]} rrd URLs to `.rrd` files or WebSocket connections to our SDK.
   */
  close(e) {
    if (!this.#e)
      throw new Error(`attempted to close \`${e}\` in a stopped viewer`);
    const t = Array.isArray(e) ? e : [e];
    for (const n of t)
      if (this.#e.remove_receiver(n), this.#e.has_panicked())
        throw new Error(`Web viewer crashed: ${this.#e.panic_message()}`);
  }
  /**
   * Stop the viewer, freeing all associated memory.
   *
   * The same viewer instance may be started multiple times.
   */
  stop() {
    this.#t !== "stopped" && (this.#t = "stopped", this.#n?.remove(), this.#e?.destroy(), this.#e?.free(), this.#n = null, this.#e = null);
  }
  /**
   * Opens a new channel for sending log messages.
   *
   * The channel can be used to incrementally push `rrd` chunks into the viewer.
   *
   * @param {string} channel_name used to identify the channel.
   *
   * @returns {LogChannel}
   */
  open_channel(e = "rerun-io/web-viewer") {
    if (!this.#e)
      throw new Error("...");
    const t = crypto.randomUUID();
    this.#e.open_channel(t, e);
    const n = (o) => {
      if (!this.#e)
        throw new Error("...");
      this.#e.send_rrd_to_channel(t, o);
    }, i = () => {
      if (!this.#e)
        throw new Error("...");
      this.#e.close_channel(t);
    }, s = () => this.#t;
    return new Ot(n, i, s);
  }
}
class Ot {
  #e;
  #n;
  #t;
  #l = !1;
  /** @internal
   *
   * @param {(data: Uint8Array) => void} on_send
   * @param {() => void} on_close
   * @param {() => 'ready' | 'starting' | 'stopped'} get_state
   */
  constructor(e, t, n) {
    this.#e = e, this.#n = t, this.#t = n;
  }
  get ready() {
    return !this.#l && this.#t() === "ready";
  }
  /**
   * Send an `rrd` containing log messages to the viewer.
   *
   * Does nothing if `!this.ready`.
   *
   * @param {Uint8Array} rrd_bytes Is an rrd file stored in a byte array, received via some other side channel.
   */
  send_rrd(e) {
    this.ready && this.#e(e);
  }
  /**
   * Close the channel.
   *
   * Does nothing if `!this.ready`.
   */
  close() {
    this.ready && (this.#n(), this.#l = !0);
  }
}
const {
  SvelteComponent: Tt,
  assign: Ut,
  create_slot: Jt,
  detach: Rt,
  element: Xt,
  get_all_dirty_from_scope: Yt,
  get_slot_changes: Gt,
  get_spread_update: Kt,
  init: Qt,
  insert: xt,
  safe_not_equal: $t,
  set_dynamic_element_data: Pe,
  set_style: V,
  toggle_class: B,
  transition_in: dt,
  transition_out: mt,
  update_slot_base: en
} = window.__gradio__svelte__internal;
function tn(l) {
  let e, t, n;
  const i = (
    /*#slots*/
    l[18].default
  ), s = Jt(
    i,
    l,
    /*$$scope*/
    l[17],
    null
  );
  let o = [
    { "data-testid": (
      /*test_id*/
      l[7]
    ) },
    { id: (
      /*elem_id*/
      l[2]
    ) },
    {
      class: t = "block " + /*elem_classes*/
      l[3].join(" ") + " svelte-nl1om8"
    }
  ], a = {};
  for (let r = 0; r < o.length; r += 1)
    a = Ut(a, o[r]);
  return {
    c() {
      e = Xt(
        /*tag*/
        l[14]
      ), s && s.c(), Pe(
        /*tag*/
        l[14]
      )(e, a), B(
        e,
        "hidden",
        /*visible*/
        l[10] === !1
      ), B(
        e,
        "padded",
        /*padding*/
        l[6]
      ), B(
        e,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), B(
        e,
        "border_contrast",
        /*border_mode*/
        l[5] === "contrast"
      ), B(e, "hide-container", !/*explicit_call*/
      l[8] && !/*container*/
      l[9]), V(
        e,
        "height",
        /*get_dimension*/
        l[15](
          /*height*/
          l[0]
        )
      ), V(e, "width", typeof /*width*/
      l[1] == "number" ? `calc(min(${/*width*/
      l[1]}px, 100%))` : (
        /*get_dimension*/
        l[15](
          /*width*/
          l[1]
        )
      )), V(
        e,
        "border-style",
        /*variant*/
        l[4]
      ), V(
        e,
        "overflow",
        /*allow_overflow*/
        l[11] ? "visible" : "hidden"
      ), V(
        e,
        "flex-grow",
        /*scale*/
        l[12]
      ), V(e, "min-width", `calc(min(${/*min_width*/
      l[13]}px, 100%))`), V(e, "border-width", "var(--block-border-width)");
    },
    m(r, f) {
      xt(r, e, f), s && s.m(e, null), n = !0;
    },
    p(r, f) {
      s && s.p && (!n || f & /*$$scope*/
      131072) && en(
        s,
        i,
        r,
        /*$$scope*/
        r[17],
        n ? Gt(
          i,
          /*$$scope*/
          r[17],
          f,
          null
        ) : Yt(
          /*$$scope*/
          r[17]
        ),
        null
      ), Pe(
        /*tag*/
        r[14]
      )(e, a = Kt(o, [
        (!n || f & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          r[7]
        ) },
        (!n || f & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          r[2]
        ) },
        (!n || f & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        r[3].join(" ") + " svelte-nl1om8")) && { class: t }
      ])), B(
        e,
        "hidden",
        /*visible*/
        r[10] === !1
      ), B(
        e,
        "padded",
        /*padding*/
        r[6]
      ), B(
        e,
        "border_focus",
        /*border_mode*/
        r[5] === "focus"
      ), B(
        e,
        "border_contrast",
        /*border_mode*/
        r[5] === "contrast"
      ), B(e, "hide-container", !/*explicit_call*/
      r[8] && !/*container*/
      r[9]), f & /*height*/
      1 && V(
        e,
        "height",
        /*get_dimension*/
        r[15](
          /*height*/
          r[0]
        )
      ), f & /*width*/
      2 && V(e, "width", typeof /*width*/
      r[1] == "number" ? `calc(min(${/*width*/
      r[1]}px, 100%))` : (
        /*get_dimension*/
        r[15](
          /*width*/
          r[1]
        )
      )), f & /*variant*/
      16 && V(
        e,
        "border-style",
        /*variant*/
        r[4]
      ), f & /*allow_overflow*/
      2048 && V(
        e,
        "overflow",
        /*allow_overflow*/
        r[11] ? "visible" : "hidden"
      ), f & /*scale*/
      4096 && V(
        e,
        "flex-grow",
        /*scale*/
        r[12]
      ), f & /*min_width*/
      8192 && V(e, "min-width", `calc(min(${/*min_width*/
      r[13]}px, 100%))`);
    },
    i(r) {
      n || (dt(s, r), n = !0);
    },
    o(r) {
      mt(s, r), n = !1;
    },
    d(r) {
      r && Rt(e), s && s.d(r);
    }
  };
}
function nn(l) {
  let e, t = (
    /*tag*/
    l[14] && tn(l)
  );
  return {
    c() {
      t && t.c();
    },
    m(n, i) {
      t && t.m(n, i), e = !0;
    },
    p(n, [i]) {
      /*tag*/
      n[14] && t.p(n, i);
    },
    i(n) {
      e || (dt(t, n), e = !0);
    },
    o(n) {
      mt(t, n), e = !1;
    },
    d(n) {
      t && t.d(n);
    }
  };
}
function ln(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { height: s = void 0 } = e, { width: o = void 0 } = e, { elem_id: a = "" } = e, { elem_classes: r = [] } = e, { variant: f = "solid" } = e, { border_mode: u = "base" } = e, { padding: c = !0 } = e, { type: p = "normal" } = e, { test_id: m = void 0 } = e, { explicit_call: y = !1 } = e, { container: L = !0 } = e, { visible: v = !0 } = e, { allow_overflow: F = !0 } = e, { scale: d = null } = e, { min_width: _ = 0 } = e, q = p === "fieldset" ? "fieldset" : "div";
  const z = (b) => {
    if (b !== void 0) {
      if (typeof b == "number")
        return b + "px";
      if (typeof b == "string")
        return b;
    }
  };
  return l.$$set = (b) => {
    "height" in b && t(0, s = b.height), "width" in b && t(1, o = b.width), "elem_id" in b && t(2, a = b.elem_id), "elem_classes" in b && t(3, r = b.elem_classes), "variant" in b && t(4, f = b.variant), "border_mode" in b && t(5, u = b.border_mode), "padding" in b && t(6, c = b.padding), "type" in b && t(16, p = b.type), "test_id" in b && t(7, m = b.test_id), "explicit_call" in b && t(8, y = b.explicit_call), "container" in b && t(9, L = b.container), "visible" in b && t(10, v = b.visible), "allow_overflow" in b && t(11, F = b.allow_overflow), "scale" in b && t(12, d = b.scale), "min_width" in b && t(13, _ = b.min_width), "$$scope" in b && t(17, i = b.$$scope);
  }, [
    s,
    o,
    a,
    r,
    f,
    u,
    c,
    m,
    y,
    L,
    v,
    F,
    d,
    _,
    q,
    z,
    p,
    i,
    n
  ];
}
class sn extends Tt {
  constructor(e) {
    super(), Qt(this, e, ln, nn, $t, {
      height: 0,
      width: 1,
      elem_id: 2,
      elem_classes: 3,
      variant: 4,
      border_mode: 5,
      padding: 6,
      type: 16,
      test_id: 7,
      explicit_call: 8,
      container: 9,
      visible: 10,
      allow_overflow: 11,
      scale: 12,
      min_width: 13
    });
  }
}
const {
  SvelteComponent: fn,
  append: Se,
  attr: T,
  bubble: on,
  create_component: rn,
  destroy_component: an,
  detach: ht,
  element: ze,
  init: un,
  insert: bt,
  listen: cn,
  mount_component: _n,
  safe_not_equal: dn,
  set_data: mn,
  set_style: ee,
  space: hn,
  text: bn,
  toggle_class: M,
  transition_in: gn,
  transition_out: wn
} = window.__gradio__svelte__internal;
function We(l) {
  let e, t;
  return {
    c() {
      e = ze("span"), t = bn(
        /*label*/
        l[1]
      ), T(e, "class", "svelte-1lrphxw");
    },
    m(n, i) {
      bt(n, e, i), Se(e, t);
    },
    p(n, i) {
      i & /*label*/
      2 && mn(
        t,
        /*label*/
        n[1]
      );
    },
    d(n) {
      n && ht(e);
    }
  };
}
function kn(l) {
  let e, t, n, i, s, o, a, r = (
    /*show_label*/
    l[2] && We(l)
  );
  return i = new /*Icon*/
  l[0]({}), {
    c() {
      e = ze("button"), r && r.c(), t = hn(), n = ze("div"), rn(i.$$.fragment), T(n, "class", "svelte-1lrphxw"), M(
        n,
        "small",
        /*size*/
        l[4] === "small"
      ), M(
        n,
        "large",
        /*size*/
        l[4] === "large"
      ), M(
        n,
        "medium",
        /*size*/
        l[4] === "medium"
      ), e.disabled = /*disabled*/
      l[7], T(
        e,
        "aria-label",
        /*label*/
        l[1]
      ), T(
        e,
        "aria-haspopup",
        /*hasPopup*/
        l[8]
      ), T(
        e,
        "title",
        /*label*/
        l[1]
      ), T(e, "class", "svelte-1lrphxw"), M(
        e,
        "pending",
        /*pending*/
        l[3]
      ), M(
        e,
        "padded",
        /*padded*/
        l[5]
      ), M(
        e,
        "highlight",
        /*highlight*/
        l[6]
      ), M(
        e,
        "transparent",
        /*transparent*/
        l[9]
      ), ee(e, "color", !/*disabled*/
      l[7] && /*_color*/
      l[12] ? (
        /*_color*/
        l[12]
      ) : "var(--block-label-text-color)"), ee(e, "--bg-color", /*disabled*/
      l[7] ? "auto" : (
        /*background*/
        l[10]
      )), ee(
        e,
        "margin-left",
        /*offset*/
        l[11] + "px"
      );
    },
    m(f, u) {
      bt(f, e, u), r && r.m(e, null), Se(e, t), Se(e, n), _n(i, n, null), s = !0, o || (a = cn(
        e,
        "click",
        /*click_handler*/
        l[14]
      ), o = !0);
    },
    p(f, [u]) {
      /*show_label*/
      f[2] ? r ? r.p(f, u) : (r = We(f), r.c(), r.m(e, t)) : r && (r.d(1), r = null), (!s || u & /*size*/
      16) && M(
        n,
        "small",
        /*size*/
        f[4] === "small"
      ), (!s || u & /*size*/
      16) && M(
        n,
        "large",
        /*size*/
        f[4] === "large"
      ), (!s || u & /*size*/
      16) && M(
        n,
        "medium",
        /*size*/
        f[4] === "medium"
      ), (!s || u & /*disabled*/
      128) && (e.disabled = /*disabled*/
      f[7]), (!s || u & /*label*/
      2) && T(
        e,
        "aria-label",
        /*label*/
        f[1]
      ), (!s || u & /*hasPopup*/
      256) && T(
        e,
        "aria-haspopup",
        /*hasPopup*/
        f[8]
      ), (!s || u & /*label*/
      2) && T(
        e,
        "title",
        /*label*/
        f[1]
      ), (!s || u & /*pending*/
      8) && M(
        e,
        "pending",
        /*pending*/
        f[3]
      ), (!s || u & /*padded*/
      32) && M(
        e,
        "padded",
        /*padded*/
        f[5]
      ), (!s || u & /*highlight*/
      64) && M(
        e,
        "highlight",
        /*highlight*/
        f[6]
      ), (!s || u & /*transparent*/
      512) && M(
        e,
        "transparent",
        /*transparent*/
        f[9]
      ), u & /*disabled, _color*/
      4224 && ee(e, "color", !/*disabled*/
      f[7] && /*_color*/
      f[12] ? (
        /*_color*/
        f[12]
      ) : "var(--block-label-text-color)"), u & /*disabled, background*/
      1152 && ee(e, "--bg-color", /*disabled*/
      f[7] ? "auto" : (
        /*background*/
        f[10]
      )), u & /*offset*/
      2048 && ee(
        e,
        "margin-left",
        /*offset*/
        f[11] + "px"
      );
    },
    i(f) {
      s || (gn(i.$$.fragment, f), s = !0);
    },
    o(f) {
      wn(i.$$.fragment, f), s = !1;
    },
    d(f) {
      f && ht(e), r && r.d(), an(i), o = !1, a();
    }
  };
}
function pn(l, e, t) {
  let n, { Icon: i } = e, { label: s = "" } = e, { show_label: o = !1 } = e, { pending: a = !1 } = e, { size: r = "small" } = e, { padded: f = !0 } = e, { highlight: u = !1 } = e, { disabled: c = !1 } = e, { hasPopup: p = !1 } = e, { color: m = "var(--block-label-text-color)" } = e, { transparent: y = !1 } = e, { background: L = "var(--background-fill-primary)" } = e, { offset: v = 0 } = e;
  function F(d) {
    on.call(this, l, d);
  }
  return l.$$set = (d) => {
    "Icon" in d && t(0, i = d.Icon), "label" in d && t(1, s = d.label), "show_label" in d && t(2, o = d.show_label), "pending" in d && t(3, a = d.pending), "size" in d && t(4, r = d.size), "padded" in d && t(5, f = d.padded), "highlight" in d && t(6, u = d.highlight), "disabled" in d && t(7, c = d.disabled), "hasPopup" in d && t(8, p = d.hasPopup), "color" in d && t(13, m = d.color), "transparent" in d && t(9, y = d.transparent), "background" in d && t(10, L = d.background), "offset" in d && t(11, v = d.offset);
  }, l.$$.update = () => {
    l.$$.dirty & /*highlight, color*/
    8256 && t(12, n = u ? "var(--color-accent)" : m);
  }, [
    i,
    s,
    o,
    a,
    r,
    f,
    u,
    c,
    p,
    y,
    L,
    v,
    n,
    m,
    F
  ];
}
class yn extends fn {
  constructor(e) {
    super(), un(this, e, pn, kn, dn, {
      Icon: 0,
      label: 1,
      show_label: 2,
      pending: 3,
      size: 4,
      padded: 5,
      highlight: 6,
      disabled: 7,
      hasPopup: 8,
      color: 13,
      transparent: 9,
      background: 10,
      offset: 11
    });
  }
}
const {
  SvelteComponent: vn,
  append: Ce,
  attr: I,
  detach: qn,
  init: Cn,
  insert: Fn,
  noop: Fe,
  safe_not_equal: Ln,
  set_style: D,
  svg_element: be
} = window.__gradio__svelte__internal;
function Sn(l) {
  let e, t, n, i;
  return {
    c() {
      e = be("svg"), t = be("g"), n = be("path"), i = be("path"), I(n, "d", "M18,6L6.087,17.913"), D(n, "fill", "none"), D(n, "fill-rule", "nonzero"), D(n, "stroke-width", "2px"), I(t, "transform", "matrix(1.14096,-0.140958,-0.140958,1.14096,-0.0559523,0.0559523)"), I(i, "d", "M4.364,4.364L19.636,19.636"), D(i, "fill", "none"), D(i, "fill-rule", "nonzero"), D(i, "stroke-width", "2px"), I(e, "width", "100%"), I(e, "height", "100%"), I(e, "viewBox", "0 0 24 24"), I(e, "version", "1.1"), I(e, "xmlns", "http://www.w3.org/2000/svg"), I(e, "xmlns:xlink", "http://www.w3.org/1999/xlink"), I(e, "xml:space", "preserve"), I(e, "stroke", "currentColor"), D(e, "fill-rule", "evenodd"), D(e, "clip-rule", "evenodd"), D(e, "stroke-linecap", "round"), D(e, "stroke-linejoin", "round");
    },
    m(s, o) {
      Fn(s, e, o), Ce(e, t), Ce(t, n), Ce(e, i);
    },
    p: Fe,
    i: Fe,
    o: Fe,
    d(s) {
      s && qn(e);
    }
  };
}
class zn extends vn {
  constructor(e) {
    super(), Cn(this, e, null, Sn, Ln, {});
  }
}
const Mn = [
  { color: "red", primary: 600, secondary: 100 },
  { color: "green", primary: 600, secondary: 100 },
  { color: "blue", primary: 600, secondary: 100 },
  { color: "yellow", primary: 500, secondary: 100 },
  { color: "purple", primary: 600, secondary: 100 },
  { color: "teal", primary: 600, secondary: 100 },
  { color: "orange", primary: 600, secondary: 100 },
  { color: "cyan", primary: 600, secondary: 100 },
  { color: "lime", primary: 500, secondary: 100 },
  { color: "pink", primary: 600, secondary: 100 }
], Be = {
  inherit: "inherit",
  current: "currentColor",
  transparent: "transparent",
  black: "#000",
  white: "#fff",
  slate: {
    50: "#f8fafc",
    100: "#f1f5f9",
    200: "#e2e8f0",
    300: "#cbd5e1",
    400: "#94a3b8",
    500: "#64748b",
    600: "#475569",
    700: "#334155",
    800: "#1e293b",
    900: "#0f172a",
    950: "#020617"
  },
  gray: {
    50: "#f9fafb",
    100: "#f3f4f6",
    200: "#e5e7eb",
    300: "#d1d5db",
    400: "#9ca3af",
    500: "#6b7280",
    600: "#4b5563",
    700: "#374151",
    800: "#1f2937",
    900: "#111827",
    950: "#030712"
  },
  zinc: {
    50: "#fafafa",
    100: "#f4f4f5",
    200: "#e4e4e7",
    300: "#d4d4d8",
    400: "#a1a1aa",
    500: "#71717a",
    600: "#52525b",
    700: "#3f3f46",
    800: "#27272a",
    900: "#18181b",
    950: "#09090b"
  },
  neutral: {
    50: "#fafafa",
    100: "#f5f5f5",
    200: "#e5e5e5",
    300: "#d4d4d4",
    400: "#a3a3a3",
    500: "#737373",
    600: "#525252",
    700: "#404040",
    800: "#262626",
    900: "#171717",
    950: "#0a0a0a"
  },
  stone: {
    50: "#fafaf9",
    100: "#f5f5f4",
    200: "#e7e5e4",
    300: "#d6d3d1",
    400: "#a8a29e",
    500: "#78716c",
    600: "#57534e",
    700: "#44403c",
    800: "#292524",
    900: "#1c1917",
    950: "#0c0a09"
  },
  red: {
    50: "#fef2f2",
    100: "#fee2e2",
    200: "#fecaca",
    300: "#fca5a5",
    400: "#f87171",
    500: "#ef4444",
    600: "#dc2626",
    700: "#b91c1c",
    800: "#991b1b",
    900: "#7f1d1d",
    950: "#450a0a"
  },
  orange: {
    50: "#fff7ed",
    100: "#ffedd5",
    200: "#fed7aa",
    300: "#fdba74",
    400: "#fb923c",
    500: "#f97316",
    600: "#ea580c",
    700: "#c2410c",
    800: "#9a3412",
    900: "#7c2d12",
    950: "#431407"
  },
  amber: {
    50: "#fffbeb",
    100: "#fef3c7",
    200: "#fde68a",
    300: "#fcd34d",
    400: "#fbbf24",
    500: "#f59e0b",
    600: "#d97706",
    700: "#b45309",
    800: "#92400e",
    900: "#78350f",
    950: "#451a03"
  },
  yellow: {
    50: "#fefce8",
    100: "#fef9c3",
    200: "#fef08a",
    300: "#fde047",
    400: "#facc15",
    500: "#eab308",
    600: "#ca8a04",
    700: "#a16207",
    800: "#854d0e",
    900: "#713f12",
    950: "#422006"
  },
  lime: {
    50: "#f7fee7",
    100: "#ecfccb",
    200: "#d9f99d",
    300: "#bef264",
    400: "#a3e635",
    500: "#84cc16",
    600: "#65a30d",
    700: "#4d7c0f",
    800: "#3f6212",
    900: "#365314",
    950: "#1a2e05"
  },
  green: {
    50: "#f0fdf4",
    100: "#dcfce7",
    200: "#bbf7d0",
    300: "#86efac",
    400: "#4ade80",
    500: "#22c55e",
    600: "#16a34a",
    700: "#15803d",
    800: "#166534",
    900: "#14532d",
    950: "#052e16"
  },
  emerald: {
    50: "#ecfdf5",
    100: "#d1fae5",
    200: "#a7f3d0",
    300: "#6ee7b7",
    400: "#34d399",
    500: "#10b981",
    600: "#059669",
    700: "#047857",
    800: "#065f46",
    900: "#064e3b",
    950: "#022c22"
  },
  teal: {
    50: "#f0fdfa",
    100: "#ccfbf1",
    200: "#99f6e4",
    300: "#5eead4",
    400: "#2dd4bf",
    500: "#14b8a6",
    600: "#0d9488",
    700: "#0f766e",
    800: "#115e59",
    900: "#134e4a",
    950: "#042f2e"
  },
  cyan: {
    50: "#ecfeff",
    100: "#cffafe",
    200: "#a5f3fc",
    300: "#67e8f9",
    400: "#22d3ee",
    500: "#06b6d4",
    600: "#0891b2",
    700: "#0e7490",
    800: "#155e75",
    900: "#164e63",
    950: "#083344"
  },
  sky: {
    50: "#f0f9ff",
    100: "#e0f2fe",
    200: "#bae6fd",
    300: "#7dd3fc",
    400: "#38bdf8",
    500: "#0ea5e9",
    600: "#0284c7",
    700: "#0369a1",
    800: "#075985",
    900: "#0c4a6e",
    950: "#082f49"
  },
  blue: {
    50: "#eff6ff",
    100: "#dbeafe",
    200: "#bfdbfe",
    300: "#93c5fd",
    400: "#60a5fa",
    500: "#3b82f6",
    600: "#2563eb",
    700: "#1d4ed8",
    800: "#1e40af",
    900: "#1e3a8a",
    950: "#172554"
  },
  indigo: {
    50: "#eef2ff",
    100: "#e0e7ff",
    200: "#c7d2fe",
    300: "#a5b4fc",
    400: "#818cf8",
    500: "#6366f1",
    600: "#4f46e5",
    700: "#4338ca",
    800: "#3730a3",
    900: "#312e81",
    950: "#1e1b4b"
  },
  violet: {
    50: "#f5f3ff",
    100: "#ede9fe",
    200: "#ddd6fe",
    300: "#c4b5fd",
    400: "#a78bfa",
    500: "#8b5cf6",
    600: "#7c3aed",
    700: "#6d28d9",
    800: "#5b21b6",
    900: "#4c1d95",
    950: "#2e1065"
  },
  purple: {
    50: "#faf5ff",
    100: "#f3e8ff",
    200: "#e9d5ff",
    300: "#d8b4fe",
    400: "#c084fc",
    500: "#a855f7",
    600: "#9333ea",
    700: "#7e22ce",
    800: "#6b21a8",
    900: "#581c87",
    950: "#3b0764"
  },
  fuchsia: {
    50: "#fdf4ff",
    100: "#fae8ff",
    200: "#f5d0fe",
    300: "#f0abfc",
    400: "#e879f9",
    500: "#d946ef",
    600: "#c026d3",
    700: "#a21caf",
    800: "#86198f",
    900: "#701a75",
    950: "#4a044e"
  },
  pink: {
    50: "#fdf2f8",
    100: "#fce7f3",
    200: "#fbcfe8",
    300: "#f9a8d4",
    400: "#f472b6",
    500: "#ec4899",
    600: "#db2777",
    700: "#be185d",
    800: "#9d174d",
    900: "#831843",
    950: "#500724"
  },
  rose: {
    50: "#fff1f2",
    100: "#ffe4e6",
    200: "#fecdd3",
    300: "#fda4af",
    400: "#fb7185",
    500: "#f43f5e",
    600: "#e11d48",
    700: "#be123c",
    800: "#9f1239",
    900: "#881337",
    950: "#4c0519"
  }
};
Mn.reduce(
  (l, { color: e, primary: t, secondary: n }) => ({
    ...l,
    [e]: {
      primary: Be[e][t],
      secondary: Be[e][n]
    }
  }),
  {}
);
function le(l) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; l > 1e3 && t < e.length - 1; )
    l /= 1e3, t++;
  let n = e[t];
  return (Number.isInteger(l) ? l : l.toFixed(1)) + n;
}
function ke() {
}
function Vn(l, e) {
  return l != l ? e == e : l !== e || l && typeof l == "object" || typeof l == "function";
}
const gt = typeof window < "u";
let De = gt ? () => window.performance.now() : () => Date.now(), wt = gt ? (l) => requestAnimationFrame(l) : ke;
const ie = /* @__PURE__ */ new Set();
function kt(l) {
  ie.forEach((e) => {
    e.c(l) || (ie.delete(e), e.f());
  }), ie.size !== 0 && wt(kt);
}
function Nn(l) {
  let e;
  return ie.size === 0 && wt(kt), {
    promise: new Promise((t) => {
      ie.add(e = { c: l, f: t });
    }),
    abort() {
      ie.delete(e);
    }
  };
}
const te = [];
function En(l, e = ke) {
  let t;
  const n = /* @__PURE__ */ new Set();
  function i(a) {
    if (Vn(l, a) && (l = a, t)) {
      const r = !te.length;
      for (const f of n)
        f[1](), te.push(f, l);
      if (r) {
        for (let f = 0; f < te.length; f += 2)
          te[f][0](te[f + 1]);
        te.length = 0;
      }
    }
  }
  function s(a) {
    i(a(l));
  }
  function o(a, r = ke) {
    const f = [a, r];
    return n.add(f), n.size === 1 && (t = e(i, s) || ke), a(l), () => {
      n.delete(f), n.size === 0 && t && (t(), t = null);
    };
  }
  return { set: i, update: s, subscribe: o };
}
function He(l) {
  return Object.prototype.toString.call(l) === "[object Date]";
}
function Me(l, e, t, n) {
  if (typeof t == "number" || He(t)) {
    const i = n - t, s = (t - e) / (l.dt || 1 / 60), o = l.opts.stiffness * i, a = l.opts.damping * s, r = (o - a) * l.inv_mass, f = (s + r) * l.dt;
    return Math.abs(f) < l.opts.precision && Math.abs(i) < l.opts.precision ? n : (l.settled = !1, He(t) ? new Date(t.getTime() + f) : t + f);
  } else {
    if (Array.isArray(t))
      return t.map(
        (i, s) => Me(l, e[s], t[s], n[s])
      );
    if (typeof t == "object") {
      const i = {};
      for (const s in t)
        i[s] = Me(l, e[s], t[s], n[s]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function Oe(l, e = {}) {
  const t = En(l), { stiffness: n = 0.15, damping: i = 0.8, precision: s = 0.01 } = e;
  let o, a, r, f = l, u = l, c = 1, p = 0, m = !1;
  function y(v, F = {}) {
    u = v;
    const d = r = {};
    return l == null || F.hard || L.stiffness >= 1 && L.damping >= 1 ? (m = !0, o = De(), f = v, t.set(l = u), Promise.resolve()) : (F.soft && (p = 1 / ((F.soft === !0 ? 0.5 : +F.soft) * 60), c = 0), a || (o = De(), m = !1, a = Nn((_) => {
      if (m)
        return m = !1, a = null, !1;
      c = Math.min(c + p, 1);
      const q = {
        inv_mass: c,
        opts: L,
        settled: !0,
        dt: (_ - o) * 60 / 1e3
      }, z = Me(q, f, l, u);
      return o = _, f = l, t.set(l = z), q.settled && (a = null), !q.settled;
    })), new Promise((_) => {
      a.promise.then(() => {
        d === r && _();
      });
    }));
  }
  const L = {
    set: y,
    update: (v, F) => y(v(u, l), F),
    subscribe: t.subscribe,
    stiffness: n,
    damping: i,
    precision: s
  };
  return L;
}
const {
  SvelteComponent: An,
  append: j,
  attr: C,
  component_subscribe: Te,
  detach: In,
  element: jn,
  init: Zn,
  insert: Pn,
  noop: Ue,
  safe_not_equal: Wn,
  set_style: ge,
  svg_element: Z,
  toggle_class: Je
} = window.__gradio__svelte__internal, { onMount: Bn } = window.__gradio__svelte__internal;
function Dn(l) {
  let e, t, n, i, s, o, a, r, f, u, c, p;
  return {
    c() {
      e = jn("div"), t = Z("svg"), n = Z("g"), i = Z("path"), s = Z("path"), o = Z("path"), a = Z("path"), r = Z("g"), f = Z("path"), u = Z("path"), c = Z("path"), p = Z("path"), C(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), C(i, "fill", "#FF7C00"), C(i, "fill-opacity", "0.4"), C(i, "class", "svelte-43sxxs"), C(s, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), C(s, "fill", "#FF7C00"), C(s, "class", "svelte-43sxxs"), C(o, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), C(o, "fill", "#FF7C00"), C(o, "fill-opacity", "0.4"), C(o, "class", "svelte-43sxxs"), C(a, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), C(a, "fill", "#FF7C00"), C(a, "class", "svelte-43sxxs"), ge(n, "transform", "translate(" + /*$top*/
      l[1][0] + "px, " + /*$top*/
      l[1][1] + "px)"), C(f, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), C(f, "fill", "#FF7C00"), C(f, "fill-opacity", "0.4"), C(f, "class", "svelte-43sxxs"), C(u, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), C(u, "fill", "#FF7C00"), C(u, "class", "svelte-43sxxs"), C(c, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), C(c, "fill", "#FF7C00"), C(c, "fill-opacity", "0.4"), C(c, "class", "svelte-43sxxs"), C(p, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), C(p, "fill", "#FF7C00"), C(p, "class", "svelte-43sxxs"), ge(r, "transform", "translate(" + /*$bottom*/
      l[2][0] + "px, " + /*$bottom*/
      l[2][1] + "px)"), C(t, "viewBox", "-1200 -1200 3000 3000"), C(t, "fill", "none"), C(t, "xmlns", "http://www.w3.org/2000/svg"), C(t, "class", "svelte-43sxxs"), C(e, "class", "svelte-43sxxs"), Je(
        e,
        "margin",
        /*margin*/
        l[0]
      );
    },
    m(m, y) {
      Pn(m, e, y), j(e, t), j(t, n), j(n, i), j(n, s), j(n, o), j(n, a), j(t, r), j(r, f), j(r, u), j(r, c), j(r, p);
    },
    p(m, [y]) {
      y & /*$top*/
      2 && ge(n, "transform", "translate(" + /*$top*/
      m[1][0] + "px, " + /*$top*/
      m[1][1] + "px)"), y & /*$bottom*/
      4 && ge(r, "transform", "translate(" + /*$bottom*/
      m[2][0] + "px, " + /*$bottom*/
      m[2][1] + "px)"), y & /*margin*/
      1 && Je(
        e,
        "margin",
        /*margin*/
        m[0]
      );
    },
    i: Ue,
    o: Ue,
    d(m) {
      m && In(e);
    }
  };
}
function Hn(l, e, t) {
  let n, i;
  var s = this && this.__awaiter || function(m, y, L, v) {
    function F(d) {
      return d instanceof L ? d : new L(function(_) {
        _(d);
      });
    }
    return new (L || (L = Promise))(function(d, _) {
      function q(g) {
        try {
          b(v.next(g));
        } catch (O) {
          _(O);
        }
      }
      function z(g) {
        try {
          b(v.throw(g));
        } catch (O) {
          _(O);
        }
      }
      function b(g) {
        g.done ? d(g.value) : F(g.value).then(q, z);
      }
      b((v = v.apply(m, y || [])).next());
    });
  };
  let { margin: o = !0 } = e;
  const a = Oe([0, 0]);
  Te(l, a, (m) => t(1, n = m));
  const r = Oe([0, 0]);
  Te(l, r, (m) => t(2, i = m));
  let f;
  function u() {
    return s(this, void 0, void 0, function* () {
      yield Promise.all([a.set([125, 140]), r.set([-125, -140])]), yield Promise.all([a.set([-125, 140]), r.set([125, -140])]), yield Promise.all([a.set([-125, 0]), r.set([125, -0])]), yield Promise.all([a.set([125, 0]), r.set([-125, 0])]);
    });
  }
  function c() {
    return s(this, void 0, void 0, function* () {
      yield u(), f || c();
    });
  }
  function p() {
    return s(this, void 0, void 0, function* () {
      yield Promise.all([a.set([125, 0]), r.set([-125, 0])]), c();
    });
  }
  return Bn(() => (p(), () => f = !0)), l.$$set = (m) => {
    "margin" in m && t(0, o = m.margin);
  }, [o, n, i, a, r];
}
class On extends An {
  constructor(e) {
    super(), Zn(this, e, Hn, Dn, Wn, { margin: 0 });
  }
}
const {
  SvelteComponent: Tn,
  append: G,
  attr: P,
  binding_callbacks: Re,
  check_outros: pt,
  create_component: yt,
  create_slot: Un,
  destroy_component: vt,
  destroy_each: qt,
  detach: w,
  element: H,
  empty: se,
  ensure_array_like: pe,
  get_all_dirty_from_scope: Jn,
  get_slot_changes: Rn,
  group_outros: Ct,
  init: Xn,
  insert: k,
  mount_component: Ft,
  noop: Ve,
  safe_not_equal: Yn,
  set_data: A,
  set_style: J,
  space: W,
  text: S,
  toggle_class: E,
  transition_in: K,
  transition_out: Q,
  update_slot_base: Gn
} = window.__gradio__svelte__internal, { tick: Kn } = window.__gradio__svelte__internal, { onDestroy: Qn } = window.__gradio__svelte__internal, { createEventDispatcher: xn } = window.__gradio__svelte__internal, $n = (l) => ({}), Xe = (l) => ({});
function Ye(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n[43] = t, n;
}
function Ge(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n;
}
function el(l) {
  let e, t, n, i, s = (
    /*i18n*/
    l[1]("common.error") + ""
  ), o, a, r;
  t = new yn({
    props: {
      Icon: zn,
      label: (
        /*i18n*/
        l[1]("common.clear")
      ),
      disabled: !1
    }
  }), t.$on(
    "click",
    /*click_handler*/
    l[32]
  );
  const f = (
    /*#slots*/
    l[30].error
  ), u = Un(
    f,
    l,
    /*$$scope*/
    l[29],
    Xe
  );
  return {
    c() {
      e = H("div"), yt(t.$$.fragment), n = W(), i = H("span"), o = S(s), a = W(), u && u.c(), P(e, "class", "clear-status svelte-1yk38uw"), P(i, "class", "error svelte-1yk38uw");
    },
    m(c, p) {
      k(c, e, p), Ft(t, e, null), k(c, n, p), k(c, i, p), G(i, o), k(c, a, p), u && u.m(c, p), r = !0;
    },
    p(c, p) {
      const m = {};
      p[0] & /*i18n*/
      2 && (m.label = /*i18n*/
      c[1]("common.clear")), t.$set(m), (!r || p[0] & /*i18n*/
      2) && s !== (s = /*i18n*/
      c[1]("common.error") + "") && A(o, s), u && u.p && (!r || p[0] & /*$$scope*/
      536870912) && Gn(
        u,
        f,
        c,
        /*$$scope*/
        c[29],
        r ? Rn(
          f,
          /*$$scope*/
          c[29],
          p,
          $n
        ) : Jn(
          /*$$scope*/
          c[29]
        ),
        Xe
      );
    },
    i(c) {
      r || (K(t.$$.fragment, c), K(u, c), r = !0);
    },
    o(c) {
      Q(t.$$.fragment, c), Q(u, c), r = !1;
    },
    d(c) {
      c && (w(e), w(n), w(i), w(a)), vt(t), u && u.d(c);
    }
  };
}
function tl(l) {
  let e, t, n, i, s, o, a, r, f, u = (
    /*variant*/
    l[8] === "default" && /*show_eta_bar*/
    l[18] && /*show_progress*/
    l[6] === "full" && Ke(l)
  );
  function c(_, q) {
    if (
      /*progress*/
      _[7]
    )
      return il;
    if (
      /*queue_position*/
      _[2] !== null && /*queue_size*/
      _[3] !== void 0 && /*queue_position*/
      _[2] >= 0
    )
      return ll;
    if (
      /*queue_position*/
      _[2] === 0
    )
      return nl;
  }
  let p = c(l), m = p && p(l), y = (
    /*timer*/
    l[5] && $e(l)
  );
  const L = [rl, ol], v = [];
  function F(_, q) {
    return (
      /*last_progress_level*/
      _[15] != null ? 0 : (
        /*show_progress*/
        _[6] === "full" ? 1 : -1
      )
    );
  }
  ~(s = F(l)) && (o = v[s] = L[s](l));
  let d = !/*timer*/
  l[5] && ft(l);
  return {
    c() {
      u && u.c(), e = W(), t = H("div"), m && m.c(), n = W(), y && y.c(), i = W(), o && o.c(), a = W(), d && d.c(), r = se(), P(t, "class", "progress-text svelte-1yk38uw"), E(
        t,
        "meta-text-center",
        /*variant*/
        l[8] === "center"
      ), E(
        t,
        "meta-text",
        /*variant*/
        l[8] === "default"
      );
    },
    m(_, q) {
      u && u.m(_, q), k(_, e, q), k(_, t, q), m && m.m(t, null), G(t, n), y && y.m(t, null), k(_, i, q), ~s && v[s].m(_, q), k(_, a, q), d && d.m(_, q), k(_, r, q), f = !0;
    },
    p(_, q) {
      /*variant*/
      _[8] === "default" && /*show_eta_bar*/
      _[18] && /*show_progress*/
      _[6] === "full" ? u ? u.p(_, q) : (u = Ke(_), u.c(), u.m(e.parentNode, e)) : u && (u.d(1), u = null), p === (p = c(_)) && m ? m.p(_, q) : (m && m.d(1), m = p && p(_), m && (m.c(), m.m(t, n))), /*timer*/
      _[5] ? y ? y.p(_, q) : (y = $e(_), y.c(), y.m(t, null)) : y && (y.d(1), y = null), (!f || q[0] & /*variant*/
      256) && E(
        t,
        "meta-text-center",
        /*variant*/
        _[8] === "center"
      ), (!f || q[0] & /*variant*/
      256) && E(
        t,
        "meta-text",
        /*variant*/
        _[8] === "default"
      );
      let z = s;
      s = F(_), s === z ? ~s && v[s].p(_, q) : (o && (Ct(), Q(v[z], 1, 1, () => {
        v[z] = null;
      }), pt()), ~s ? (o = v[s], o ? o.p(_, q) : (o = v[s] = L[s](_), o.c()), K(o, 1), o.m(a.parentNode, a)) : o = null), /*timer*/
      _[5] ? d && (d.d(1), d = null) : d ? d.p(_, q) : (d = ft(_), d.c(), d.m(r.parentNode, r));
    },
    i(_) {
      f || (K(o), f = !0);
    },
    o(_) {
      Q(o), f = !1;
    },
    d(_) {
      _ && (w(e), w(t), w(i), w(a), w(r)), u && u.d(_), m && m.d(), y && y.d(), ~s && v[s].d(_), d && d.d(_);
    }
  };
}
function Ke(l) {
  let e, t = `translateX(${/*eta_level*/
  (l[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = H("div"), P(e, "class", "eta-bar svelte-1yk38uw"), J(e, "transform", t);
    },
    m(n, i) {
      k(n, e, i);
    },
    p(n, i) {
      i[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && J(e, "transform", t);
    },
    d(n) {
      n && w(e);
    }
  };
}
function nl(l) {
  let e;
  return {
    c() {
      e = S("processing |");
    },
    m(t, n) {
      k(t, e, n);
    },
    p: Ve,
    d(t) {
      t && w(e);
    }
  };
}
function ll(l) {
  let e, t = (
    /*queue_position*/
    l[2] + 1 + ""
  ), n, i, s, o;
  return {
    c() {
      e = S("queue: "), n = S(t), i = S("/"), s = S(
        /*queue_size*/
        l[3]
      ), o = S(" |");
    },
    m(a, r) {
      k(a, e, r), k(a, n, r), k(a, i, r), k(a, s, r), k(a, o, r);
    },
    p(a, r) {
      r[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      a[2] + 1 + "") && A(n, t), r[0] & /*queue_size*/
      8 && A(
        s,
        /*queue_size*/
        a[3]
      );
    },
    d(a) {
      a && (w(e), w(n), w(i), w(s), w(o));
    }
  };
}
function il(l) {
  let e, t = pe(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = xe(Ge(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = se();
    },
    m(i, s) {
      for (let o = 0; o < n.length; o += 1)
        n[o] && n[o].m(i, s);
      k(i, e, s);
    },
    p(i, s) {
      if (s[0] & /*progress*/
      128) {
        t = pe(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const a = Ge(i, t, o);
          n[o] ? n[o].p(a, s) : (n[o] = xe(a), n[o].c(), n[o].m(e.parentNode, e));
        }
        for (; o < n.length; o += 1)
          n[o].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && w(e), qt(n, i);
    }
  };
}
function Qe(l) {
  let e, t = (
    /*p*/
    l[41].unit + ""
  ), n, i, s = " ", o;
  function a(u, c) {
    return (
      /*p*/
      u[41].length != null ? fl : sl
    );
  }
  let r = a(l), f = r(l);
  return {
    c() {
      f.c(), e = W(), n = S(t), i = S(" | "), o = S(s);
    },
    m(u, c) {
      f.m(u, c), k(u, e, c), k(u, n, c), k(u, i, c), k(u, o, c);
    },
    p(u, c) {
      r === (r = a(u)) && f ? f.p(u, c) : (f.d(1), f = r(u), f && (f.c(), f.m(e.parentNode, e))), c[0] & /*progress*/
      128 && t !== (t = /*p*/
      u[41].unit + "") && A(n, t);
    },
    d(u) {
      u && (w(e), w(n), w(i), w(o)), f.d(u);
    }
  };
}
function sl(l) {
  let e = le(
    /*p*/
    l[41].index || 0
  ) + "", t;
  return {
    c() {
      t = S(e);
    },
    m(n, i) {
      k(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = le(
        /*p*/
        n[41].index || 0
      ) + "") && A(t, e);
    },
    d(n) {
      n && w(t);
    }
  };
}
function fl(l) {
  let e = le(
    /*p*/
    l[41].index || 0
  ) + "", t, n, i = le(
    /*p*/
    l[41].length
  ) + "", s;
  return {
    c() {
      t = S(e), n = S("/"), s = S(i);
    },
    m(o, a) {
      k(o, t, a), k(o, n, a), k(o, s, a);
    },
    p(o, a) {
      a[0] & /*progress*/
      128 && e !== (e = le(
        /*p*/
        o[41].index || 0
      ) + "") && A(t, e), a[0] & /*progress*/
      128 && i !== (i = le(
        /*p*/
        o[41].length
      ) + "") && A(s, i);
    },
    d(o) {
      o && (w(t), w(n), w(s));
    }
  };
}
function xe(l) {
  let e, t = (
    /*p*/
    l[41].index != null && Qe(l)
  );
  return {
    c() {
      t && t.c(), e = se();
    },
    m(n, i) {
      t && t.m(n, i), k(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[41].index != null ? t ? t.p(n, i) : (t = Qe(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && w(e), t && t.d(n);
    }
  };
}
function $e(l) {
  let e, t = (
    /*eta*/
    l[0] ? `/${/*formatted_eta*/
    l[19]}` : ""
  ), n, i;
  return {
    c() {
      e = S(
        /*formatted_timer*/
        l[20]
      ), n = S(t), i = S("s");
    },
    m(s, o) {
      k(s, e, o), k(s, n, o), k(s, i, o);
    },
    p(s, o) {
      o[0] & /*formatted_timer*/
      1048576 && A(
        e,
        /*formatted_timer*/
        s[20]
      ), o[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      s[0] ? `/${/*formatted_eta*/
      s[19]}` : "") && A(n, t);
    },
    d(s) {
      s && (w(e), w(n), w(i));
    }
  };
}
function ol(l) {
  let e, t;
  return e = new On({
    props: { margin: (
      /*variant*/
      l[8] === "default"
    ) }
  }), {
    c() {
      yt(e.$$.fragment);
    },
    m(n, i) {
      Ft(e, n, i), t = !0;
    },
    p(n, i) {
      const s = {};
      i[0] & /*variant*/
      256 && (s.margin = /*variant*/
      n[8] === "default"), e.$set(s);
    },
    i(n) {
      t || (K(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Q(e.$$.fragment, n), t = !1;
    },
    d(n) {
      vt(e, n);
    }
  };
}
function rl(l) {
  let e, t, n, i, s, o = `${/*last_progress_level*/
  l[15] * 100}%`, a = (
    /*progress*/
    l[7] != null && et(l)
  );
  return {
    c() {
      e = H("div"), t = H("div"), a && a.c(), n = W(), i = H("div"), s = H("div"), P(t, "class", "progress-level-inner svelte-1yk38uw"), P(s, "class", "progress-bar svelte-1yk38uw"), J(s, "width", o), P(i, "class", "progress-bar-wrap svelte-1yk38uw"), P(e, "class", "progress-level svelte-1yk38uw");
    },
    m(r, f) {
      k(r, e, f), G(e, t), a && a.m(t, null), G(e, n), G(e, i), G(i, s), l[31](s);
    },
    p(r, f) {
      /*progress*/
      r[7] != null ? a ? a.p(r, f) : (a = et(r), a.c(), a.m(t, null)) : a && (a.d(1), a = null), f[0] & /*last_progress_level*/
      32768 && o !== (o = `${/*last_progress_level*/
      r[15] * 100}%`) && J(s, "width", o);
    },
    i: Ve,
    o: Ve,
    d(r) {
      r && w(e), a && a.d(), l[31](null);
    }
  };
}
function et(l) {
  let e, t = pe(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = st(Ye(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = se();
    },
    m(i, s) {
      for (let o = 0; o < n.length; o += 1)
        n[o] && n[o].m(i, s);
      k(i, e, s);
    },
    p(i, s) {
      if (s[0] & /*progress_level, progress*/
      16512) {
        t = pe(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const a = Ye(i, t, o);
          n[o] ? n[o].p(a, s) : (n[o] = st(a), n[o].c(), n[o].m(e.parentNode, e));
        }
        for (; o < n.length; o += 1)
          n[o].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && w(e), qt(n, i);
    }
  };
}
function tt(l) {
  let e, t, n, i, s = (
    /*i*/
    l[43] !== 0 && al()
  ), o = (
    /*p*/
    l[41].desc != null && nt(l)
  ), a = (
    /*p*/
    l[41].desc != null && /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[43]
    ] != null && lt()
  ), r = (
    /*progress_level*/
    l[14] != null && it(l)
  );
  return {
    c() {
      s && s.c(), e = W(), o && o.c(), t = W(), a && a.c(), n = W(), r && r.c(), i = se();
    },
    m(f, u) {
      s && s.m(f, u), k(f, e, u), o && o.m(f, u), k(f, t, u), a && a.m(f, u), k(f, n, u), r && r.m(f, u), k(f, i, u);
    },
    p(f, u) {
      /*p*/
      f[41].desc != null ? o ? o.p(f, u) : (o = nt(f), o.c(), o.m(t.parentNode, t)) : o && (o.d(1), o = null), /*p*/
      f[41].desc != null && /*progress_level*/
      f[14] && /*progress_level*/
      f[14][
        /*i*/
        f[43]
      ] != null ? a || (a = lt(), a.c(), a.m(n.parentNode, n)) : a && (a.d(1), a = null), /*progress_level*/
      f[14] != null ? r ? r.p(f, u) : (r = it(f), r.c(), r.m(i.parentNode, i)) : r && (r.d(1), r = null);
    },
    d(f) {
      f && (w(e), w(t), w(n), w(i)), s && s.d(f), o && o.d(f), a && a.d(f), r && r.d(f);
    }
  };
}
function al(l) {
  let e;
  return {
    c() {
      e = S(" /");
    },
    m(t, n) {
      k(t, e, n);
    },
    d(t) {
      t && w(e);
    }
  };
}
function nt(l) {
  let e = (
    /*p*/
    l[41].desc + ""
  ), t;
  return {
    c() {
      t = S(e);
    },
    m(n, i) {
      k(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = /*p*/
      n[41].desc + "") && A(t, e);
    },
    d(n) {
      n && w(t);
    }
  };
}
function lt(l) {
  let e;
  return {
    c() {
      e = S("-");
    },
    m(t, n) {
      k(t, e, n);
    },
    d(t) {
      t && w(e);
    }
  };
}
function it(l) {
  let e = (100 * /*progress_level*/
  (l[14][
    /*i*/
    l[43]
  ] || 0)).toFixed(1) + "", t, n;
  return {
    c() {
      t = S(e), n = S("%");
    },
    m(i, s) {
      k(i, t, s), k(i, n, s);
    },
    p(i, s) {
      s[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[43]
      ] || 0)).toFixed(1) + "") && A(t, e);
    },
    d(i) {
      i && (w(t), w(n));
    }
  };
}
function st(l) {
  let e, t = (
    /*p*/
    (l[41].desc != null || /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[43]
    ] != null) && tt(l)
  );
  return {
    c() {
      t && t.c(), e = se();
    },
    m(n, i) {
      t && t.m(n, i), k(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[41].desc != null || /*progress_level*/
      n[14] && /*progress_level*/
      n[14][
        /*i*/
        n[43]
      ] != null ? t ? t.p(n, i) : (t = tt(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && w(e), t && t.d(n);
    }
  };
}
function ft(l) {
  let e, t;
  return {
    c() {
      e = H("p"), t = S(
        /*loading_text*/
        l[9]
      ), P(e, "class", "loading svelte-1yk38uw");
    },
    m(n, i) {
      k(n, e, i), G(e, t);
    },
    p(n, i) {
      i[0] & /*loading_text*/
      512 && A(
        t,
        /*loading_text*/
        n[9]
      );
    },
    d(n) {
      n && w(e);
    }
  };
}
function ul(l) {
  let e, t, n, i, s;
  const o = [tl, el], a = [];
  function r(f, u) {
    return (
      /*status*/
      f[4] === "pending" ? 0 : (
        /*status*/
        f[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = r(l)) && (n = a[t] = o[t](l)), {
    c() {
      e = H("div"), n && n.c(), P(e, "class", i = "wrap " + /*variant*/
      l[8] + " " + /*show_progress*/
      l[6] + " svelte-1yk38uw"), E(e, "hide", !/*status*/
      l[4] || /*status*/
      l[4] === "complete" || /*show_progress*/
      l[6] === "hidden"), E(
        e,
        "translucent",
        /*variant*/
        l[8] === "center" && /*status*/
        (l[4] === "pending" || /*status*/
        l[4] === "error") || /*translucent*/
        l[11] || /*show_progress*/
        l[6] === "minimal"
      ), E(
        e,
        "generating",
        /*status*/
        l[4] === "generating"
      ), E(
        e,
        "border",
        /*border*/
        l[12]
      ), J(
        e,
        "position",
        /*absolute*/
        l[10] ? "absolute" : "static"
      ), J(
        e,
        "padding",
        /*absolute*/
        l[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(f, u) {
      k(f, e, u), ~t && a[t].m(e, null), l[33](e), s = !0;
    },
    p(f, u) {
      let c = t;
      t = r(f), t === c ? ~t && a[t].p(f, u) : (n && (Ct(), Q(a[c], 1, 1, () => {
        a[c] = null;
      }), pt()), ~t ? (n = a[t], n ? n.p(f, u) : (n = a[t] = o[t](f), n.c()), K(n, 1), n.m(e, null)) : n = null), (!s || u[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      f[8] + " " + /*show_progress*/
      f[6] + " svelte-1yk38uw")) && P(e, "class", i), (!s || u[0] & /*variant, show_progress, status, show_progress*/
      336) && E(e, "hide", !/*status*/
      f[4] || /*status*/
      f[4] === "complete" || /*show_progress*/
      f[6] === "hidden"), (!s || u[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && E(
        e,
        "translucent",
        /*variant*/
        f[8] === "center" && /*status*/
        (f[4] === "pending" || /*status*/
        f[4] === "error") || /*translucent*/
        f[11] || /*show_progress*/
        f[6] === "minimal"
      ), (!s || u[0] & /*variant, show_progress, status*/
      336) && E(
        e,
        "generating",
        /*status*/
        f[4] === "generating"
      ), (!s || u[0] & /*variant, show_progress, border*/
      4416) && E(
        e,
        "border",
        /*border*/
        f[12]
      ), u[0] & /*absolute*/
      1024 && J(
        e,
        "position",
        /*absolute*/
        f[10] ? "absolute" : "static"
      ), u[0] & /*absolute*/
      1024 && J(
        e,
        "padding",
        /*absolute*/
        f[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(f) {
      s || (K(n), s = !0);
    },
    o(f) {
      Q(n), s = !1;
    },
    d(f) {
      f && w(e), ~t && a[t].d(), l[33](null);
    }
  };
}
var cl = function(l, e, t, n) {
  function i(s) {
    return s instanceof t ? s : new t(function(o) {
      o(s);
    });
  }
  return new (t || (t = Promise))(function(s, o) {
    function a(u) {
      try {
        f(n.next(u));
      } catch (c) {
        o(c);
      }
    }
    function r(u) {
      try {
        f(n.throw(u));
      } catch (c) {
        o(c);
      }
    }
    function f(u) {
      u.done ? s(u.value) : i(u.value).then(a, r);
    }
    f((n = n.apply(l, e || [])).next());
  });
};
let we = [], Le = !1;
function _l(l) {
  return cl(this, arguments, void 0, function* (e, t = !0) {
    if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
      if (we.push(e), !Le)
        Le = !0;
      else
        return;
      yield Kn(), requestAnimationFrame(() => {
        let n = [0, 0];
        for (let i = 0; i < we.length; i++) {
          const o = we[i].getBoundingClientRect();
          (i === 0 || o.top + window.scrollY <= n[0]) && (n[0] = o.top + window.scrollY, n[1] = i);
        }
        window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), Le = !1, we = [];
      });
    }
  });
}
function dl(l, e, t) {
  let n, { $$slots: i = {}, $$scope: s } = e;
  this && this.__awaiter;
  const o = xn();
  let { i18n: a } = e, { eta: r = null } = e, { queue_position: f } = e, { queue_size: u } = e, { status: c } = e, { scroll_to_output: p = !1 } = e, { timer: m = !0 } = e, { show_progress: y = "full" } = e, { message: L = null } = e, { progress: v = null } = e, { variant: F = "default" } = e, { loading_text: d = "Loading..." } = e, { absolute: _ = !0 } = e, { translucent: q = !1 } = e, { border: z = !1 } = e, { autoscroll: b } = e, g, O = !1, ue = 0, R = 0, x = null, $ = null, Ae = 0, X = null, fe, U = null, Ie = !0;
  const Nt = () => {
    t(0, r = t(27, x = t(19, ce = null))), t(25, ue = performance.now()), t(26, R = 0), O = !0, je();
  };
  function je() {
    requestAnimationFrame(() => {
      t(26, R = (performance.now() - ue) / 1e3), O && je();
    });
  }
  function Ze() {
    t(26, R = 0), t(0, r = t(27, x = t(19, ce = null))), O && (O = !1);
  }
  Qn(() => {
    O && Ze();
  });
  let ce = null;
  function Et(h) {
    Re[h ? "unshift" : "push"](() => {
      U = h, t(16, U), t(7, v), t(14, X), t(15, fe);
    });
  }
  const At = () => {
    o("clear_status");
  };
  function It(h) {
    Re[h ? "unshift" : "push"](() => {
      g = h, t(13, g);
    });
  }
  return l.$$set = (h) => {
    "i18n" in h && t(1, a = h.i18n), "eta" in h && t(0, r = h.eta), "queue_position" in h && t(2, f = h.queue_position), "queue_size" in h && t(3, u = h.queue_size), "status" in h && t(4, c = h.status), "scroll_to_output" in h && t(22, p = h.scroll_to_output), "timer" in h && t(5, m = h.timer), "show_progress" in h && t(6, y = h.show_progress), "message" in h && t(23, L = h.message), "progress" in h && t(7, v = h.progress), "variant" in h && t(8, F = h.variant), "loading_text" in h && t(9, d = h.loading_text), "absolute" in h && t(10, _ = h.absolute), "translucent" in h && t(11, q = h.translucent), "border" in h && t(12, z = h.border), "autoscroll" in h && t(24, b = h.autoscroll), "$$scope" in h && t(29, s = h.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    436207617 && (r === null && t(0, r = x), r != null && x !== r && (t(28, $ = (performance.now() - ue) / 1e3 + r), t(19, ce = $.toFixed(1)), t(27, x = r))), l.$$.dirty[0] & /*eta_from_start, timer_diff*/
    335544320 && t(17, Ae = $ === null || $ <= 0 || !R ? null : Math.min(R / $, 1)), l.$$.dirty[0] & /*progress*/
    128 && v != null && t(18, Ie = !1), l.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (v != null ? t(14, X = v.map((h) => {
      if (h.index != null && h.length != null)
        return h.index / h.length;
      if (h.progress != null)
        return h.progress;
    })) : t(14, X = null), X ? (t(15, fe = X[X.length - 1]), U && (fe === 0 ? t(16, U.style.transition = "0", U) : t(16, U.style.transition = "150ms", U))) : t(15, fe = void 0)), l.$$.dirty[0] & /*status*/
    16 && (c === "pending" ? Nt() : Ze()), l.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && g && p && (c === "pending" || c === "complete") && _l(g, b), l.$$.dirty[0] & /*status, message*/
    8388624, l.$$.dirty[0] & /*timer_diff*/
    67108864 && t(20, n = R.toFixed(1));
  }, [
    r,
    a,
    f,
    u,
    c,
    m,
    y,
    v,
    F,
    d,
    _,
    q,
    z,
    g,
    X,
    fe,
    U,
    Ae,
    Ie,
    ce,
    n,
    o,
    p,
    L,
    b,
    ue,
    R,
    x,
    $,
    s,
    i,
    Et,
    At,
    It
  ];
}
class ml extends Tn {
  constructor(e) {
    super(), Xn(
      this,
      e,
      dl,
      ul,
      Yn,
      {
        i18n: 1,
        eta: 0,
        queue_position: 2,
        queue_size: 3,
        status: 4,
        scroll_to_output: 22,
        timer: 5,
        show_progress: 6,
        message: 23,
        progress: 7,
        variant: 8,
        loading_text: 9,
        absolute: 10,
        translucent: 11,
        border: 12,
        autoscroll: 24
      },
      null,
      [-1, -1]
    );
  }
}
const {
  SvelteComponent: hl,
  append: bl,
  attr: re,
  detach: Lt,
  element: ot,
  empty: gl,
  init: wl,
  insert: St,
  noop: rt,
  safe_not_equal: kl,
  src_url_equal: at,
  toggle_class: ne
} = window.__gradio__svelte__internal;
function ut(l) {
  let e, t, n;
  return {
    c() {
      e = ot("div"), t = ot("img"), at(t.src, n = /*value*/
      l[0].url) || re(t, "src", n), re(t, "alt", ""), re(t, "class", "svelte-giydt1"), re(e, "class", "container svelte-giydt1"), ne(
        e,
        "table",
        /*type*/
        l[1] === "table"
      ), ne(
        e,
        "gallery",
        /*type*/
        l[1] === "gallery"
      ), ne(
        e,
        "selected",
        /*selected*/
        l[2]
      );
    },
    m(i, s) {
      St(i, e, s), bl(e, t);
    },
    p(i, s) {
      s & /*value*/
      1 && !at(t.src, n = /*value*/
      i[0].url) && re(t, "src", n), s & /*type*/
      2 && ne(
        e,
        "table",
        /*type*/
        i[1] === "table"
      ), s & /*type*/
      2 && ne(
        e,
        "gallery",
        /*type*/
        i[1] === "gallery"
      ), s & /*selected*/
      4 && ne(
        e,
        "selected",
        /*selected*/
        i[2]
      );
    },
    d(i) {
      i && Lt(e);
    }
  };
}
function pl(l) {
  let e, t = (
    /*value*/
    l[0] && ut(l)
  );
  return {
    c() {
      t && t.c(), e = gl();
    },
    m(n, i) {
      t && t.m(n, i), St(n, e, i);
    },
    p(n, [i]) {
      /*value*/
      n[0] ? t ? t.p(n, i) : (t = ut(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    i: rt,
    o: rt,
    d(n) {
      n && Lt(e), t && t.d(n);
    }
  };
}
function yl(l, e, t) {
  let { value: n } = e, { type: i } = e, { selected: s = !1 } = e;
  return l.$$set = (o) => {
    "value" in o && t(0, n = o.value), "type" in o && t(1, i = o.type), "selected" in o && t(2, s = o.selected);
  }, [n, i, s];
}
class Bl extends hl {
  constructor(e) {
    super(), wl(this, e, yl, pl, kl, { value: 0, type: 1, selected: 2 });
  }
}
const {
  SvelteComponent: vl,
  assign: ql,
  attr: Cl,
  binding_callbacks: Fl,
  check_outros: Ll,
  create_component: zt,
  destroy_component: Mt,
  detach: Ne,
  element: Sl,
  empty: zl,
  flush: N,
  get_spread_object: Ml,
  get_spread_update: Vl,
  group_outros: Nl,
  init: El,
  insert: Ee,
  mount_component: Vt,
  safe_not_equal: Al,
  set_style: ct,
  space: Il,
  transition_in: ae,
  transition_out: ye
} = window.__gradio__svelte__internal, { onMount: jl } = window.__gradio__svelte__internal;
function _t(l) {
  let e, t;
  return e = new sn({
    props: {
      visible: (
        /*visible*/
        l[3]
      ),
      variant: "solid",
      border_mode: (
        /*dragging*/
        l[12] ? "focus" : "base"
      ),
      padding: !1,
      elem_id: (
        /*elem_id*/
        l[1]
      ),
      elem_classes: (
        /*elem_classes*/
        l[2]
      ),
      allow_overflow: !1,
      container: (
        /*container*/
        l[4]
      ),
      scale: (
        /*scale*/
        l[5]
      ),
      min_width: (
        /*min_width*/
        l[6]
      ),
      $$slots: { default: [Zl] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      zt(e.$$.fragment);
    },
    m(n, i) {
      Vt(e, n, i), t = !0;
    },
    p(n, i) {
      const s = {};
      i & /*visible*/
      8 && (s.visible = /*visible*/
      n[3]), i & /*elem_id*/
      2 && (s.elem_id = /*elem_id*/
      n[1]), i & /*elem_classes*/
      4 && (s.elem_classes = /*elem_classes*/
      n[2]), i & /*container*/
      16 && (s.container = /*container*/
      n[4]), i & /*scale*/
      32 && (s.scale = /*scale*/
      n[5]), i & /*min_width*/
      64 && (s.min_width = /*min_width*/
      n[6]), i & /*$$scope, ref, height, gradio, patched_loading_status, loading_status*/
      1052289 && (s.$$scope = { dirty: i, ctx: n }), e.$set(s);
    },
    i(n) {
      t || (ae(e.$$.fragment, n), t = !0);
    },
    o(n) {
      ye(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Mt(e, n);
    }
  };
}
function Zl(l) {
  let e, t, n, i;
  const s = [
    { autoscroll: (
      /*gradio*/
      l[9].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      l[9].i18n
    ) },
    /*patched_loading_status*/
    l[10]
  ];
  let o = {};
  for (let a = 0; a < s.length; a += 1)
    o = ql(o, s[a]);
  return e = new ml({ props: o }), e.$on(
    "clear_status",
    /*clear_status_handler*/
    l[15]
  ), {
    c() {
      zt(e.$$.fragment), t = Il(), n = Sl("div"), Cl(n, "class", "viewer svelte-mo2zro"), ct(
        n,
        "height",
        /*height*/
        l[0]
      );
    },
    m(a, r) {
      Vt(e, a, r), Ee(a, t, r), Ee(a, n, r), l[16](n), i = !0;
    },
    p(a, r) {
      const f = r & /*gradio, patched_loading_status*/
      1536 ? Vl(s, [
        r & /*gradio*/
        512 && { autoscroll: (
          /*gradio*/
          a[9].autoscroll
        ) },
        r & /*gradio*/
        512 && { i18n: (
          /*gradio*/
          a[9].i18n
        ) },
        r & /*patched_loading_status*/
        1024 && Ml(
          /*patched_loading_status*/
          a[10]
        )
      ]) : {};
      e.$set(f), r & /*height*/
      1 && ct(
        n,
        "height",
        /*height*/
        a[0]
      );
    },
    i(a) {
      i || (ae(e.$$.fragment, a), i = !0);
    },
    o(a) {
      ye(e.$$.fragment, a), i = !1;
    },
    d(a) {
      a && (Ne(t), Ne(n)), Mt(e, a), l[16](null);
    }
  };
}
function Pl(l) {
  let e, t, n = !/*interactive*/
  l[8] && _t(l);
  return {
    c() {
      n && n.c(), e = zl();
    },
    m(i, s) {
      n && n.m(i, s), Ee(i, e, s), t = !0;
    },
    p(i, [s]) {
      /*interactive*/
      i[8] ? n && (Nl(), ye(n, 1, 1, () => {
        n = null;
      }), Ll()) : n ? (n.p(i, s), s & /*interactive*/
      256 && ae(n, 1)) : (n = _t(i), n.c(), ae(n, 1), n.m(e.parentNode, e));
    },
    i(i) {
      t || (ae(n), t = !0);
    },
    o(i) {
      ye(n), t = !1;
    },
    d(i) {
      i && Ne(e), n && n.d(i);
    }
  };
}
function Wl(l, e, t) {
  let { elem_id: n = "" } = e, { elem_classes: i = [] } = e, { visible: s = !0 } = e, { height: o = 640 } = e, { value: a = null } = e, { container: r = !0 } = e, { scale: f = null } = e, { min_width: u = void 0 } = e, { loading_status: c } = e, { interactive: p } = e, { streaming: m } = e, y = null, { gradio: L } = e, v, F, d, _;
  function q() {
    if (JSON.stringify(a) !== JSON.stringify(y) && F != null && F.ready)
      if (y = a, !Array.isArray(a))
        a.is_stream ? F.open(a.url, { follow_if_http: !0 }) : F.open(a.url);
      else
        for (const g of a)
          typeof g != "string" ? g.url && F.open(g.url) : F.open(g);
  }
  jl(() => (F = new Ht(), F.start(void 0, d, !0).then(() => {
    q();
  }), () => {
    F.stop();
  }));
  const z = () => L.dispatch("clear_status", c);
  function b(g) {
    Fl[g ? "unshift" : "push"](() => {
      d = g, t(11, d);
    });
  }
  return l.$$set = (g) => {
    "elem_id" in g && t(1, n = g.elem_id), "elem_classes" in g && t(2, i = g.elem_classes), "visible" in g && t(3, s = g.visible), "height" in g && t(0, o = g.height), "value" in g && t(13, a = g.value), "container" in g && t(4, r = g.container), "scale" in g && t(5, f = g.scale), "min_width" in g && t(6, u = g.min_width), "loading_status" in g && t(7, c = g.loading_status), "interactive" in g && t(8, p = g.interactive), "streaming" in g && t(14, m = g.streaming), "gradio" in g && t(9, L = g.gradio);
  }, l.$$.update = () => {
    l.$$.dirty & /*height*/
    1 && t(0, o = typeof o == "number" ? `${o}px` : o), l.$$.dirty & /*loading_status, streaming, patched_loading_status*/
    17536 && (t(10, _ = c), m && _?.status === "generating" && t(10, _.status = "complete", _)), l.$$.dirty & /*value*/
    8192 && q();
  }, [
    o,
    n,
    i,
    s,
    r,
    f,
    u,
    c,
    p,
    L,
    _,
    d,
    v,
    a,
    m,
    z,
    b
  ];
}
class Dl extends vl {
  constructor(e) {
    super(), El(this, e, Wl, Pl, Al, {
      elem_id: 1,
      elem_classes: 2,
      visible: 3,
      height: 0,
      value: 13,
      container: 4,
      scale: 5,
      min_width: 6,
      loading_status: 7,
      interactive: 8,
      streaming: 14,
      gradio: 9
    });
  }
  get elem_id() {
    return this.$$.ctx[1];
  }
  set elem_id(e) {
    this.$$set({ elem_id: e }), N();
  }
  get elem_classes() {
    return this.$$.ctx[2];
  }
  set elem_classes(e) {
    this.$$set({ elem_classes: e }), N();
  }
  get visible() {
    return this.$$.ctx[3];
  }
  set visible(e) {
    this.$$set({ visible: e }), N();
  }
  get height() {
    return this.$$.ctx[0];
  }
  set height(e) {
    this.$$set({ height: e }), N();
  }
  get value() {
    return this.$$.ctx[13];
  }
  set value(e) {
    this.$$set({ value: e }), N();
  }
  get container() {
    return this.$$.ctx[4];
  }
  set container(e) {
    this.$$set({ container: e }), N();
  }
  get scale() {
    return this.$$.ctx[5];
  }
  set scale(e) {
    this.$$set({ scale: e }), N();
  }
  get min_width() {
    return this.$$.ctx[6];
  }
  set min_width(e) {
    this.$$set({ min_width: e }), N();
  }
  get loading_status() {
    return this.$$.ctx[7];
  }
  set loading_status(e) {
    this.$$set({ loading_status: e }), N();
  }
  get interactive() {
    return this.$$.ctx[8];
  }
  set interactive(e) {
    this.$$set({ interactive: e }), N();
  }
  get streaming() {
    return this.$$.ctx[14];
  }
  set streaming(e) {
    this.$$set({ streaming: e }), N();
  }
  get gradio() {
    return this.$$.ctx[9];
  }
  set gradio(e) {
    this.$$set({ gradio: e }), N();
  }
}
export {
  Bl as BaseExample,
  Dl as default
};
