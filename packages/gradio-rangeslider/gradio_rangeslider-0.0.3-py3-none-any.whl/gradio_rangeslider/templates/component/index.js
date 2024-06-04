const {
  SvelteComponent: Ot,
  assign: Jt,
  create_slot: Xt,
  detach: Yt,
  element: Gt,
  get_all_dirty_from_scope: Rt,
  get_slot_changes: Ht,
  get_spread_update: Kt,
  init: Qt,
  insert: Ut,
  safe_not_equal: Wt,
  set_dynamic_element_data: Qe,
  set_style: E,
  toggle_class: W,
  transition_in: vt,
  transition_out: yt,
  update_slot_base: xt
} = window.__gradio__svelte__internal;
function $t(l) {
  let e, t, n;
  const i = (
    /*#slots*/
    l[18].default
  ), s = Xt(
    i,
    l,
    /*$$scope*/
    l[17],
    null
  );
  let a = [
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
  ], r = {};
  for (let f = 0; f < a.length; f += 1)
    r = Jt(r, a[f]);
  return {
    c() {
      e = Gt(
        /*tag*/
        l[14]
      ), s && s.c(), Qe(
        /*tag*/
        l[14]
      )(e, r), W(
        e,
        "hidden",
        /*visible*/
        l[10] === !1
      ), W(
        e,
        "padded",
        /*padding*/
        l[6]
      ), W(
        e,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), W(
        e,
        "border_contrast",
        /*border_mode*/
        l[5] === "contrast"
      ), W(e, "hide-container", !/*explicit_call*/
      l[8] && !/*container*/
      l[9]), E(
        e,
        "height",
        /*get_dimension*/
        l[15](
          /*height*/
          l[0]
        )
      ), E(e, "width", typeof /*width*/
      l[1] == "number" ? `calc(min(${/*width*/
      l[1]}px, 100%))` : (
        /*get_dimension*/
        l[15](
          /*width*/
          l[1]
        )
      )), E(
        e,
        "border-style",
        /*variant*/
        l[4]
      ), E(
        e,
        "overflow",
        /*allow_overflow*/
        l[11] ? "visible" : "hidden"
      ), E(
        e,
        "flex-grow",
        /*scale*/
        l[12]
      ), E(e, "min-width", `calc(min(${/*min_width*/
      l[13]}px, 100%))`), E(e, "border-width", "var(--block-border-width)");
    },
    m(f, o) {
      Ut(f, e, o), s && s.m(e, null), n = !0;
    },
    p(f, o) {
      s && s.p && (!n || o & /*$$scope*/
      131072) && xt(
        s,
        i,
        f,
        /*$$scope*/
        f[17],
        n ? Ht(
          i,
          /*$$scope*/
          f[17],
          o,
          null
        ) : Rt(
          /*$$scope*/
          f[17]
        ),
        null
      ), Qe(
        /*tag*/
        f[14]
      )(e, r = Kt(a, [
        (!n || o & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          f[7]
        ) },
        (!n || o & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          f[2]
        ) },
        (!n || o & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        f[3].join(" ") + " svelte-nl1om8")) && { class: t }
      ])), W(
        e,
        "hidden",
        /*visible*/
        f[10] === !1
      ), W(
        e,
        "padded",
        /*padding*/
        f[6]
      ), W(
        e,
        "border_focus",
        /*border_mode*/
        f[5] === "focus"
      ), W(
        e,
        "border_contrast",
        /*border_mode*/
        f[5] === "contrast"
      ), W(e, "hide-container", !/*explicit_call*/
      f[8] && !/*container*/
      f[9]), o & /*height*/
      1 && E(
        e,
        "height",
        /*get_dimension*/
        f[15](
          /*height*/
          f[0]
        )
      ), o & /*width*/
      2 && E(e, "width", typeof /*width*/
      f[1] == "number" ? `calc(min(${/*width*/
      f[1]}px, 100%))` : (
        /*get_dimension*/
        f[15](
          /*width*/
          f[1]
        )
      )), o & /*variant*/
      16 && E(
        e,
        "border-style",
        /*variant*/
        f[4]
      ), o & /*allow_overflow*/
      2048 && E(
        e,
        "overflow",
        /*allow_overflow*/
        f[11] ? "visible" : "hidden"
      ), o & /*scale*/
      4096 && E(
        e,
        "flex-grow",
        /*scale*/
        f[12]
      ), o & /*min_width*/
      8192 && E(e, "min-width", `calc(min(${/*min_width*/
      f[13]}px, 100%))`);
    },
    i(f) {
      n || (vt(s, f), n = !0);
    },
    o(f) {
      yt(s, f), n = !1;
    },
    d(f) {
      f && Yt(e), s && s.d(f);
    }
  };
}
function el(l) {
  let e, t = (
    /*tag*/
    l[14] && $t(l)
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
      e || (vt(t, n), e = !0);
    },
    o(n) {
      yt(t, n), e = !1;
    },
    d(n) {
      t && t.d(n);
    }
  };
}
function tl(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { height: s = void 0 } = e, { width: a = void 0 } = e, { elem_id: r = "" } = e, { elem_classes: f = [] } = e, { variant: o = "solid" } = e, { border_mode: u = "base" } = e, { padding: _ = !0 } = e, { type: m = "normal" } = e, { test_id: b = void 0 } = e, { explicit_call: y = !1 } = e, { container: V = !0 } = e, { visible: k = !0 } = e, { allow_overflow: I = !0 } = e, { scale: c = null } = e, { min_width: d = 0 } = e, S = m === "fieldset" ? "fieldset" : "div";
  const z = (h) => {
    if (h !== void 0) {
      if (typeof h == "number")
        return h + "px";
      if (typeof h == "string")
        return h;
    }
  };
  return l.$$set = (h) => {
    "height" in h && t(0, s = h.height), "width" in h && t(1, a = h.width), "elem_id" in h && t(2, r = h.elem_id), "elem_classes" in h && t(3, f = h.elem_classes), "variant" in h && t(4, o = h.variant), "border_mode" in h && t(5, u = h.border_mode), "padding" in h && t(6, _ = h.padding), "type" in h && t(16, m = h.type), "test_id" in h && t(7, b = h.test_id), "explicit_call" in h && t(8, y = h.explicit_call), "container" in h && t(9, V = h.container), "visible" in h && t(10, k = h.visible), "allow_overflow" in h && t(11, I = h.allow_overflow), "scale" in h && t(12, c = h.scale), "min_width" in h && t(13, d = h.min_width), "$$scope" in h && t(17, i = h.$$scope);
  }, [
    s,
    a,
    r,
    f,
    o,
    u,
    _,
    b,
    y,
    V,
    k,
    I,
    c,
    d,
    S,
    z,
    m,
    i,
    n
  ];
}
class ll extends Ot {
  constructor(e) {
    super(), Qt(this, e, tl, el, Wt, {
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
  SvelteComponent: nl,
  attr: il,
  create_slot: fl,
  detach: sl,
  element: ol,
  get_all_dirty_from_scope: al,
  get_slot_changes: rl,
  init: ul,
  insert: _l,
  safe_not_equal: dl,
  transition_in: cl,
  transition_out: ml,
  update_slot_base: bl
} = window.__gradio__svelte__internal;
function gl(l) {
  let e, t;
  const n = (
    /*#slots*/
    l[1].default
  ), i = fl(
    n,
    l,
    /*$$scope*/
    l[0],
    null
  );
  return {
    c() {
      e = ol("div"), i && i.c(), il(e, "class", "svelte-1hnfib2");
    },
    m(s, a) {
      _l(s, e, a), i && i.m(e, null), t = !0;
    },
    p(s, [a]) {
      i && i.p && (!t || a & /*$$scope*/
      1) && bl(
        i,
        n,
        s,
        /*$$scope*/
        s[0],
        t ? rl(
          n,
          /*$$scope*/
          s[0],
          a,
          null
        ) : al(
          /*$$scope*/
          s[0]
        ),
        null
      );
    },
    i(s) {
      t || (cl(i, s), t = !0);
    },
    o(s) {
      ml(i, s), t = !1;
    },
    d(s) {
      s && sl(e), i && i.d(s);
    }
  };
}
function hl(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e;
  return l.$$set = (s) => {
    "$$scope" in s && t(0, i = s.$$scope);
  }, [i, n];
}
class wl extends nl {
  constructor(e) {
    super(), ul(this, e, hl, gl, dl, {});
  }
}
const {
  SvelteComponent: pl,
  attr: Ue,
  check_outros: kl,
  create_component: vl,
  create_slot: yl,
  destroy_component: ql,
  detach: ze,
  element: Cl,
  empty: Fl,
  get_all_dirty_from_scope: Ll,
  get_slot_changes: Sl,
  group_outros: zl,
  init: Ml,
  insert: Me,
  mount_component: Vl,
  safe_not_equal: Nl,
  set_data: Il,
  space: Zl,
  text: jl,
  toggle_class: ue,
  transition_in: we,
  transition_out: Ve,
  update_slot_base: Pl
} = window.__gradio__svelte__internal;
function We(l) {
  let e, t;
  return e = new wl({
    props: {
      $$slots: { default: [Bl] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      vl(e.$$.fragment);
    },
    m(n, i) {
      Vl(e, n, i), t = !0;
    },
    p(n, i) {
      const s = {};
      i & /*$$scope, info*/
      10 && (s.$$scope = { dirty: i, ctx: n }), e.$set(s);
    },
    i(n) {
      t || (we(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Ve(e.$$.fragment, n), t = !1;
    },
    d(n) {
      ql(e, n);
    }
  };
}
function Bl(l) {
  let e;
  return {
    c() {
      e = jl(
        /*info*/
        l[1]
      );
    },
    m(t, n) {
      Me(t, e, n);
    },
    p(t, n) {
      n & /*info*/
      2 && Il(
        e,
        /*info*/
        t[1]
      );
    },
    d(t) {
      t && ze(e);
    }
  };
}
function Al(l) {
  let e, t, n, i;
  const s = (
    /*#slots*/
    l[2].default
  ), a = yl(
    s,
    l,
    /*$$scope*/
    l[3],
    null
  );
  let r = (
    /*info*/
    l[1] && We(l)
  );
  return {
    c() {
      e = Cl("span"), a && a.c(), t = Zl(), r && r.c(), n = Fl(), Ue(e, "data-testid", "block-info"), Ue(e, "class", "svelte-22c38v"), ue(e, "sr-only", !/*show_label*/
      l[0]), ue(e, "hide", !/*show_label*/
      l[0]), ue(
        e,
        "has-info",
        /*info*/
        l[1] != null
      );
    },
    m(f, o) {
      Me(f, e, o), a && a.m(e, null), Me(f, t, o), r && r.m(f, o), Me(f, n, o), i = !0;
    },
    p(f, [o]) {
      a && a.p && (!i || o & /*$$scope*/
      8) && Pl(
        a,
        s,
        f,
        /*$$scope*/
        f[3],
        i ? Sl(
          s,
          /*$$scope*/
          f[3],
          o,
          null
        ) : Ll(
          /*$$scope*/
          f[3]
        ),
        null
      ), (!i || o & /*show_label*/
      1) && ue(e, "sr-only", !/*show_label*/
      f[0]), (!i || o & /*show_label*/
      1) && ue(e, "hide", !/*show_label*/
      f[0]), (!i || o & /*info*/
      2) && ue(
        e,
        "has-info",
        /*info*/
        f[1] != null
      ), /*info*/
      f[1] ? r ? (r.p(f, o), o & /*info*/
      2 && we(r, 1)) : (r = We(f), r.c(), we(r, 1), r.m(n.parentNode, n)) : r && (zl(), Ve(r, 1, 1, () => {
        r = null;
      }), kl());
    },
    i(f) {
      i || (we(a, f), we(r), i = !0);
    },
    o(f) {
      Ve(a, f), Ve(r), i = !1;
    },
    d(f) {
      f && (ze(e), ze(t), ze(n)), a && a.d(f), r && r.d(f);
    }
  };
}
function Dl(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { show_label: s = !0 } = e, { info: a = void 0 } = e;
  return l.$$set = (r) => {
    "show_label" in r && t(0, s = r.show_label), "info" in r && t(1, a = r.info), "$$scope" in r && t(3, i = r.$$scope);
  }, [s, a, n, i];
}
class El extends pl {
  constructor(e) {
    super(), Ml(this, e, Dl, Al, Nl, { show_label: 0, info: 1 });
  }
}
const {
  SvelteComponent: Tl,
  append: De,
  attr: te,
  bubble: Ol,
  create_component: Jl,
  destroy_component: Xl,
  detach: qt,
  element: Ee,
  init: Yl,
  insert: Ct,
  listen: Gl,
  mount_component: Rl,
  safe_not_equal: Hl,
  set_data: Kl,
  set_style: _e,
  space: Ql,
  text: Ul,
  toggle_class: A,
  transition_in: Wl,
  transition_out: xl
} = window.__gradio__svelte__internal;
function xe(l) {
  let e, t;
  return {
    c() {
      e = Ee("span"), t = Ul(
        /*label*/
        l[1]
      ), te(e, "class", "svelte-1lrphxw");
    },
    m(n, i) {
      Ct(n, e, i), De(e, t);
    },
    p(n, i) {
      i & /*label*/
      2 && Kl(
        t,
        /*label*/
        n[1]
      );
    },
    d(n) {
      n && qt(e);
    }
  };
}
function $l(l) {
  let e, t, n, i, s, a, r, f = (
    /*show_label*/
    l[2] && xe(l)
  );
  return i = new /*Icon*/
  l[0]({}), {
    c() {
      e = Ee("button"), f && f.c(), t = Ql(), n = Ee("div"), Jl(i.$$.fragment), te(n, "class", "svelte-1lrphxw"), A(
        n,
        "small",
        /*size*/
        l[4] === "small"
      ), A(
        n,
        "large",
        /*size*/
        l[4] === "large"
      ), A(
        n,
        "medium",
        /*size*/
        l[4] === "medium"
      ), e.disabled = /*disabled*/
      l[7], te(
        e,
        "aria-label",
        /*label*/
        l[1]
      ), te(
        e,
        "aria-haspopup",
        /*hasPopup*/
        l[8]
      ), te(
        e,
        "title",
        /*label*/
        l[1]
      ), te(e, "class", "svelte-1lrphxw"), A(
        e,
        "pending",
        /*pending*/
        l[3]
      ), A(
        e,
        "padded",
        /*padded*/
        l[5]
      ), A(
        e,
        "highlight",
        /*highlight*/
        l[6]
      ), A(
        e,
        "transparent",
        /*transparent*/
        l[9]
      ), _e(e, "color", !/*disabled*/
      l[7] && /*_color*/
      l[12] ? (
        /*_color*/
        l[12]
      ) : "var(--block-label-text-color)"), _e(e, "--bg-color", /*disabled*/
      l[7] ? "auto" : (
        /*background*/
        l[10]
      )), _e(
        e,
        "margin-left",
        /*offset*/
        l[11] + "px"
      );
    },
    m(o, u) {
      Ct(o, e, u), f && f.m(e, null), De(e, t), De(e, n), Rl(i, n, null), s = !0, a || (r = Gl(
        e,
        "click",
        /*click_handler*/
        l[14]
      ), a = !0);
    },
    p(o, [u]) {
      /*show_label*/
      o[2] ? f ? f.p(o, u) : (f = xe(o), f.c(), f.m(e, t)) : f && (f.d(1), f = null), (!s || u & /*size*/
      16) && A(
        n,
        "small",
        /*size*/
        o[4] === "small"
      ), (!s || u & /*size*/
      16) && A(
        n,
        "large",
        /*size*/
        o[4] === "large"
      ), (!s || u & /*size*/
      16) && A(
        n,
        "medium",
        /*size*/
        o[4] === "medium"
      ), (!s || u & /*disabled*/
      128) && (e.disabled = /*disabled*/
      o[7]), (!s || u & /*label*/
      2) && te(
        e,
        "aria-label",
        /*label*/
        o[1]
      ), (!s || u & /*hasPopup*/
      256) && te(
        e,
        "aria-haspopup",
        /*hasPopup*/
        o[8]
      ), (!s || u & /*label*/
      2) && te(
        e,
        "title",
        /*label*/
        o[1]
      ), (!s || u & /*pending*/
      8) && A(
        e,
        "pending",
        /*pending*/
        o[3]
      ), (!s || u & /*padded*/
      32) && A(
        e,
        "padded",
        /*padded*/
        o[5]
      ), (!s || u & /*highlight*/
      64) && A(
        e,
        "highlight",
        /*highlight*/
        o[6]
      ), (!s || u & /*transparent*/
      512) && A(
        e,
        "transparent",
        /*transparent*/
        o[9]
      ), u & /*disabled, _color*/
      4224 && _e(e, "color", !/*disabled*/
      o[7] && /*_color*/
      o[12] ? (
        /*_color*/
        o[12]
      ) : "var(--block-label-text-color)"), u & /*disabled, background*/
      1152 && _e(e, "--bg-color", /*disabled*/
      o[7] ? "auto" : (
        /*background*/
        o[10]
      )), u & /*offset*/
      2048 && _e(
        e,
        "margin-left",
        /*offset*/
        o[11] + "px"
      );
    },
    i(o) {
      s || (Wl(i.$$.fragment, o), s = !0);
    },
    o(o) {
      xl(i.$$.fragment, o), s = !1;
    },
    d(o) {
      o && qt(e), f && f.d(), Xl(i), a = !1, r();
    }
  };
}
function en(l, e, t) {
  let n, { Icon: i } = e, { label: s = "" } = e, { show_label: a = !1 } = e, { pending: r = !1 } = e, { size: f = "small" } = e, { padded: o = !0 } = e, { highlight: u = !1 } = e, { disabled: _ = !1 } = e, { hasPopup: m = !1 } = e, { color: b = "var(--block-label-text-color)" } = e, { transparent: y = !1 } = e, { background: V = "var(--background-fill-primary)" } = e, { offset: k = 0 } = e;
  function I(c) {
    Ol.call(this, l, c);
  }
  return l.$$set = (c) => {
    "Icon" in c && t(0, i = c.Icon), "label" in c && t(1, s = c.label), "show_label" in c && t(2, a = c.show_label), "pending" in c && t(3, r = c.pending), "size" in c && t(4, f = c.size), "padded" in c && t(5, o = c.padded), "highlight" in c && t(6, u = c.highlight), "disabled" in c && t(7, _ = c.disabled), "hasPopup" in c && t(8, m = c.hasPopup), "color" in c && t(13, b = c.color), "transparent" in c && t(9, y = c.transparent), "background" in c && t(10, V = c.background), "offset" in c && t(11, k = c.offset);
  }, l.$$.update = () => {
    l.$$.dirty & /*highlight, color*/
    8256 && t(12, n = u ? "var(--color-accent)" : b);
  }, [
    i,
    s,
    a,
    r,
    f,
    o,
    u,
    _,
    m,
    y,
    V,
    k,
    n,
    b,
    I
  ];
}
class tn extends Tl {
  constructor(e) {
    super(), Yl(this, e, en, $l, Hl, {
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
  SvelteComponent: ln,
  append: Pe,
  attr: G,
  detach: nn,
  init: fn,
  insert: sn,
  noop: Be,
  safe_not_equal: on,
  set_style: x,
  svg_element: Fe
} = window.__gradio__svelte__internal;
function an(l) {
  let e, t, n, i;
  return {
    c() {
      e = Fe("svg"), t = Fe("g"), n = Fe("path"), i = Fe("path"), G(n, "d", "M18,6L6.087,17.913"), x(n, "fill", "none"), x(n, "fill-rule", "nonzero"), x(n, "stroke-width", "2px"), G(t, "transform", "matrix(1.14096,-0.140958,-0.140958,1.14096,-0.0559523,0.0559523)"), G(i, "d", "M4.364,4.364L19.636,19.636"), x(i, "fill", "none"), x(i, "fill-rule", "nonzero"), x(i, "stroke-width", "2px"), G(e, "width", "100%"), G(e, "height", "100%"), G(e, "viewBox", "0 0 24 24"), G(e, "version", "1.1"), G(e, "xmlns", "http://www.w3.org/2000/svg"), G(e, "xmlns:xlink", "http://www.w3.org/1999/xlink"), G(e, "xml:space", "preserve"), G(e, "stroke", "currentColor"), x(e, "fill-rule", "evenodd"), x(e, "clip-rule", "evenodd"), x(e, "stroke-linecap", "round"), x(e, "stroke-linejoin", "round");
    },
    m(s, a) {
      sn(s, e, a), Pe(e, t), Pe(t, n), Pe(e, i);
    },
    p: Be,
    i: Be,
    o: Be,
    d(s) {
      s && nn(e);
    }
  };
}
class rn extends ln {
  constructor(e) {
    super(), fn(this, e, null, an, on, {});
  }
}
const un = [
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
], $e = {
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
un.reduce(
  (l, { color: e, primary: t, secondary: n }) => ({
    ...l,
    [e]: {
      primary: $e[e][t],
      secondary: $e[e][n]
    }
  }),
  {}
);
function ce(l) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; l > 1e3 && t < e.length - 1; )
    l /= 1e3, t++;
  let n = e[t];
  return (Number.isInteger(l) ? l : l.toFixed(1)) + n;
}
function Ne() {
}
function _n(l, e) {
  return l != l ? e == e : l !== e || l && typeof l == "object" || typeof l == "function";
}
const Ft = typeof window < "u";
let et = Ft ? () => window.performance.now() : () => Date.now(), Lt = Ft ? (l) => requestAnimationFrame(l) : Ne;
const be = /* @__PURE__ */ new Set();
function St(l) {
  be.forEach((e) => {
    e.c(l) || (be.delete(e), e.f());
  }), be.size !== 0 && Lt(St);
}
function dn(l) {
  let e;
  return be.size === 0 && Lt(St), {
    promise: new Promise((t) => {
      be.add(e = { c: l, f: t });
    }),
    abort() {
      be.delete(e);
    }
  };
}
const de = [];
function cn(l, e = Ne) {
  let t;
  const n = /* @__PURE__ */ new Set();
  function i(r) {
    if (_n(l, r) && (l = r, t)) {
      const f = !de.length;
      for (const o of n)
        o[1](), de.push(o, l);
      if (f) {
        for (let o = 0; o < de.length; o += 2)
          de[o][0](de[o + 1]);
        de.length = 0;
      }
    }
  }
  function s(r) {
    i(r(l));
  }
  function a(r, f = Ne) {
    const o = [r, f];
    return n.add(o), n.size === 1 && (t = e(i, s) || Ne), r(l), () => {
      n.delete(o), n.size === 0 && t && (t(), t = null);
    };
  }
  return { set: i, update: s, subscribe: a };
}
function tt(l) {
  return Object.prototype.toString.call(l) === "[object Date]";
}
function Te(l, e, t, n) {
  if (typeof t == "number" || tt(t)) {
    const i = n - t, s = (t - e) / (l.dt || 1 / 60), a = l.opts.stiffness * i, r = l.opts.damping * s, f = (a - r) * l.inv_mass, o = (s + f) * l.dt;
    return Math.abs(o) < l.opts.precision && Math.abs(i) < l.opts.precision ? n : (l.settled = !1, tt(t) ? new Date(t.getTime() + o) : t + o);
  } else {
    if (Array.isArray(t))
      return t.map(
        (i, s) => Te(l, e[s], t[s], n[s])
      );
    if (typeof t == "object") {
      const i = {};
      for (const s in t)
        i[s] = Te(l, e[s], t[s], n[s]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function lt(l, e = {}) {
  const t = cn(l), { stiffness: n = 0.15, damping: i = 0.8, precision: s = 0.01 } = e;
  let a, r, f, o = l, u = l, _ = 1, m = 0, b = !1;
  function y(k, I = {}) {
    u = k;
    const c = f = {};
    return l == null || I.hard || V.stiffness >= 1 && V.damping >= 1 ? (b = !0, a = et(), o = k, t.set(l = u), Promise.resolve()) : (I.soft && (m = 1 / ((I.soft === !0 ? 0.5 : +I.soft) * 60), _ = 0), r || (a = et(), b = !1, r = dn((d) => {
      if (b)
        return b = !1, r = null, !1;
      _ = Math.min(_ + m, 1);
      const S = {
        inv_mass: _,
        opts: V,
        settled: !0,
        dt: (d - a) * 60 / 1e3
      }, z = Te(S, o, l, u);
      return a = d, o = l, t.set(l = z), S.settled && (r = null), !S.settled;
    })), new Promise((d) => {
      r.promise.then(() => {
        c === f && d();
      });
    }));
  }
  const V = {
    set: y,
    update: (k, I) => y(k(u, l), I),
    subscribe: t.subscribe,
    stiffness: n,
    damping: i,
    precision: s
  };
  return V;
}
const {
  SvelteComponent: mn,
  append: R,
  attr: M,
  component_subscribe: nt,
  detach: bn,
  element: gn,
  init: hn,
  insert: wn,
  noop: it,
  safe_not_equal: pn,
  set_style: Le,
  svg_element: H,
  toggle_class: ft
} = window.__gradio__svelte__internal, { onMount: kn } = window.__gradio__svelte__internal;
function vn(l) {
  let e, t, n, i, s, a, r, f, o, u, _, m;
  return {
    c() {
      e = gn("div"), t = H("svg"), n = H("g"), i = H("path"), s = H("path"), a = H("path"), r = H("path"), f = H("g"), o = H("path"), u = H("path"), _ = H("path"), m = H("path"), M(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), M(i, "fill", "#FF7C00"), M(i, "fill-opacity", "0.4"), M(i, "class", "svelte-43sxxs"), M(s, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), M(s, "fill", "#FF7C00"), M(s, "class", "svelte-43sxxs"), M(a, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), M(a, "fill", "#FF7C00"), M(a, "fill-opacity", "0.4"), M(a, "class", "svelte-43sxxs"), M(r, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), M(r, "fill", "#FF7C00"), M(r, "class", "svelte-43sxxs"), Le(n, "transform", "translate(" + /*$top*/
      l[1][0] + "px, " + /*$top*/
      l[1][1] + "px)"), M(o, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), M(o, "fill", "#FF7C00"), M(o, "fill-opacity", "0.4"), M(o, "class", "svelte-43sxxs"), M(u, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), M(u, "fill", "#FF7C00"), M(u, "class", "svelte-43sxxs"), M(_, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), M(_, "fill", "#FF7C00"), M(_, "fill-opacity", "0.4"), M(_, "class", "svelte-43sxxs"), M(m, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), M(m, "fill", "#FF7C00"), M(m, "class", "svelte-43sxxs"), Le(f, "transform", "translate(" + /*$bottom*/
      l[2][0] + "px, " + /*$bottom*/
      l[2][1] + "px)"), M(t, "viewBox", "-1200 -1200 3000 3000"), M(t, "fill", "none"), M(t, "xmlns", "http://www.w3.org/2000/svg"), M(t, "class", "svelte-43sxxs"), M(e, "class", "svelte-43sxxs"), ft(
        e,
        "margin",
        /*margin*/
        l[0]
      );
    },
    m(b, y) {
      wn(b, e, y), R(e, t), R(t, n), R(n, i), R(n, s), R(n, a), R(n, r), R(t, f), R(f, o), R(f, u), R(f, _), R(f, m);
    },
    p(b, [y]) {
      y & /*$top*/
      2 && Le(n, "transform", "translate(" + /*$top*/
      b[1][0] + "px, " + /*$top*/
      b[1][1] + "px)"), y & /*$bottom*/
      4 && Le(f, "transform", "translate(" + /*$bottom*/
      b[2][0] + "px, " + /*$bottom*/
      b[2][1] + "px)"), y & /*margin*/
      1 && ft(
        e,
        "margin",
        /*margin*/
        b[0]
      );
    },
    i: it,
    o: it,
    d(b) {
      b && bn(e);
    }
  };
}
function yn(l, e, t) {
  let n, i;
  var s = this && this.__awaiter || function(b, y, V, k) {
    function I(c) {
      return c instanceof V ? c : new V(function(d) {
        d(c);
      });
    }
    return new (V || (V = Promise))(function(c, d) {
      function S(P) {
        try {
          h(k.next(P));
        } catch (N) {
          d(N);
        }
      }
      function z(P) {
        try {
          h(k.throw(P));
        } catch (N) {
          d(N);
        }
      }
      function h(P) {
        P.done ? c(P.value) : I(P.value).then(S, z);
      }
      h((k = k.apply(b, y || [])).next());
    });
  };
  let { margin: a = !0 } = e;
  const r = lt([0, 0]);
  nt(l, r, (b) => t(1, n = b));
  const f = lt([0, 0]);
  nt(l, f, (b) => t(2, i = b));
  let o;
  function u() {
    return s(this, void 0, void 0, function* () {
      yield Promise.all([r.set([125, 140]), f.set([-125, -140])]), yield Promise.all([r.set([-125, 140]), f.set([125, -140])]), yield Promise.all([r.set([-125, 0]), f.set([125, -0])]), yield Promise.all([r.set([125, 0]), f.set([-125, 0])]);
    });
  }
  function _() {
    return s(this, void 0, void 0, function* () {
      yield u(), o || _();
    });
  }
  function m() {
    return s(this, void 0, void 0, function* () {
      yield Promise.all([r.set([125, 0]), f.set([-125, 0])]), _();
    });
  }
  return kn(() => (m(), () => o = !0)), l.$$set = (b) => {
    "margin" in b && t(0, a = b.margin);
  }, [a, n, i, r, f];
}
class qn extends mn {
  constructor(e) {
    super(), hn(this, e, yn, vn, pn, { margin: 0 });
  }
}
const {
  SvelteComponent: Cn,
  append: oe,
  attr: K,
  binding_callbacks: st,
  check_outros: zt,
  create_component: Mt,
  create_slot: Fn,
  destroy_component: Vt,
  destroy_each: Nt,
  detach: C,
  element: ee,
  empty: ge,
  ensure_array_like: Ie,
  get_all_dirty_from_scope: Ln,
  get_slot_changes: Sn,
  group_outros: It,
  init: zn,
  insert: F,
  mount_component: Zt,
  noop: Oe,
  safe_not_equal: Mn,
  set_data: X,
  set_style: ie,
  space: Q,
  text: j,
  toggle_class: J,
  transition_in: ae,
  transition_out: re,
  update_slot_base: Vn
} = window.__gradio__svelte__internal, { tick: Nn } = window.__gradio__svelte__internal, { onDestroy: In } = window.__gradio__svelte__internal, { createEventDispatcher: Zn } = window.__gradio__svelte__internal, jn = (l) => ({}), ot = (l) => ({});
function at(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n[43] = t, n;
}
function rt(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n;
}
function Pn(l) {
  let e, t, n, i, s = (
    /*i18n*/
    l[1]("common.error") + ""
  ), a, r, f;
  t = new tn({
    props: {
      Icon: rn,
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
  const o = (
    /*#slots*/
    l[30].error
  ), u = Fn(
    o,
    l,
    /*$$scope*/
    l[29],
    ot
  );
  return {
    c() {
      e = ee("div"), Mt(t.$$.fragment), n = Q(), i = ee("span"), a = j(s), r = Q(), u && u.c(), K(e, "class", "clear-status svelte-1yk38uw"), K(i, "class", "error svelte-1yk38uw");
    },
    m(_, m) {
      F(_, e, m), Zt(t, e, null), F(_, n, m), F(_, i, m), oe(i, a), F(_, r, m), u && u.m(_, m), f = !0;
    },
    p(_, m) {
      const b = {};
      m[0] & /*i18n*/
      2 && (b.label = /*i18n*/
      _[1]("common.clear")), t.$set(b), (!f || m[0] & /*i18n*/
      2) && s !== (s = /*i18n*/
      _[1]("common.error") + "") && X(a, s), u && u.p && (!f || m[0] & /*$$scope*/
      536870912) && Vn(
        u,
        o,
        _,
        /*$$scope*/
        _[29],
        f ? Sn(
          o,
          /*$$scope*/
          _[29],
          m,
          jn
        ) : Ln(
          /*$$scope*/
          _[29]
        ),
        ot
      );
    },
    i(_) {
      f || (ae(t.$$.fragment, _), ae(u, _), f = !0);
    },
    o(_) {
      re(t.$$.fragment, _), re(u, _), f = !1;
    },
    d(_) {
      _ && (C(e), C(n), C(i), C(r)), Vt(t), u && u.d(_);
    }
  };
}
function Bn(l) {
  let e, t, n, i, s, a, r, f, o, u = (
    /*variant*/
    l[8] === "default" && /*show_eta_bar*/
    l[18] && /*show_progress*/
    l[6] === "full" && ut(l)
  );
  function _(d, S) {
    if (
      /*progress*/
      d[7]
    )
      return En;
    if (
      /*queue_position*/
      d[2] !== null && /*queue_size*/
      d[3] !== void 0 && /*queue_position*/
      d[2] >= 0
    )
      return Dn;
    if (
      /*queue_position*/
      d[2] === 0
    )
      return An;
  }
  let m = _(l), b = m && m(l), y = (
    /*timer*/
    l[5] && ct(l)
  );
  const V = [Xn, Jn], k = [];
  function I(d, S) {
    return (
      /*last_progress_level*/
      d[15] != null ? 0 : (
        /*show_progress*/
        d[6] === "full" ? 1 : -1
      )
    );
  }
  ~(s = I(l)) && (a = k[s] = V[s](l));
  let c = !/*timer*/
  l[5] && kt(l);
  return {
    c() {
      u && u.c(), e = Q(), t = ee("div"), b && b.c(), n = Q(), y && y.c(), i = Q(), a && a.c(), r = Q(), c && c.c(), f = ge(), K(t, "class", "progress-text svelte-1yk38uw"), J(
        t,
        "meta-text-center",
        /*variant*/
        l[8] === "center"
      ), J(
        t,
        "meta-text",
        /*variant*/
        l[8] === "default"
      );
    },
    m(d, S) {
      u && u.m(d, S), F(d, e, S), F(d, t, S), b && b.m(t, null), oe(t, n), y && y.m(t, null), F(d, i, S), ~s && k[s].m(d, S), F(d, r, S), c && c.m(d, S), F(d, f, S), o = !0;
    },
    p(d, S) {
      /*variant*/
      d[8] === "default" && /*show_eta_bar*/
      d[18] && /*show_progress*/
      d[6] === "full" ? u ? u.p(d, S) : (u = ut(d), u.c(), u.m(e.parentNode, e)) : u && (u.d(1), u = null), m === (m = _(d)) && b ? b.p(d, S) : (b && b.d(1), b = m && m(d), b && (b.c(), b.m(t, n))), /*timer*/
      d[5] ? y ? y.p(d, S) : (y = ct(d), y.c(), y.m(t, null)) : y && (y.d(1), y = null), (!o || S[0] & /*variant*/
      256) && J(
        t,
        "meta-text-center",
        /*variant*/
        d[8] === "center"
      ), (!o || S[0] & /*variant*/
      256) && J(
        t,
        "meta-text",
        /*variant*/
        d[8] === "default"
      );
      let z = s;
      s = I(d), s === z ? ~s && k[s].p(d, S) : (a && (It(), re(k[z], 1, 1, () => {
        k[z] = null;
      }), zt()), ~s ? (a = k[s], a ? a.p(d, S) : (a = k[s] = V[s](d), a.c()), ae(a, 1), a.m(r.parentNode, r)) : a = null), /*timer*/
      d[5] ? c && (c.d(1), c = null) : c ? c.p(d, S) : (c = kt(d), c.c(), c.m(f.parentNode, f));
    },
    i(d) {
      o || (ae(a), o = !0);
    },
    o(d) {
      re(a), o = !1;
    },
    d(d) {
      d && (C(e), C(t), C(i), C(r), C(f)), u && u.d(d), b && b.d(), y && y.d(), ~s && k[s].d(d), c && c.d(d);
    }
  };
}
function ut(l) {
  let e, t = `translateX(${/*eta_level*/
  (l[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = ee("div"), K(e, "class", "eta-bar svelte-1yk38uw"), ie(e, "transform", t);
    },
    m(n, i) {
      F(n, e, i);
    },
    p(n, i) {
      i[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && ie(e, "transform", t);
    },
    d(n) {
      n && C(e);
    }
  };
}
function An(l) {
  let e;
  return {
    c() {
      e = j("processing |");
    },
    m(t, n) {
      F(t, e, n);
    },
    p: Oe,
    d(t) {
      t && C(e);
    }
  };
}
function Dn(l) {
  let e, t = (
    /*queue_position*/
    l[2] + 1 + ""
  ), n, i, s, a;
  return {
    c() {
      e = j("queue: "), n = j(t), i = j("/"), s = j(
        /*queue_size*/
        l[3]
      ), a = j(" |");
    },
    m(r, f) {
      F(r, e, f), F(r, n, f), F(r, i, f), F(r, s, f), F(r, a, f);
    },
    p(r, f) {
      f[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      r[2] + 1 + "") && X(n, t), f[0] & /*queue_size*/
      8 && X(
        s,
        /*queue_size*/
        r[3]
      );
    },
    d(r) {
      r && (C(e), C(n), C(i), C(s), C(a));
    }
  };
}
function En(l) {
  let e, t = Ie(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = dt(rt(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = ge();
    },
    m(i, s) {
      for (let a = 0; a < n.length; a += 1)
        n[a] && n[a].m(i, s);
      F(i, e, s);
    },
    p(i, s) {
      if (s[0] & /*progress*/
      128) {
        t = Ie(
          /*progress*/
          i[7]
        );
        let a;
        for (a = 0; a < t.length; a += 1) {
          const r = rt(i, t, a);
          n[a] ? n[a].p(r, s) : (n[a] = dt(r), n[a].c(), n[a].m(e.parentNode, e));
        }
        for (; a < n.length; a += 1)
          n[a].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && C(e), Nt(n, i);
    }
  };
}
function _t(l) {
  let e, t = (
    /*p*/
    l[41].unit + ""
  ), n, i, s = " ", a;
  function r(u, _) {
    return (
      /*p*/
      u[41].length != null ? On : Tn
    );
  }
  let f = r(l), o = f(l);
  return {
    c() {
      o.c(), e = Q(), n = j(t), i = j(" | "), a = j(s);
    },
    m(u, _) {
      o.m(u, _), F(u, e, _), F(u, n, _), F(u, i, _), F(u, a, _);
    },
    p(u, _) {
      f === (f = r(u)) && o ? o.p(u, _) : (o.d(1), o = f(u), o && (o.c(), o.m(e.parentNode, e))), _[0] & /*progress*/
      128 && t !== (t = /*p*/
      u[41].unit + "") && X(n, t);
    },
    d(u) {
      u && (C(e), C(n), C(i), C(a)), o.d(u);
    }
  };
}
function Tn(l) {
  let e = ce(
    /*p*/
    l[41].index || 0
  ) + "", t;
  return {
    c() {
      t = j(e);
    },
    m(n, i) {
      F(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = ce(
        /*p*/
        n[41].index || 0
      ) + "") && X(t, e);
    },
    d(n) {
      n && C(t);
    }
  };
}
function On(l) {
  let e = ce(
    /*p*/
    l[41].index || 0
  ) + "", t, n, i = ce(
    /*p*/
    l[41].length
  ) + "", s;
  return {
    c() {
      t = j(e), n = j("/"), s = j(i);
    },
    m(a, r) {
      F(a, t, r), F(a, n, r), F(a, s, r);
    },
    p(a, r) {
      r[0] & /*progress*/
      128 && e !== (e = ce(
        /*p*/
        a[41].index || 0
      ) + "") && X(t, e), r[0] & /*progress*/
      128 && i !== (i = ce(
        /*p*/
        a[41].length
      ) + "") && X(s, i);
    },
    d(a) {
      a && (C(t), C(n), C(s));
    }
  };
}
function dt(l) {
  let e, t = (
    /*p*/
    l[41].index != null && _t(l)
  );
  return {
    c() {
      t && t.c(), e = ge();
    },
    m(n, i) {
      t && t.m(n, i), F(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[41].index != null ? t ? t.p(n, i) : (t = _t(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && C(e), t && t.d(n);
    }
  };
}
function ct(l) {
  let e, t = (
    /*eta*/
    l[0] ? `/${/*formatted_eta*/
    l[19]}` : ""
  ), n, i;
  return {
    c() {
      e = j(
        /*formatted_timer*/
        l[20]
      ), n = j(t), i = j("s");
    },
    m(s, a) {
      F(s, e, a), F(s, n, a), F(s, i, a);
    },
    p(s, a) {
      a[0] & /*formatted_timer*/
      1048576 && X(
        e,
        /*formatted_timer*/
        s[20]
      ), a[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      s[0] ? `/${/*formatted_eta*/
      s[19]}` : "") && X(n, t);
    },
    d(s) {
      s && (C(e), C(n), C(i));
    }
  };
}
function Jn(l) {
  let e, t;
  return e = new qn({
    props: { margin: (
      /*variant*/
      l[8] === "default"
    ) }
  }), {
    c() {
      Mt(e.$$.fragment);
    },
    m(n, i) {
      Zt(e, n, i), t = !0;
    },
    p(n, i) {
      const s = {};
      i[0] & /*variant*/
      256 && (s.margin = /*variant*/
      n[8] === "default"), e.$set(s);
    },
    i(n) {
      t || (ae(e.$$.fragment, n), t = !0);
    },
    o(n) {
      re(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Vt(e, n);
    }
  };
}
function Xn(l) {
  let e, t, n, i, s, a = `${/*last_progress_level*/
  l[15] * 100}%`, r = (
    /*progress*/
    l[7] != null && mt(l)
  );
  return {
    c() {
      e = ee("div"), t = ee("div"), r && r.c(), n = Q(), i = ee("div"), s = ee("div"), K(t, "class", "progress-level-inner svelte-1yk38uw"), K(s, "class", "progress-bar svelte-1yk38uw"), ie(s, "width", a), K(i, "class", "progress-bar-wrap svelte-1yk38uw"), K(e, "class", "progress-level svelte-1yk38uw");
    },
    m(f, o) {
      F(f, e, o), oe(e, t), r && r.m(t, null), oe(e, n), oe(e, i), oe(i, s), l[31](s);
    },
    p(f, o) {
      /*progress*/
      f[7] != null ? r ? r.p(f, o) : (r = mt(f), r.c(), r.m(t, null)) : r && (r.d(1), r = null), o[0] & /*last_progress_level*/
      32768 && a !== (a = `${/*last_progress_level*/
      f[15] * 100}%`) && ie(s, "width", a);
    },
    i: Oe,
    o: Oe,
    d(f) {
      f && C(e), r && r.d(), l[31](null);
    }
  };
}
function mt(l) {
  let e, t = Ie(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = pt(at(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = ge();
    },
    m(i, s) {
      for (let a = 0; a < n.length; a += 1)
        n[a] && n[a].m(i, s);
      F(i, e, s);
    },
    p(i, s) {
      if (s[0] & /*progress_level, progress*/
      16512) {
        t = Ie(
          /*progress*/
          i[7]
        );
        let a;
        for (a = 0; a < t.length; a += 1) {
          const r = at(i, t, a);
          n[a] ? n[a].p(r, s) : (n[a] = pt(r), n[a].c(), n[a].m(e.parentNode, e));
        }
        for (; a < n.length; a += 1)
          n[a].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && C(e), Nt(n, i);
    }
  };
}
function bt(l) {
  let e, t, n, i, s = (
    /*i*/
    l[43] !== 0 && Yn()
  ), a = (
    /*p*/
    l[41].desc != null && gt(l)
  ), r = (
    /*p*/
    l[41].desc != null && /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[43]
    ] != null && ht()
  ), f = (
    /*progress_level*/
    l[14] != null && wt(l)
  );
  return {
    c() {
      s && s.c(), e = Q(), a && a.c(), t = Q(), r && r.c(), n = Q(), f && f.c(), i = ge();
    },
    m(o, u) {
      s && s.m(o, u), F(o, e, u), a && a.m(o, u), F(o, t, u), r && r.m(o, u), F(o, n, u), f && f.m(o, u), F(o, i, u);
    },
    p(o, u) {
      /*p*/
      o[41].desc != null ? a ? a.p(o, u) : (a = gt(o), a.c(), a.m(t.parentNode, t)) : a && (a.d(1), a = null), /*p*/
      o[41].desc != null && /*progress_level*/
      o[14] && /*progress_level*/
      o[14][
        /*i*/
        o[43]
      ] != null ? r || (r = ht(), r.c(), r.m(n.parentNode, n)) : r && (r.d(1), r = null), /*progress_level*/
      o[14] != null ? f ? f.p(o, u) : (f = wt(o), f.c(), f.m(i.parentNode, i)) : f && (f.d(1), f = null);
    },
    d(o) {
      o && (C(e), C(t), C(n), C(i)), s && s.d(o), a && a.d(o), r && r.d(o), f && f.d(o);
    }
  };
}
function Yn(l) {
  let e;
  return {
    c() {
      e = j(" /");
    },
    m(t, n) {
      F(t, e, n);
    },
    d(t) {
      t && C(e);
    }
  };
}
function gt(l) {
  let e = (
    /*p*/
    l[41].desc + ""
  ), t;
  return {
    c() {
      t = j(e);
    },
    m(n, i) {
      F(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = /*p*/
      n[41].desc + "") && X(t, e);
    },
    d(n) {
      n && C(t);
    }
  };
}
function ht(l) {
  let e;
  return {
    c() {
      e = j("-");
    },
    m(t, n) {
      F(t, e, n);
    },
    d(t) {
      t && C(e);
    }
  };
}
function wt(l) {
  let e = (100 * /*progress_level*/
  (l[14][
    /*i*/
    l[43]
  ] || 0)).toFixed(1) + "", t, n;
  return {
    c() {
      t = j(e), n = j("%");
    },
    m(i, s) {
      F(i, t, s), F(i, n, s);
    },
    p(i, s) {
      s[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[43]
      ] || 0)).toFixed(1) + "") && X(t, e);
    },
    d(i) {
      i && (C(t), C(n));
    }
  };
}
function pt(l) {
  let e, t = (
    /*p*/
    (l[41].desc != null || /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[43]
    ] != null) && bt(l)
  );
  return {
    c() {
      t && t.c(), e = ge();
    },
    m(n, i) {
      t && t.m(n, i), F(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[41].desc != null || /*progress_level*/
      n[14] && /*progress_level*/
      n[14][
        /*i*/
        n[43]
      ] != null ? t ? t.p(n, i) : (t = bt(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && C(e), t && t.d(n);
    }
  };
}
function kt(l) {
  let e, t;
  return {
    c() {
      e = ee("p"), t = j(
        /*loading_text*/
        l[9]
      ), K(e, "class", "loading svelte-1yk38uw");
    },
    m(n, i) {
      F(n, e, i), oe(e, t);
    },
    p(n, i) {
      i[0] & /*loading_text*/
      512 && X(
        t,
        /*loading_text*/
        n[9]
      );
    },
    d(n) {
      n && C(e);
    }
  };
}
function Gn(l) {
  let e, t, n, i, s;
  const a = [Bn, Pn], r = [];
  function f(o, u) {
    return (
      /*status*/
      o[4] === "pending" ? 0 : (
        /*status*/
        o[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = f(l)) && (n = r[t] = a[t](l)), {
    c() {
      e = ee("div"), n && n.c(), K(e, "class", i = "wrap " + /*variant*/
      l[8] + " " + /*show_progress*/
      l[6] + " svelte-1yk38uw"), J(e, "hide", !/*status*/
      l[4] || /*status*/
      l[4] === "complete" || /*show_progress*/
      l[6] === "hidden"), J(
        e,
        "translucent",
        /*variant*/
        l[8] === "center" && /*status*/
        (l[4] === "pending" || /*status*/
        l[4] === "error") || /*translucent*/
        l[11] || /*show_progress*/
        l[6] === "minimal"
      ), J(
        e,
        "generating",
        /*status*/
        l[4] === "generating"
      ), J(
        e,
        "border",
        /*border*/
        l[12]
      ), ie(
        e,
        "position",
        /*absolute*/
        l[10] ? "absolute" : "static"
      ), ie(
        e,
        "padding",
        /*absolute*/
        l[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(o, u) {
      F(o, e, u), ~t && r[t].m(e, null), l[33](e), s = !0;
    },
    p(o, u) {
      let _ = t;
      t = f(o), t === _ ? ~t && r[t].p(o, u) : (n && (It(), re(r[_], 1, 1, () => {
        r[_] = null;
      }), zt()), ~t ? (n = r[t], n ? n.p(o, u) : (n = r[t] = a[t](o), n.c()), ae(n, 1), n.m(e, null)) : n = null), (!s || u[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      o[8] + " " + /*show_progress*/
      o[6] + " svelte-1yk38uw")) && K(e, "class", i), (!s || u[0] & /*variant, show_progress, status, show_progress*/
      336) && J(e, "hide", !/*status*/
      o[4] || /*status*/
      o[4] === "complete" || /*show_progress*/
      o[6] === "hidden"), (!s || u[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && J(
        e,
        "translucent",
        /*variant*/
        o[8] === "center" && /*status*/
        (o[4] === "pending" || /*status*/
        o[4] === "error") || /*translucent*/
        o[11] || /*show_progress*/
        o[6] === "minimal"
      ), (!s || u[0] & /*variant, show_progress, status*/
      336) && J(
        e,
        "generating",
        /*status*/
        o[4] === "generating"
      ), (!s || u[0] & /*variant, show_progress, border*/
      4416) && J(
        e,
        "border",
        /*border*/
        o[12]
      ), u[0] & /*absolute*/
      1024 && ie(
        e,
        "position",
        /*absolute*/
        o[10] ? "absolute" : "static"
      ), u[0] & /*absolute*/
      1024 && ie(
        e,
        "padding",
        /*absolute*/
        o[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(o) {
      s || (ae(n), s = !0);
    },
    o(o) {
      re(n), s = !1;
    },
    d(o) {
      o && C(e), ~t && r[t].d(), l[33](null);
    }
  };
}
var Rn = function(l, e, t, n) {
  function i(s) {
    return s instanceof t ? s : new t(function(a) {
      a(s);
    });
  }
  return new (t || (t = Promise))(function(s, a) {
    function r(u) {
      try {
        o(n.next(u));
      } catch (_) {
        a(_);
      }
    }
    function f(u) {
      try {
        o(n.throw(u));
      } catch (_) {
        a(_);
      }
    }
    function o(u) {
      u.done ? s(u.value) : i(u.value).then(r, f);
    }
    o((n = n.apply(l, e || [])).next());
  });
};
let Se = [], Ae = !1;
function Hn(l) {
  return Rn(this, arguments, void 0, function* (e, t = !0) {
    if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
      if (Se.push(e), !Ae)
        Ae = !0;
      else
        return;
      yield Nn(), requestAnimationFrame(() => {
        let n = [0, 0];
        for (let i = 0; i < Se.length; i++) {
          const a = Se[i].getBoundingClientRect();
          (i === 0 || a.top + window.scrollY <= n[0]) && (n[0] = a.top + window.scrollY, n[1] = i);
        }
        window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), Ae = !1, Se = [];
      });
    }
  });
}
function Kn(l, e, t) {
  let n, { $$slots: i = {}, $$scope: s } = e;
  this && this.__awaiter;
  const a = Zn();
  let { i18n: r } = e, { eta: f = null } = e, { queue_position: o } = e, { queue_size: u } = e, { status: _ } = e, { scroll_to_output: m = !1 } = e, { timer: b = !0 } = e, { show_progress: y = "full" } = e, { message: V = null } = e, { progress: k = null } = e, { variant: I = "default" } = e, { loading_text: c = "Loading..." } = e, { absolute: d = !0 } = e, { translucent: S = !1 } = e, { border: z = !1 } = e, { autoscroll: h } = e, P, N = !1, B = 0, q = 0, Z = null, Y = null, le = 0, D = null, g, v = null, p = !0;
  const U = () => {
    t(0, f = t(27, Z = t(19, ve = null))), t(25, B = performance.now()), t(26, q = 0), N = !0, He();
  };
  function He() {
    requestAnimationFrame(() => {
      t(26, q = (performance.now() - B) / 1e3), N && He();
    });
  }
  function Ke() {
    t(26, q = 0), t(0, f = t(27, Z = t(19, ve = null))), N && (N = !1);
  }
  In(() => {
    N && Ke();
  });
  let ve = null;
  function jt(w) {
    st[w ? "unshift" : "push"](() => {
      v = w, t(16, v), t(7, k), t(14, D), t(15, g);
    });
  }
  const Pt = () => {
    a("clear_status");
  };
  function Bt(w) {
    st[w ? "unshift" : "push"](() => {
      P = w, t(13, P);
    });
  }
  return l.$$set = (w) => {
    "i18n" in w && t(1, r = w.i18n), "eta" in w && t(0, f = w.eta), "queue_position" in w && t(2, o = w.queue_position), "queue_size" in w && t(3, u = w.queue_size), "status" in w && t(4, _ = w.status), "scroll_to_output" in w && t(22, m = w.scroll_to_output), "timer" in w && t(5, b = w.timer), "show_progress" in w && t(6, y = w.show_progress), "message" in w && t(23, V = w.message), "progress" in w && t(7, k = w.progress), "variant" in w && t(8, I = w.variant), "loading_text" in w && t(9, c = w.loading_text), "absolute" in w && t(10, d = w.absolute), "translucent" in w && t(11, S = w.translucent), "border" in w && t(12, z = w.border), "autoscroll" in w && t(24, h = w.autoscroll), "$$scope" in w && t(29, s = w.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    436207617 && (f === null && t(0, f = Z), f != null && Z !== f && (t(28, Y = (performance.now() - B) / 1e3 + f), t(19, ve = Y.toFixed(1)), t(27, Z = f))), l.$$.dirty[0] & /*eta_from_start, timer_diff*/
    335544320 && t(17, le = Y === null || Y <= 0 || !q ? null : Math.min(q / Y, 1)), l.$$.dirty[0] & /*progress*/
    128 && k != null && t(18, p = !1), l.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (k != null ? t(14, D = k.map((w) => {
      if (w.index != null && w.length != null)
        return w.index / w.length;
      if (w.progress != null)
        return w.progress;
    })) : t(14, D = null), D ? (t(15, g = D[D.length - 1]), v && (g === 0 ? t(16, v.style.transition = "0", v) : t(16, v.style.transition = "150ms", v))) : t(15, g = void 0)), l.$$.dirty[0] & /*status*/
    16 && (_ === "pending" ? U() : Ke()), l.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && P && m && (_ === "pending" || _ === "complete") && Hn(P, h), l.$$.dirty[0] & /*status, message*/
    8388624, l.$$.dirty[0] & /*timer_diff*/
    67108864 && t(20, n = q.toFixed(1));
  }, [
    f,
    r,
    o,
    u,
    _,
    b,
    y,
    k,
    I,
    c,
    d,
    S,
    z,
    P,
    D,
    g,
    v,
    le,
    p,
    ve,
    n,
    a,
    m,
    V,
    h,
    B,
    q,
    Z,
    Y,
    s,
    i,
    jt,
    Pt,
    Bt
  ];
}
class Qn extends Cn {
  constructor(e) {
    super(), zn(
      this,
      e,
      Kn,
      Gn,
      Mn,
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
  SvelteComponent: Un,
  append: T,
  assign: Wn,
  attr: L,
  create_component: Je,
  destroy_component: Xe,
  detach: pe,
  element: $,
  get_spread_object: xn,
  get_spread_update: $n,
  init: ei,
  insert: ke,
  listen: O,
  mount_component: Ye,
  run_all: ti,
  safe_not_equal: li,
  set_data: ni,
  set_input_value: ne,
  space: se,
  text: ii,
  to_number: me,
  transition_in: Ge,
  transition_out: Re
} = window.__gradio__svelte__internal;
function fi(l) {
  let e;
  return {
    c() {
      e = ii(
        /*label*/
        l[4]
      );
    },
    m(t, n) {
      ke(t, e, n);
    },
    p(t, n) {
      n & /*label*/
      16 && ni(
        e,
        /*label*/
        t[4]
      );
    },
    d(t) {
      t && pe(e);
    }
  };
}
function si(l) {
  let e, t, n, i, s, a, r, f, o, u, _, m, b, y, V, k, I, c, d, S, z, h, P, N, B, q, Z, Y;
  const le = [
    { autoscroll: (
      /*gradio*/
      l[0].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      l[0].i18n
    ) },
    /*loading_status*/
    l[14]
  ];
  let D = {};
  for (let g = 0; g < le.length; g += 1)
    D = Wn(D, le[g]);
  return e = new Qn({ props: D }), e.$on(
    "clear_status",
    /*clear_status_handler*/
    l[24]
  ), s = new El({
    props: {
      show_label: (
        /*show_label*/
        l[12]
      ),
      info: (
        /*info*/
        l[5]
      ),
      $$slots: { default: [fi] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      Je(e.$$.fragment), t = se(), n = $("div"), i = $("div"), Je(s.$$.fragment), a = se(), r = $("div"), f = $("input"), _ = se(), m = $("input"), V = se(), k = $("div"), I = $("div"), c = se(), d = $("div"), S = se(), z = $("input"), P = se(), N = $("input"), L(f, "aria-label", o = `max input for ${/*label*/
      l[4]}`), L(f, "data-testid", "max-input"), L(f, "type", "number"), L(
        f,
        "min",
        /*minimum*/
        l[9]
      ), L(
        f,
        "max",
        /*maximum*/
        l[10]
      ), f.disabled = u = !/*interactive*/
      l[13], L(f, "class", "svelte-1dsqogo"), L(m, "aria-label", b = `min input for ${/*label*/
      l[4]}`), L(m, "data-testid", "min-input"), L(m, "type", "number"), L(
        m,
        "min",
        /*minimum*/
        l[9]
      ), L(
        m,
        "max",
        /*maximum*/
        l[10]
      ), m.disabled = y = !/*interactive*/
      l[13], L(m, "class", "svelte-1dsqogo"), L(r, "class", "numbers svelte-1dsqogo"), L(i, "class", "head svelte-1dsqogo"), L(n, "class", "wrap svelte-1dsqogo"), L(I, "class", "range-bg svelte-1dsqogo"), L(d, "class", "range-line svelte-1dsqogo"), L(
        d,
        "style",
        /*rangeLine*/
        l[17]
      ), L(z, "type", "range"), z.disabled = h = !/*interactive*/
      l[13], L(
        z,
        "min",
        /*minimum*/
        l[9]
      ), L(
        z,
        "max",
        /*maximum*/
        l[10]
      ), L(
        z,
        "step",
        /*step*/
        l[11]
      ), L(z, "class", "svelte-1dsqogo"), L(N, "type", "range"), N.disabled = B = !/*interactive*/
      l[13], L(
        N,
        "min",
        /*minimum*/
        l[9]
      ), L(
        N,
        "max",
        /*maximum*/
        l[10]
      ), L(
        N,
        "step",
        /*step*/
        l[11]
      ), L(N, "class", "svelte-1dsqogo"), L(k, "class", "range-slider svelte-1dsqogo");
    },
    m(g, v) {
      Ye(e, g, v), ke(g, t, v), ke(g, n, v), T(n, i), Ye(s, i, null), T(i, a), T(i, r), T(r, f), ne(
        f,
        /*selected_max*/
        l[16]
      ), T(r, _), T(r, m), ne(
        m,
        /*selected_min*/
        l[15]
      ), ke(g, V, v), ke(g, k, v), T(k, I), T(k, c), T(k, d), T(k, S), T(k, z), ne(
        z,
        /*selected_min*/
        l[15]
      ), T(k, P), T(k, N), ne(
        N,
        /*selected_max*/
        l[16]
      ), q = !0, Z || (Y = [
        O(
          f,
          "input",
          /*input0_input_handler*/
          l[25]
        ),
        O(
          f,
          "pointerup",
          /*handle_release*/
          l[20]
        ),
        O(
          m,
          "input",
          /*input1_input_handler*/
          l[26]
        ),
        O(
          m,
          "pointerup",
          /*handle_release*/
          l[20]
        ),
        O(
          z,
          "change",
          /*input2_change_input_handler*/
          l[27]
        ),
        O(
          z,
          "input",
          /*input2_change_input_handler*/
          l[27]
        ),
        O(
          z,
          "input",
          /*handle_min_change*/
          l[18]
        ),
        O(
          z,
          "pointerup",
          /*handle_release*/
          l[20]
        ),
        O(
          N,
          "change",
          /*input3_change_input_handler*/
          l[28]
        ),
        O(
          N,
          "input",
          /*input3_change_input_handler*/
          l[28]
        ),
        O(
          N,
          "input",
          /*handle_max_change*/
          l[19]
        ),
        O(
          N,
          "pointerup",
          /*handle_release*/
          l[20]
        )
      ], Z = !0);
    },
    p(g, v) {
      const p = v & /*gradio, loading_status*/
      16385 ? $n(le, [
        v & /*gradio*/
        1 && { autoscroll: (
          /*gradio*/
          g[0].autoscroll
        ) },
        v & /*gradio*/
        1 && { i18n: (
          /*gradio*/
          g[0].i18n
        ) },
        v & /*loading_status*/
        16384 && xn(
          /*loading_status*/
          g[14]
        )
      ]) : {};
      e.$set(p);
      const U = {};
      v & /*show_label*/
      4096 && (U.show_label = /*show_label*/
      g[12]), v & /*info*/
      32 && (U.info = /*info*/
      g[5]), v & /*$$scope, label*/
      1073741840 && (U.$$scope = { dirty: v, ctx: g }), s.$set(U), (!q || v & /*label*/
      16 && o !== (o = `max input for ${/*label*/
      g[4]}`)) && L(f, "aria-label", o), (!q || v & /*minimum*/
      512) && L(
        f,
        "min",
        /*minimum*/
        g[9]
      ), (!q || v & /*maximum*/
      1024) && L(
        f,
        "max",
        /*maximum*/
        g[10]
      ), (!q || v & /*interactive*/
      8192 && u !== (u = !/*interactive*/
      g[13])) && (f.disabled = u), v & /*selected_max*/
      65536 && me(f.value) !== /*selected_max*/
      g[16] && ne(
        f,
        /*selected_max*/
        g[16]
      ), (!q || v & /*label*/
      16 && b !== (b = `min input for ${/*label*/
      g[4]}`)) && L(m, "aria-label", b), (!q || v & /*minimum*/
      512) && L(
        m,
        "min",
        /*minimum*/
        g[9]
      ), (!q || v & /*maximum*/
      1024) && L(
        m,
        "max",
        /*maximum*/
        g[10]
      ), (!q || v & /*interactive*/
      8192 && y !== (y = !/*interactive*/
      g[13])) && (m.disabled = y), v & /*selected_min*/
      32768 && me(m.value) !== /*selected_min*/
      g[15] && ne(
        m,
        /*selected_min*/
        g[15]
      ), (!q || v & /*rangeLine*/
      131072) && L(
        d,
        "style",
        /*rangeLine*/
        g[17]
      ), (!q || v & /*interactive*/
      8192 && h !== (h = !/*interactive*/
      g[13])) && (z.disabled = h), (!q || v & /*minimum*/
      512) && L(
        z,
        "min",
        /*minimum*/
        g[9]
      ), (!q || v & /*maximum*/
      1024) && L(
        z,
        "max",
        /*maximum*/
        g[10]
      ), (!q || v & /*step*/
      2048) && L(
        z,
        "step",
        /*step*/
        g[11]
      ), v & /*selected_min*/
      32768 && ne(
        z,
        /*selected_min*/
        g[15]
      ), (!q || v & /*interactive*/
      8192 && B !== (B = !/*interactive*/
      g[13])) && (N.disabled = B), (!q || v & /*minimum*/
      512) && L(
        N,
        "min",
        /*minimum*/
        g[9]
      ), (!q || v & /*maximum*/
      1024) && L(
        N,
        "max",
        /*maximum*/
        g[10]
      ), (!q || v & /*step*/
      2048) && L(
        N,
        "step",
        /*step*/
        g[11]
      ), v & /*selected_max*/
      65536 && ne(
        N,
        /*selected_max*/
        g[16]
      );
    },
    i(g) {
      q || (Ge(e.$$.fragment, g), Ge(s.$$.fragment, g), q = !0);
    },
    o(g) {
      Re(e.$$.fragment, g), Re(s.$$.fragment, g), q = !1;
    },
    d(g) {
      g && (pe(t), pe(n), pe(V), pe(k)), Xe(e, g), Xe(s), Z = !1, ti(Y);
    }
  };
}
function oi(l) {
  let e, t;
  return e = new ll({
    props: {
      visible: (
        /*visible*/
        l[3]
      ),
      elem_id: (
        /*elem_id*/
        l[1]
      ),
      elem_classes: (
        /*elem_classes*/
        l[2]
      ),
      container: (
        /*container*/
        l[6]
      ),
      scale: (
        /*scale*/
        l[7]
      ),
      min_width: (
        /*min_width*/
        l[8]
      ),
      $$slots: { default: [si] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      Je(e.$$.fragment);
    },
    m(n, i) {
      Ye(e, n, i), t = !0;
    },
    p(n, [i]) {
      const s = {};
      i & /*visible*/
      8 && (s.visible = /*visible*/
      n[3]), i & /*elem_id*/
      2 && (s.elem_id = /*elem_id*/
      n[1]), i & /*elem_classes*/
      4 && (s.elem_classes = /*elem_classes*/
      n[2]), i & /*container*/
      64 && (s.container = /*container*/
      n[6]), i & /*scale*/
      128 && (s.scale = /*scale*/
      n[7]), i & /*min_width*/
      256 && (s.min_width = /*min_width*/
      n[8]), i & /*$$scope, interactive, minimum, maximum, step, selected_max, selected_min, rangeLine, label, show_label, info, gradio, loading_status*/
      1074003505 && (s.$$scope = { dirty: i, ctx: n }), e.$set(s);
    },
    i(n) {
      t || (Ge(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Re(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Xe(e, n);
    }
  };
}
function ai(l, e, t) {
  let n, { gradio: i } = e, { elem_id: s = "" } = e, { elem_classes: a = [] } = e, { visible: r = !0 } = e, { value: f } = e, { label: o = i.i18n("slider.slider") } = e, { info: u = void 0 } = e, { container: _ = !0 } = e, { scale: m = null } = e, { min_width: b = void 0 } = e, { minimum: y = 0 } = e, { maximum: V = 100 } = e, { step: k } = e, { show_label: I } = e, { interactive: c } = e, { loading_status: d } = e, { value_is_output: S = !1 } = e;
  function z(p, U) {
    t(21, f = [p, U]), i.dispatch("change", [p, U]), S || i.dispatch("input", [p, U]);
  }
  function h(p) {
    t(15, q = parseInt(p.target.value)), q > Z && t(16, Z = q);
  }
  function P(p) {
    t(16, Z = parseInt(p.target.value)), Z < q && t(15, q = Z);
  }
  function N(p) {
    i.dispatch("release", f);
  }
  let B = f, [q, Z] = f;
  const Y = () => i.dispatch("clear_status", d);
  function le() {
    Z = me(this.value), t(16, Z), t(23, B), t(21, f);
  }
  function D() {
    q = me(this.value), t(15, q), t(23, B), t(21, f);
  }
  function g() {
    q = me(this.value), t(15, q), t(23, B), t(21, f);
  }
  function v() {
    Z = me(this.value), t(16, Z), t(23, B), t(21, f);
  }
  return l.$$set = (p) => {
    "gradio" in p && t(0, i = p.gradio), "elem_id" in p && t(1, s = p.elem_id), "elem_classes" in p && t(2, a = p.elem_classes), "visible" in p && t(3, r = p.visible), "value" in p && t(21, f = p.value), "label" in p && t(4, o = p.label), "info" in p && t(5, u = p.info), "container" in p && t(6, _ = p.container), "scale" in p && t(7, m = p.scale), "min_width" in p && t(8, b = p.min_width), "minimum" in p && t(9, y = p.minimum), "maximum" in p && t(10, V = p.maximum), "step" in p && t(11, k = p.step), "show_label" in p && t(12, I = p.show_label), "interactive" in p && t(13, c = p.interactive), "loading_status" in p && t(14, d = p.loading_status), "value_is_output" in p && t(22, S = p.value_is_output);
  }, l.$$.update = () => {
    l.$$.dirty & /*old_value, value*/
    10485760 && JSON.stringify(B) !== JSON.stringify(f) && (t(15, [q, Z] = f, q, (t(16, Z), t(23, B), t(21, f))), t(23, B = f)), l.$$.dirty & /*selected_min, selected_max*/
    98304 && z(q, Z), l.$$.dirty & /*selected_min, minimum, maximum, selected_max*/
    99840 && t(17, n = `
      left: ${(q - y) / (V - y) * 100}%;
      width: ${(Z - q) / (V - y) * 100}%;
    `);
  }, [
    i,
    s,
    a,
    r,
    o,
    u,
    _,
    m,
    b,
    y,
    V,
    k,
    I,
    c,
    d,
    q,
    Z,
    n,
    h,
    P,
    N,
    f,
    S,
    B,
    Y,
    le,
    D,
    g,
    v
  ];
}
class ri extends Un {
  constructor(e) {
    super(), ei(this, e, ai, oi, li, {
      gradio: 0,
      elem_id: 1,
      elem_classes: 2,
      visible: 3,
      value: 21,
      label: 4,
      info: 5,
      container: 6,
      scale: 7,
      min_width: 8,
      minimum: 9,
      maximum: 10,
      step: 11,
      show_label: 12,
      interactive: 13,
      loading_status: 14,
      value_is_output: 22
    });
  }
}
export {
  ri as default
};
