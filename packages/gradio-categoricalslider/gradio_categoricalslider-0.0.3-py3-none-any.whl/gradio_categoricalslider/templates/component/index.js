const {
  SvelteComponent: Qt,
  assign: Wt,
  create_slot: xt,
  detach: $t,
  element: el,
  get_all_dirty_from_scope: tl,
  get_slot_changes: ll,
  get_spread_update: nl,
  init: il,
  insert: fl,
  safe_not_equal: sl,
  set_dynamic_element_data: Je,
  set_style: j,
  toggle_class: O,
  transition_in: Ft,
  transition_out: St,
  update_slot_base: ol
} = window.__gradio__svelte__internal;
function al(l) {
  let e, t, n;
  const i = (
    /*#slots*/
    l[18].default
  ), f = xt(
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
  ], r = {};
  for (let s = 0; s < o.length; s += 1)
    r = Wt(r, o[s]);
  return {
    c() {
      e = el(
        /*tag*/
        l[14]
      ), f && f.c(), Je(
        /*tag*/
        l[14]
      )(e, r), O(
        e,
        "hidden",
        /*visible*/
        l[10] === !1
      ), O(
        e,
        "padded",
        /*padding*/
        l[6]
      ), O(
        e,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), O(
        e,
        "border_contrast",
        /*border_mode*/
        l[5] === "contrast"
      ), O(e, "hide-container", !/*explicit_call*/
      l[8] && !/*container*/
      l[9]), j(
        e,
        "height",
        /*get_dimension*/
        l[15](
          /*height*/
          l[0]
        )
      ), j(e, "width", typeof /*width*/
      l[1] == "number" ? `calc(min(${/*width*/
      l[1]}px, 100%))` : (
        /*get_dimension*/
        l[15](
          /*width*/
          l[1]
        )
      )), j(
        e,
        "border-style",
        /*variant*/
        l[4]
      ), j(
        e,
        "overflow",
        /*allow_overflow*/
        l[11] ? "visible" : "hidden"
      ), j(
        e,
        "flex-grow",
        /*scale*/
        l[12]
      ), j(e, "min-width", `calc(min(${/*min_width*/
      l[13]}px, 100%))`), j(e, "border-width", "var(--block-border-width)");
    },
    m(s, a) {
      fl(s, e, a), f && f.m(e, null), n = !0;
    },
    p(s, a) {
      f && f.p && (!n || a & /*$$scope*/
      131072) && ol(
        f,
        i,
        s,
        /*$$scope*/
        s[17],
        n ? ll(
          i,
          /*$$scope*/
          s[17],
          a,
          null
        ) : tl(
          /*$$scope*/
          s[17]
        ),
        null
      ), Je(
        /*tag*/
        s[14]
      )(e, r = nl(o, [
        (!n || a & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          s[7]
        ) },
        (!n || a & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          s[2]
        ) },
        (!n || a & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        s[3].join(" ") + " svelte-nl1om8")) && { class: t }
      ])), O(
        e,
        "hidden",
        /*visible*/
        s[10] === !1
      ), O(
        e,
        "padded",
        /*padding*/
        s[6]
      ), O(
        e,
        "border_focus",
        /*border_mode*/
        s[5] === "focus"
      ), O(
        e,
        "border_contrast",
        /*border_mode*/
        s[5] === "contrast"
      ), O(e, "hide-container", !/*explicit_call*/
      s[8] && !/*container*/
      s[9]), a & /*height*/
      1 && j(
        e,
        "height",
        /*get_dimension*/
        s[15](
          /*height*/
          s[0]
        )
      ), a & /*width*/
      2 && j(e, "width", typeof /*width*/
      s[1] == "number" ? `calc(min(${/*width*/
      s[1]}px, 100%))` : (
        /*get_dimension*/
        s[15](
          /*width*/
          s[1]
        )
      )), a & /*variant*/
      16 && j(
        e,
        "border-style",
        /*variant*/
        s[4]
      ), a & /*allow_overflow*/
      2048 && j(
        e,
        "overflow",
        /*allow_overflow*/
        s[11] ? "visible" : "hidden"
      ), a & /*scale*/
      4096 && j(
        e,
        "flex-grow",
        /*scale*/
        s[12]
      ), a & /*min_width*/
      8192 && j(e, "min-width", `calc(min(${/*min_width*/
      s[13]}px, 100%))`);
    },
    i(s) {
      n || (Ft(f, s), n = !0);
    },
    o(s) {
      St(f, s), n = !1;
    },
    d(s) {
      s && $t(e), f && f.d(s);
    }
  };
}
function rl(l) {
  let e, t = (
    /*tag*/
    l[14] && al(l)
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
      e || (Ft(t, n), e = !0);
    },
    o(n) {
      St(t, n), e = !1;
    },
    d(n) {
      t && t.d(n);
    }
  };
}
function _l(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { height: f = void 0 } = e, { width: o = void 0 } = e, { elem_id: r = "" } = e, { elem_classes: s = [] } = e, { variant: a = "solid" } = e, { border_mode: _ = "base" } = e, { padding: c = !0 } = e, { type: w = "normal" } = e, { test_id: b = void 0 } = e, { explicit_call: y = !1 } = e, { container: S = !0 } = e, { visible: q = !0 } = e, { allow_overflow: z = !0 } = e, { scale: d = null } = e, { min_width: u = 0 } = e, m = w === "fieldset" ? "fieldset" : "div";
  const C = (g) => {
    if (g !== void 0) {
      if (typeof g == "number")
        return g + "px";
      if (typeof g == "string")
        return g;
    }
  };
  return l.$$set = (g) => {
    "height" in g && t(0, f = g.height), "width" in g && t(1, o = g.width), "elem_id" in g && t(2, r = g.elem_id), "elem_classes" in g && t(3, s = g.elem_classes), "variant" in g && t(4, a = g.variant), "border_mode" in g && t(5, _ = g.border_mode), "padding" in g && t(6, c = g.padding), "type" in g && t(16, w = g.type), "test_id" in g && t(7, b = g.test_id), "explicit_call" in g && t(8, y = g.explicit_call), "container" in g && t(9, S = g.container), "visible" in g && t(10, q = g.visible), "allow_overflow" in g && t(11, z = g.allow_overflow), "scale" in g && t(12, d = g.scale), "min_width" in g && t(13, u = g.min_width), "$$scope" in g && t(17, i = g.$$scope);
  }, [
    f,
    o,
    r,
    s,
    a,
    _,
    c,
    b,
    y,
    S,
    q,
    z,
    d,
    u,
    m,
    C,
    w,
    i,
    n
  ];
}
class ul extends Qt {
  constructor(e) {
    super(), il(this, e, _l, rl, sl, {
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
  SvelteComponent: cl,
  attr: dl,
  create_slot: ml,
  detach: bl,
  element: gl,
  get_all_dirty_from_scope: hl,
  get_slot_changes: wl,
  init: pl,
  insert: kl,
  safe_not_equal: vl,
  transition_in: yl,
  transition_out: ql,
  update_slot_base: Cl
} = window.__gradio__svelte__internal;
function Fl(l) {
  let e, t;
  const n = (
    /*#slots*/
    l[1].default
  ), i = ml(
    n,
    l,
    /*$$scope*/
    l[0],
    null
  );
  return {
    c() {
      e = gl("div"), i && i.c(), dl(e, "class", "svelte-1hnfib2");
    },
    m(f, o) {
      kl(f, e, o), i && i.m(e, null), t = !0;
    },
    p(f, [o]) {
      i && i.p && (!t || o & /*$$scope*/
      1) && Cl(
        i,
        n,
        f,
        /*$$scope*/
        f[0],
        t ? wl(
          n,
          /*$$scope*/
          f[0],
          o,
          null
        ) : hl(
          /*$$scope*/
          f[0]
        ),
        null
      );
    },
    i(f) {
      t || (yl(i, f), t = !0);
    },
    o(f) {
      ql(i, f), t = !1;
    },
    d(f) {
      f && bl(e), i && i.d(f);
    }
  };
}
function Sl(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e;
  return l.$$set = (f) => {
    "$$scope" in f && t(0, i = f.$$scope);
  }, [i, n];
}
class zl extends cl {
  constructor(e) {
    super(), pl(this, e, Sl, Fl, vl, {});
  }
}
const {
  SvelteComponent: Ll,
  attr: Ke,
  check_outros: Ml,
  create_component: Vl,
  create_slot: Il,
  destroy_component: Nl,
  detach: ve,
  element: Zl,
  empty: jl,
  get_all_dirty_from_scope: Pl,
  get_slot_changes: Bl,
  group_outros: Al,
  init: Dl,
  insert: ye,
  mount_component: El,
  safe_not_equal: Tl,
  set_data: Xl,
  space: Yl,
  text: Gl,
  toggle_class: ie,
  transition_in: ce,
  transition_out: qe,
  update_slot_base: Ol
} = window.__gradio__svelte__internal;
function Qe(l) {
  let e, t;
  return e = new zl({
    props: {
      $$slots: { default: [Rl] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      Vl(e.$$.fragment);
    },
    m(n, i) {
      El(e, n, i), t = !0;
    },
    p(n, i) {
      const f = {};
      i & /*$$scope, info*/
      10 && (f.$$scope = { dirty: i, ctx: n }), e.$set(f);
    },
    i(n) {
      t || (ce(e.$$.fragment, n), t = !0);
    },
    o(n) {
      qe(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Nl(e, n);
    }
  };
}
function Rl(l) {
  let e;
  return {
    c() {
      e = Gl(
        /*info*/
        l[1]
      );
    },
    m(t, n) {
      ye(t, e, n);
    },
    p(t, n) {
      n & /*info*/
      2 && Xl(
        e,
        /*info*/
        t[1]
      );
    },
    d(t) {
      t && ve(e);
    }
  };
}
function Ul(l) {
  let e, t, n, i;
  const f = (
    /*#slots*/
    l[2].default
  ), o = Il(
    f,
    l,
    /*$$scope*/
    l[3],
    null
  );
  let r = (
    /*info*/
    l[1] && Qe(l)
  );
  return {
    c() {
      e = Zl("span"), o && o.c(), t = Yl(), r && r.c(), n = jl(), Ke(e, "data-testid", "block-info"), Ke(e, "class", "svelte-22c38v"), ie(e, "sr-only", !/*show_label*/
      l[0]), ie(e, "hide", !/*show_label*/
      l[0]), ie(
        e,
        "has-info",
        /*info*/
        l[1] != null
      );
    },
    m(s, a) {
      ye(s, e, a), o && o.m(e, null), ye(s, t, a), r && r.m(s, a), ye(s, n, a), i = !0;
    },
    p(s, [a]) {
      o && o.p && (!i || a & /*$$scope*/
      8) && Ol(
        o,
        f,
        s,
        /*$$scope*/
        s[3],
        i ? Bl(
          f,
          /*$$scope*/
          s[3],
          a,
          null
        ) : Pl(
          /*$$scope*/
          s[3]
        ),
        null
      ), (!i || a & /*show_label*/
      1) && ie(e, "sr-only", !/*show_label*/
      s[0]), (!i || a & /*show_label*/
      1) && ie(e, "hide", !/*show_label*/
      s[0]), (!i || a & /*info*/
      2) && ie(
        e,
        "has-info",
        /*info*/
        s[1] != null
      ), /*info*/
      s[1] ? r ? (r.p(s, a), a & /*info*/
      2 && ce(r, 1)) : (r = Qe(s), r.c(), ce(r, 1), r.m(n.parentNode, n)) : r && (Al(), qe(r, 1, 1, () => {
        r = null;
      }), Ml());
    },
    i(s) {
      i || (ce(o, s), ce(r), i = !0);
    },
    o(s) {
      qe(o, s), qe(r), i = !1;
    },
    d(s) {
      s && (ve(e), ve(t), ve(n)), o && o.d(s), r && r.d(s);
    }
  };
}
function Hl(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { show_label: f = !0 } = e, { info: o = void 0 } = e;
  return l.$$set = (r) => {
    "show_label" in r && t(0, f = r.show_label), "info" in r && t(1, o = r.info), "$$scope" in r && t(3, i = r.$$scope);
  }, [f, o, n, i];
}
class Jl extends Ll {
  constructor(e) {
    super(), Dl(this, e, Hl, Ul, Tl, { show_label: 0, info: 1 });
  }
}
const {
  SvelteComponent: Kl,
  append: je,
  attr: K,
  bubble: Ql,
  create_component: Wl,
  destroy_component: xl,
  detach: zt,
  element: Pe,
  init: $l,
  insert: Lt,
  listen: en,
  mount_component: tn,
  safe_not_equal: ln,
  set_data: nn,
  set_style: fe,
  space: fn,
  text: sn,
  toggle_class: N,
  transition_in: on,
  transition_out: an
} = window.__gradio__svelte__internal;
function We(l) {
  let e, t;
  return {
    c() {
      e = Pe("span"), t = sn(
        /*label*/
        l[1]
      ), K(e, "class", "svelte-1lrphxw");
    },
    m(n, i) {
      Lt(n, e, i), je(e, t);
    },
    p(n, i) {
      i & /*label*/
      2 && nn(
        t,
        /*label*/
        n[1]
      );
    },
    d(n) {
      n && zt(e);
    }
  };
}
function rn(l) {
  let e, t, n, i, f, o, r, s = (
    /*show_label*/
    l[2] && We(l)
  );
  return i = new /*Icon*/
  l[0]({}), {
    c() {
      e = Pe("button"), s && s.c(), t = fn(), n = Pe("div"), Wl(i.$$.fragment), K(n, "class", "svelte-1lrphxw"), N(
        n,
        "small",
        /*size*/
        l[4] === "small"
      ), N(
        n,
        "large",
        /*size*/
        l[4] === "large"
      ), N(
        n,
        "medium",
        /*size*/
        l[4] === "medium"
      ), e.disabled = /*disabled*/
      l[7], K(
        e,
        "aria-label",
        /*label*/
        l[1]
      ), K(
        e,
        "aria-haspopup",
        /*hasPopup*/
        l[8]
      ), K(
        e,
        "title",
        /*label*/
        l[1]
      ), K(e, "class", "svelte-1lrphxw"), N(
        e,
        "pending",
        /*pending*/
        l[3]
      ), N(
        e,
        "padded",
        /*padded*/
        l[5]
      ), N(
        e,
        "highlight",
        /*highlight*/
        l[6]
      ), N(
        e,
        "transparent",
        /*transparent*/
        l[9]
      ), fe(e, "color", !/*disabled*/
      l[7] && /*_color*/
      l[12] ? (
        /*_color*/
        l[12]
      ) : "var(--block-label-text-color)"), fe(e, "--bg-color", /*disabled*/
      l[7] ? "auto" : (
        /*background*/
        l[10]
      )), fe(
        e,
        "margin-left",
        /*offset*/
        l[11] + "px"
      );
    },
    m(a, _) {
      Lt(a, e, _), s && s.m(e, null), je(e, t), je(e, n), tn(i, n, null), f = !0, o || (r = en(
        e,
        "click",
        /*click_handler*/
        l[14]
      ), o = !0);
    },
    p(a, [_]) {
      /*show_label*/
      a[2] ? s ? s.p(a, _) : (s = We(a), s.c(), s.m(e, t)) : s && (s.d(1), s = null), (!f || _ & /*size*/
      16) && N(
        n,
        "small",
        /*size*/
        a[4] === "small"
      ), (!f || _ & /*size*/
      16) && N(
        n,
        "large",
        /*size*/
        a[4] === "large"
      ), (!f || _ & /*size*/
      16) && N(
        n,
        "medium",
        /*size*/
        a[4] === "medium"
      ), (!f || _ & /*disabled*/
      128) && (e.disabled = /*disabled*/
      a[7]), (!f || _ & /*label*/
      2) && K(
        e,
        "aria-label",
        /*label*/
        a[1]
      ), (!f || _ & /*hasPopup*/
      256) && K(
        e,
        "aria-haspopup",
        /*hasPopup*/
        a[8]
      ), (!f || _ & /*label*/
      2) && K(
        e,
        "title",
        /*label*/
        a[1]
      ), (!f || _ & /*pending*/
      8) && N(
        e,
        "pending",
        /*pending*/
        a[3]
      ), (!f || _ & /*padded*/
      32) && N(
        e,
        "padded",
        /*padded*/
        a[5]
      ), (!f || _ & /*highlight*/
      64) && N(
        e,
        "highlight",
        /*highlight*/
        a[6]
      ), (!f || _ & /*transparent*/
      512) && N(
        e,
        "transparent",
        /*transparent*/
        a[9]
      ), _ & /*disabled, _color*/
      4224 && fe(e, "color", !/*disabled*/
      a[7] && /*_color*/
      a[12] ? (
        /*_color*/
        a[12]
      ) : "var(--block-label-text-color)"), _ & /*disabled, background*/
      1152 && fe(e, "--bg-color", /*disabled*/
      a[7] ? "auto" : (
        /*background*/
        a[10]
      )), _ & /*offset*/
      2048 && fe(
        e,
        "margin-left",
        /*offset*/
        a[11] + "px"
      );
    },
    i(a) {
      f || (on(i.$$.fragment, a), f = !0);
    },
    o(a) {
      an(i.$$.fragment, a), f = !1;
    },
    d(a) {
      a && zt(e), s && s.d(), xl(i), o = !1, r();
    }
  };
}
function _n(l, e, t) {
  let n, { Icon: i } = e, { label: f = "" } = e, { show_label: o = !1 } = e, { pending: r = !1 } = e, { size: s = "small" } = e, { padded: a = !0 } = e, { highlight: _ = !1 } = e, { disabled: c = !1 } = e, { hasPopup: w = !1 } = e, { color: b = "var(--block-label-text-color)" } = e, { transparent: y = !1 } = e, { background: S = "var(--background-fill-primary)" } = e, { offset: q = 0 } = e;
  function z(d) {
    Ql.call(this, l, d);
  }
  return l.$$set = (d) => {
    "Icon" in d && t(0, i = d.Icon), "label" in d && t(1, f = d.label), "show_label" in d && t(2, o = d.show_label), "pending" in d && t(3, r = d.pending), "size" in d && t(4, s = d.size), "padded" in d && t(5, a = d.padded), "highlight" in d && t(6, _ = d.highlight), "disabled" in d && t(7, c = d.disabled), "hasPopup" in d && t(8, w = d.hasPopup), "color" in d && t(13, b = d.color), "transparent" in d && t(9, y = d.transparent), "background" in d && t(10, S = d.background), "offset" in d && t(11, q = d.offset);
  }, l.$$.update = () => {
    l.$$.dirty & /*highlight, color*/
    8256 && t(12, n = _ ? "var(--color-accent)" : b);
  }, [
    i,
    f,
    o,
    r,
    s,
    a,
    _,
    c,
    w,
    y,
    S,
    q,
    n,
    b,
    z
  ];
}
class un extends Kl {
  constructor(e) {
    super(), $l(this, e, _n, rn, ln, {
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
  SvelteComponent: cn,
  append: Ve,
  attr: D,
  detach: dn,
  init: mn,
  insert: bn,
  noop: Ie,
  safe_not_equal: gn,
  set_style: R,
  svg_element: he
} = window.__gradio__svelte__internal;
function hn(l) {
  let e, t, n, i;
  return {
    c() {
      e = he("svg"), t = he("g"), n = he("path"), i = he("path"), D(n, "d", "M18,6L6.087,17.913"), R(n, "fill", "none"), R(n, "fill-rule", "nonzero"), R(n, "stroke-width", "2px"), D(t, "transform", "matrix(1.14096,-0.140958,-0.140958,1.14096,-0.0559523,0.0559523)"), D(i, "d", "M4.364,4.364L19.636,19.636"), R(i, "fill", "none"), R(i, "fill-rule", "nonzero"), R(i, "stroke-width", "2px"), D(e, "width", "100%"), D(e, "height", "100%"), D(e, "viewBox", "0 0 24 24"), D(e, "version", "1.1"), D(e, "xmlns", "http://www.w3.org/2000/svg"), D(e, "xmlns:xlink", "http://www.w3.org/1999/xlink"), D(e, "xml:space", "preserve"), D(e, "stroke", "currentColor"), R(e, "fill-rule", "evenodd"), R(e, "clip-rule", "evenodd"), R(e, "stroke-linecap", "round"), R(e, "stroke-linejoin", "round");
    },
    m(f, o) {
      bn(f, e, o), Ve(e, t), Ve(t, n), Ve(e, i);
    },
    p: Ie,
    i: Ie,
    o: Ie,
    d(f) {
      f && dn(e);
    }
  };
}
class wn extends cn {
  constructor(e) {
    super(), mn(this, e, null, hn, gn, {});
  }
}
const pn = [
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
], xe = {
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
pn.reduce(
  (l, { color: e, primary: t, secondary: n }) => ({
    ...l,
    [e]: {
      primary: xe[e][t],
      secondary: xe[e][n]
    }
  }),
  {}
);
function ae(l) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; l > 1e3 && t < e.length - 1; )
    l /= 1e3, t++;
  let n = e[t];
  return (Number.isInteger(l) ? l : l.toFixed(1)) + n;
}
function Ce() {
}
function kn(l, e) {
  return l != l ? e == e : l !== e || l && typeof l == "object" || typeof l == "function";
}
const Mt = typeof window < "u";
let $e = Mt ? () => window.performance.now() : () => Date.now(), Vt = Mt ? (l) => requestAnimationFrame(l) : Ce;
const re = /* @__PURE__ */ new Set();
function It(l) {
  re.forEach((e) => {
    e.c(l) || (re.delete(e), e.f());
  }), re.size !== 0 && Vt(It);
}
function vn(l) {
  let e;
  return re.size === 0 && Vt(It), {
    promise: new Promise((t) => {
      re.add(e = { c: l, f: t });
    }),
    abort() {
      re.delete(e);
    }
  };
}
const se = [];
function yn(l, e = Ce) {
  let t;
  const n = /* @__PURE__ */ new Set();
  function i(r) {
    if (kn(l, r) && (l = r, t)) {
      const s = !se.length;
      for (const a of n)
        a[1](), se.push(a, l);
      if (s) {
        for (let a = 0; a < se.length; a += 2)
          se[a][0](se[a + 1]);
        se.length = 0;
      }
    }
  }
  function f(r) {
    i(r(l));
  }
  function o(r, s = Ce) {
    const a = [r, s];
    return n.add(a), n.size === 1 && (t = e(i, f) || Ce), r(l), () => {
      n.delete(a), n.size === 0 && t && (t(), t = null);
    };
  }
  return { set: i, update: f, subscribe: o };
}
function et(l) {
  return Object.prototype.toString.call(l) === "[object Date]";
}
function Be(l, e, t, n) {
  if (typeof t == "number" || et(t)) {
    const i = n - t, f = (t - e) / (l.dt || 1 / 60), o = l.opts.stiffness * i, r = l.opts.damping * f, s = (o - r) * l.inv_mass, a = (f + s) * l.dt;
    return Math.abs(a) < l.opts.precision && Math.abs(i) < l.opts.precision ? n : (l.settled = !1, et(t) ? new Date(t.getTime() + a) : t + a);
  } else {
    if (Array.isArray(t))
      return t.map(
        (i, f) => Be(l, e[f], t[f], n[f])
      );
    if (typeof t == "object") {
      const i = {};
      for (const f in t)
        i[f] = Be(l, e[f], t[f], n[f]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function tt(l, e = {}) {
  const t = yn(l), { stiffness: n = 0.15, damping: i = 0.8, precision: f = 0.01 } = e;
  let o, r, s, a = l, _ = l, c = 1, w = 0, b = !1;
  function y(q, z = {}) {
    _ = q;
    const d = s = {};
    return l == null || z.hard || S.stiffness >= 1 && S.damping >= 1 ? (b = !0, o = $e(), a = q, t.set(l = _), Promise.resolve()) : (z.soft && (w = 1 / ((z.soft === !0 ? 0.5 : +z.soft) * 60), c = 0), r || (o = $e(), b = !1, r = vn((u) => {
      if (b)
        return b = !1, r = null, !1;
      c = Math.min(c + w, 1);
      const m = {
        inv_mass: c,
        opts: S,
        settled: !0,
        dt: (u - o) * 60 / 1e3
      }, C = Be(m, a, l, _);
      return o = u, a = l, t.set(l = C), m.settled && (r = null), !m.settled;
    })), new Promise((u) => {
      r.promise.then(() => {
        d === s && u();
      });
    }));
  }
  const S = {
    set: y,
    update: (q, z) => y(q(_, l), z),
    subscribe: t.subscribe,
    stiffness: n,
    damping: i,
    precision: f
  };
  return S;
}
const {
  SvelteComponent: qn,
  append: E,
  attr: F,
  component_subscribe: lt,
  detach: Cn,
  element: Fn,
  init: Sn,
  insert: zn,
  noop: nt,
  safe_not_equal: Ln,
  set_style: we,
  svg_element: T,
  toggle_class: it
} = window.__gradio__svelte__internal, { onMount: Mn } = window.__gradio__svelte__internal;
function Vn(l) {
  let e, t, n, i, f, o, r, s, a, _, c, w;
  return {
    c() {
      e = Fn("div"), t = T("svg"), n = T("g"), i = T("path"), f = T("path"), o = T("path"), r = T("path"), s = T("g"), a = T("path"), _ = T("path"), c = T("path"), w = T("path"), F(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), F(i, "fill", "#FF7C00"), F(i, "fill-opacity", "0.4"), F(i, "class", "svelte-43sxxs"), F(f, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), F(f, "fill", "#FF7C00"), F(f, "class", "svelte-43sxxs"), F(o, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), F(o, "fill", "#FF7C00"), F(o, "fill-opacity", "0.4"), F(o, "class", "svelte-43sxxs"), F(r, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), F(r, "fill", "#FF7C00"), F(r, "class", "svelte-43sxxs"), we(n, "transform", "translate(" + /*$top*/
      l[1][0] + "px, " + /*$top*/
      l[1][1] + "px)"), F(a, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), F(a, "fill", "#FF7C00"), F(a, "fill-opacity", "0.4"), F(a, "class", "svelte-43sxxs"), F(_, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), F(_, "fill", "#FF7C00"), F(_, "class", "svelte-43sxxs"), F(c, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), F(c, "fill", "#FF7C00"), F(c, "fill-opacity", "0.4"), F(c, "class", "svelte-43sxxs"), F(w, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), F(w, "fill", "#FF7C00"), F(w, "class", "svelte-43sxxs"), we(s, "transform", "translate(" + /*$bottom*/
      l[2][0] + "px, " + /*$bottom*/
      l[2][1] + "px)"), F(t, "viewBox", "-1200 -1200 3000 3000"), F(t, "fill", "none"), F(t, "xmlns", "http://www.w3.org/2000/svg"), F(t, "class", "svelte-43sxxs"), F(e, "class", "svelte-43sxxs"), it(
        e,
        "margin",
        /*margin*/
        l[0]
      );
    },
    m(b, y) {
      zn(b, e, y), E(e, t), E(t, n), E(n, i), E(n, f), E(n, o), E(n, r), E(t, s), E(s, a), E(s, _), E(s, c), E(s, w);
    },
    p(b, [y]) {
      y & /*$top*/
      2 && we(n, "transform", "translate(" + /*$top*/
      b[1][0] + "px, " + /*$top*/
      b[1][1] + "px)"), y & /*$bottom*/
      4 && we(s, "transform", "translate(" + /*$bottom*/
      b[2][0] + "px, " + /*$bottom*/
      b[2][1] + "px)"), y & /*margin*/
      1 && it(
        e,
        "margin",
        /*margin*/
        b[0]
      );
    },
    i: nt,
    o: nt,
    d(b) {
      b && Cn(e);
    }
  };
}
function In(l, e, t) {
  let n, i;
  var f = this && this.__awaiter || function(b, y, S, q) {
    function z(d) {
      return d instanceof S ? d : new S(function(u) {
        u(d);
      });
    }
    return new (S || (S = Promise))(function(d, u) {
      function m(V) {
        try {
          g(q.next(V));
        } catch (L) {
          u(L);
        }
      }
      function C(V) {
        try {
          g(q.throw(V));
        } catch (L) {
          u(L);
        }
      }
      function g(V) {
        V.done ? d(V.value) : z(V.value).then(m, C);
      }
      g((q = q.apply(b, y || [])).next());
    });
  };
  let { margin: o = !0 } = e;
  const r = tt([0, 0]);
  lt(l, r, (b) => t(1, n = b));
  const s = tt([0, 0]);
  lt(l, s, (b) => t(2, i = b));
  let a;
  function _() {
    return f(this, void 0, void 0, function* () {
      yield Promise.all([r.set([125, 140]), s.set([-125, -140])]), yield Promise.all([r.set([-125, 140]), s.set([125, -140])]), yield Promise.all([r.set([-125, 0]), s.set([125, -0])]), yield Promise.all([r.set([125, 0]), s.set([-125, 0])]);
    });
  }
  function c() {
    return f(this, void 0, void 0, function* () {
      yield _(), a || c();
    });
  }
  function w() {
    return f(this, void 0, void 0, function* () {
      yield Promise.all([r.set([125, 0]), s.set([-125, 0])]), c();
    });
  }
  return Mn(() => (w(), () => a = !0)), l.$$set = (b) => {
    "margin" in b && t(0, o = b.margin);
  }, [o, n, i, r, s];
}
class Nn extends qn {
  constructor(e) {
    super(), Sn(this, e, In, Vn, Ln, { margin: 0 });
  }
}
const {
  SvelteComponent: Zn,
  append: ne,
  attr: Y,
  binding_callbacks: ft,
  check_outros: Ae,
  create_component: Nt,
  create_slot: Zt,
  destroy_component: jt,
  destroy_each: Pt,
  detach: k,
  element: U,
  empty: _e,
  ensure_array_like: Fe,
  get_all_dirty_from_scope: Bt,
  get_slot_changes: At,
  group_outros: De,
  init: jn,
  insert: v,
  mount_component: Dt,
  noop: Ee,
  safe_not_equal: Pn,
  set_data: A,
  set_style: $,
  space: B,
  text: M,
  toggle_class: P,
  transition_in: X,
  transition_out: H,
  update_slot_base: Et
} = window.__gradio__svelte__internal, { tick: Bn } = window.__gradio__svelte__internal, { onDestroy: An } = window.__gradio__svelte__internal, { createEventDispatcher: Dn } = window.__gradio__svelte__internal, En = (l) => ({}), st = (l) => ({}), Tn = (l) => ({}), ot = (l) => ({});
function at(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n[43] = t, n;
}
function rt(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n;
}
function Xn(l) {
  let e, t, n, i, f = (
    /*i18n*/
    l[1]("common.error") + ""
  ), o, r, s;
  t = new un({
    props: {
      Icon: wn,
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
  const a = (
    /*#slots*/
    l[30].error
  ), _ = Zt(
    a,
    l,
    /*$$scope*/
    l[29],
    st
  );
  return {
    c() {
      e = U("div"), Nt(t.$$.fragment), n = B(), i = U("span"), o = M(f), r = B(), _ && _.c(), Y(e, "class", "clear-status svelte-vopvsi"), Y(i, "class", "error svelte-vopvsi");
    },
    m(c, w) {
      v(c, e, w), Dt(t, e, null), v(c, n, w), v(c, i, w), ne(i, o), v(c, r, w), _ && _.m(c, w), s = !0;
    },
    p(c, w) {
      const b = {};
      w[0] & /*i18n*/
      2 && (b.label = /*i18n*/
      c[1]("common.clear")), t.$set(b), (!s || w[0] & /*i18n*/
      2) && f !== (f = /*i18n*/
      c[1]("common.error") + "") && A(o, f), _ && _.p && (!s || w[0] & /*$$scope*/
      536870912) && Et(
        _,
        a,
        c,
        /*$$scope*/
        c[29],
        s ? At(
          a,
          /*$$scope*/
          c[29],
          w,
          En
        ) : Bt(
          /*$$scope*/
          c[29]
        ),
        st
      );
    },
    i(c) {
      s || (X(t.$$.fragment, c), X(_, c), s = !0);
    },
    o(c) {
      H(t.$$.fragment, c), H(_, c), s = !1;
    },
    d(c) {
      c && (k(e), k(n), k(i), k(r)), jt(t), _ && _.d(c);
    }
  };
}
function Yn(l) {
  let e, t, n, i, f, o, r, s, a, _ = (
    /*variant*/
    l[8] === "default" && /*show_eta_bar*/
    l[18] && /*show_progress*/
    l[6] === "full" && _t(l)
  );
  function c(u, m) {
    if (
      /*progress*/
      u[7]
    )
      return Rn;
    if (
      /*queue_position*/
      u[2] !== null && /*queue_size*/
      u[3] !== void 0 && /*queue_position*/
      u[2] >= 0
    )
      return On;
    if (
      /*queue_position*/
      u[2] === 0
    )
      return Gn;
  }
  let w = c(l), b = w && w(l), y = (
    /*timer*/
    l[5] && dt(l)
  );
  const S = [Kn, Jn], q = [];
  function z(u, m) {
    return (
      /*last_progress_level*/
      u[15] != null ? 0 : (
        /*show_progress*/
        u[6] === "full" ? 1 : -1
      )
    );
  }
  ~(f = z(l)) && (o = q[f] = S[f](l));
  let d = !/*timer*/
  l[5] && kt(l);
  return {
    c() {
      _ && _.c(), e = B(), t = U("div"), b && b.c(), n = B(), y && y.c(), i = B(), o && o.c(), r = B(), d && d.c(), s = _e(), Y(t, "class", "progress-text svelte-vopvsi"), P(
        t,
        "meta-text-center",
        /*variant*/
        l[8] === "center"
      ), P(
        t,
        "meta-text",
        /*variant*/
        l[8] === "default"
      );
    },
    m(u, m) {
      _ && _.m(u, m), v(u, e, m), v(u, t, m), b && b.m(t, null), ne(t, n), y && y.m(t, null), v(u, i, m), ~f && q[f].m(u, m), v(u, r, m), d && d.m(u, m), v(u, s, m), a = !0;
    },
    p(u, m) {
      /*variant*/
      u[8] === "default" && /*show_eta_bar*/
      u[18] && /*show_progress*/
      u[6] === "full" ? _ ? _.p(u, m) : (_ = _t(u), _.c(), _.m(e.parentNode, e)) : _ && (_.d(1), _ = null), w === (w = c(u)) && b ? b.p(u, m) : (b && b.d(1), b = w && w(u), b && (b.c(), b.m(t, n))), /*timer*/
      u[5] ? y ? y.p(u, m) : (y = dt(u), y.c(), y.m(t, null)) : y && (y.d(1), y = null), (!a || m[0] & /*variant*/
      256) && P(
        t,
        "meta-text-center",
        /*variant*/
        u[8] === "center"
      ), (!a || m[0] & /*variant*/
      256) && P(
        t,
        "meta-text",
        /*variant*/
        u[8] === "default"
      );
      let C = f;
      f = z(u), f === C ? ~f && q[f].p(u, m) : (o && (De(), H(q[C], 1, 1, () => {
        q[C] = null;
      }), Ae()), ~f ? (o = q[f], o ? o.p(u, m) : (o = q[f] = S[f](u), o.c()), X(o, 1), o.m(r.parentNode, r)) : o = null), /*timer*/
      u[5] ? d && (De(), H(d, 1, 1, () => {
        d = null;
      }), Ae()) : d ? (d.p(u, m), m[0] & /*timer*/
      32 && X(d, 1)) : (d = kt(u), d.c(), X(d, 1), d.m(s.parentNode, s));
    },
    i(u) {
      a || (X(o), X(d), a = !0);
    },
    o(u) {
      H(o), H(d), a = !1;
    },
    d(u) {
      u && (k(e), k(t), k(i), k(r), k(s)), _ && _.d(u), b && b.d(), y && y.d(), ~f && q[f].d(u), d && d.d(u);
    }
  };
}
function _t(l) {
  let e, t = `translateX(${/*eta_level*/
  (l[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = U("div"), Y(e, "class", "eta-bar svelte-vopvsi"), $(e, "transform", t);
    },
    m(n, i) {
      v(n, e, i);
    },
    p(n, i) {
      i[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && $(e, "transform", t);
    },
    d(n) {
      n && k(e);
    }
  };
}
function Gn(l) {
  let e;
  return {
    c() {
      e = M("processing |");
    },
    m(t, n) {
      v(t, e, n);
    },
    p: Ee,
    d(t) {
      t && k(e);
    }
  };
}
function On(l) {
  let e, t = (
    /*queue_position*/
    l[2] + 1 + ""
  ), n, i, f, o;
  return {
    c() {
      e = M("queue: "), n = M(t), i = M("/"), f = M(
        /*queue_size*/
        l[3]
      ), o = M(" |");
    },
    m(r, s) {
      v(r, e, s), v(r, n, s), v(r, i, s), v(r, f, s), v(r, o, s);
    },
    p(r, s) {
      s[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      r[2] + 1 + "") && A(n, t), s[0] & /*queue_size*/
      8 && A(
        f,
        /*queue_size*/
        r[3]
      );
    },
    d(r) {
      r && (k(e), k(n), k(i), k(f), k(o));
    }
  };
}
function Rn(l) {
  let e, t = Fe(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = ct(rt(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = _e();
    },
    m(i, f) {
      for (let o = 0; o < n.length; o += 1)
        n[o] && n[o].m(i, f);
      v(i, e, f);
    },
    p(i, f) {
      if (f[0] & /*progress*/
      128) {
        t = Fe(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const r = rt(i, t, o);
          n[o] ? n[o].p(r, f) : (n[o] = ct(r), n[o].c(), n[o].m(e.parentNode, e));
        }
        for (; o < n.length; o += 1)
          n[o].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && k(e), Pt(n, i);
    }
  };
}
function ut(l) {
  let e, t = (
    /*p*/
    l[41].unit + ""
  ), n, i, f = " ", o;
  function r(_, c) {
    return (
      /*p*/
      _[41].length != null ? Hn : Un
    );
  }
  let s = r(l), a = s(l);
  return {
    c() {
      a.c(), e = B(), n = M(t), i = M(" | "), o = M(f);
    },
    m(_, c) {
      a.m(_, c), v(_, e, c), v(_, n, c), v(_, i, c), v(_, o, c);
    },
    p(_, c) {
      s === (s = r(_)) && a ? a.p(_, c) : (a.d(1), a = s(_), a && (a.c(), a.m(e.parentNode, e))), c[0] & /*progress*/
      128 && t !== (t = /*p*/
      _[41].unit + "") && A(n, t);
    },
    d(_) {
      _ && (k(e), k(n), k(i), k(o)), a.d(_);
    }
  };
}
function Un(l) {
  let e = ae(
    /*p*/
    l[41].index || 0
  ) + "", t;
  return {
    c() {
      t = M(e);
    },
    m(n, i) {
      v(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = ae(
        /*p*/
        n[41].index || 0
      ) + "") && A(t, e);
    },
    d(n) {
      n && k(t);
    }
  };
}
function Hn(l) {
  let e = ae(
    /*p*/
    l[41].index || 0
  ) + "", t, n, i = ae(
    /*p*/
    l[41].length
  ) + "", f;
  return {
    c() {
      t = M(e), n = M("/"), f = M(i);
    },
    m(o, r) {
      v(o, t, r), v(o, n, r), v(o, f, r);
    },
    p(o, r) {
      r[0] & /*progress*/
      128 && e !== (e = ae(
        /*p*/
        o[41].index || 0
      ) + "") && A(t, e), r[0] & /*progress*/
      128 && i !== (i = ae(
        /*p*/
        o[41].length
      ) + "") && A(f, i);
    },
    d(o) {
      o && (k(t), k(n), k(f));
    }
  };
}
function ct(l) {
  let e, t = (
    /*p*/
    l[41].index != null && ut(l)
  );
  return {
    c() {
      t && t.c(), e = _e();
    },
    m(n, i) {
      t && t.m(n, i), v(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[41].index != null ? t ? t.p(n, i) : (t = ut(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && k(e), t && t.d(n);
    }
  };
}
function dt(l) {
  let e, t = (
    /*eta*/
    l[0] ? `/${/*formatted_eta*/
    l[19]}` : ""
  ), n, i;
  return {
    c() {
      e = M(
        /*formatted_timer*/
        l[20]
      ), n = M(t), i = M("s");
    },
    m(f, o) {
      v(f, e, o), v(f, n, o), v(f, i, o);
    },
    p(f, o) {
      o[0] & /*formatted_timer*/
      1048576 && A(
        e,
        /*formatted_timer*/
        f[20]
      ), o[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      f[0] ? `/${/*formatted_eta*/
      f[19]}` : "") && A(n, t);
    },
    d(f) {
      f && (k(e), k(n), k(i));
    }
  };
}
function Jn(l) {
  let e, t;
  return e = new Nn({
    props: { margin: (
      /*variant*/
      l[8] === "default"
    ) }
  }), {
    c() {
      Nt(e.$$.fragment);
    },
    m(n, i) {
      Dt(e, n, i), t = !0;
    },
    p(n, i) {
      const f = {};
      i[0] & /*variant*/
      256 && (f.margin = /*variant*/
      n[8] === "default"), e.$set(f);
    },
    i(n) {
      t || (X(e.$$.fragment, n), t = !0);
    },
    o(n) {
      H(e.$$.fragment, n), t = !1;
    },
    d(n) {
      jt(e, n);
    }
  };
}
function Kn(l) {
  let e, t, n, i, f, o = `${/*last_progress_level*/
  l[15] * 100}%`, r = (
    /*progress*/
    l[7] != null && mt(l)
  );
  return {
    c() {
      e = U("div"), t = U("div"), r && r.c(), n = B(), i = U("div"), f = U("div"), Y(t, "class", "progress-level-inner svelte-vopvsi"), Y(f, "class", "progress-bar svelte-vopvsi"), $(f, "width", o), Y(i, "class", "progress-bar-wrap svelte-vopvsi"), Y(e, "class", "progress-level svelte-vopvsi");
    },
    m(s, a) {
      v(s, e, a), ne(e, t), r && r.m(t, null), ne(e, n), ne(e, i), ne(i, f), l[31](f);
    },
    p(s, a) {
      /*progress*/
      s[7] != null ? r ? r.p(s, a) : (r = mt(s), r.c(), r.m(t, null)) : r && (r.d(1), r = null), a[0] & /*last_progress_level*/
      32768 && o !== (o = `${/*last_progress_level*/
      s[15] * 100}%`) && $(f, "width", o);
    },
    i: Ee,
    o: Ee,
    d(s) {
      s && k(e), r && r.d(), l[31](null);
    }
  };
}
function mt(l) {
  let e, t = Fe(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = pt(at(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = _e();
    },
    m(i, f) {
      for (let o = 0; o < n.length; o += 1)
        n[o] && n[o].m(i, f);
      v(i, e, f);
    },
    p(i, f) {
      if (f[0] & /*progress_level, progress*/
      16512) {
        t = Fe(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const r = at(i, t, o);
          n[o] ? n[o].p(r, f) : (n[o] = pt(r), n[o].c(), n[o].m(e.parentNode, e));
        }
        for (; o < n.length; o += 1)
          n[o].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && k(e), Pt(n, i);
    }
  };
}
function bt(l) {
  let e, t, n, i, f = (
    /*i*/
    l[43] !== 0 && Qn()
  ), o = (
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
  ), s = (
    /*progress_level*/
    l[14] != null && wt(l)
  );
  return {
    c() {
      f && f.c(), e = B(), o && o.c(), t = B(), r && r.c(), n = B(), s && s.c(), i = _e();
    },
    m(a, _) {
      f && f.m(a, _), v(a, e, _), o && o.m(a, _), v(a, t, _), r && r.m(a, _), v(a, n, _), s && s.m(a, _), v(a, i, _);
    },
    p(a, _) {
      /*p*/
      a[41].desc != null ? o ? o.p(a, _) : (o = gt(a), o.c(), o.m(t.parentNode, t)) : o && (o.d(1), o = null), /*p*/
      a[41].desc != null && /*progress_level*/
      a[14] && /*progress_level*/
      a[14][
        /*i*/
        a[43]
      ] != null ? r || (r = ht(), r.c(), r.m(n.parentNode, n)) : r && (r.d(1), r = null), /*progress_level*/
      a[14] != null ? s ? s.p(a, _) : (s = wt(a), s.c(), s.m(i.parentNode, i)) : s && (s.d(1), s = null);
    },
    d(a) {
      a && (k(e), k(t), k(n), k(i)), f && f.d(a), o && o.d(a), r && r.d(a), s && s.d(a);
    }
  };
}
function Qn(l) {
  let e;
  return {
    c() {
      e = M(" /");
    },
    m(t, n) {
      v(t, e, n);
    },
    d(t) {
      t && k(e);
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
      t = M(e);
    },
    m(n, i) {
      v(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = /*p*/
      n[41].desc + "") && A(t, e);
    },
    d(n) {
      n && k(t);
    }
  };
}
function ht(l) {
  let e;
  return {
    c() {
      e = M("-");
    },
    m(t, n) {
      v(t, e, n);
    },
    d(t) {
      t && k(e);
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
      t = M(e), n = M("%");
    },
    m(i, f) {
      v(i, t, f), v(i, n, f);
    },
    p(i, f) {
      f[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[43]
      ] || 0)).toFixed(1) + "") && A(t, e);
    },
    d(i) {
      i && (k(t), k(n));
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
      t && t.c(), e = _e();
    },
    m(n, i) {
      t && t.m(n, i), v(n, e, i);
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
      n && k(e), t && t.d(n);
    }
  };
}
function kt(l) {
  let e, t, n, i;
  const f = (
    /*#slots*/
    l[30]["additional-loading-text"]
  ), o = Zt(
    f,
    l,
    /*$$scope*/
    l[29],
    ot
  );
  return {
    c() {
      e = U("p"), t = M(
        /*loading_text*/
        l[9]
      ), n = B(), o && o.c(), Y(e, "class", "loading svelte-vopvsi");
    },
    m(r, s) {
      v(r, e, s), ne(e, t), v(r, n, s), o && o.m(r, s), i = !0;
    },
    p(r, s) {
      (!i || s[0] & /*loading_text*/
      512) && A(
        t,
        /*loading_text*/
        r[9]
      ), o && o.p && (!i || s[0] & /*$$scope*/
      536870912) && Et(
        o,
        f,
        r,
        /*$$scope*/
        r[29],
        i ? At(
          f,
          /*$$scope*/
          r[29],
          s,
          Tn
        ) : Bt(
          /*$$scope*/
          r[29]
        ),
        ot
      );
    },
    i(r) {
      i || (X(o, r), i = !0);
    },
    o(r) {
      H(o, r), i = !1;
    },
    d(r) {
      r && (k(e), k(n)), o && o.d(r);
    }
  };
}
function Wn(l) {
  let e, t, n, i, f;
  const o = [Yn, Xn], r = [];
  function s(a, _) {
    return (
      /*status*/
      a[4] === "pending" ? 0 : (
        /*status*/
        a[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = s(l)) && (n = r[t] = o[t](l)), {
    c() {
      e = U("div"), n && n.c(), Y(e, "class", i = "wrap " + /*variant*/
      l[8] + " " + /*show_progress*/
      l[6] + " svelte-vopvsi"), P(e, "hide", !/*status*/
      l[4] || /*status*/
      l[4] === "complete" || /*show_progress*/
      l[6] === "hidden"), P(
        e,
        "translucent",
        /*variant*/
        l[8] === "center" && /*status*/
        (l[4] === "pending" || /*status*/
        l[4] === "error") || /*translucent*/
        l[11] || /*show_progress*/
        l[6] === "minimal"
      ), P(
        e,
        "generating",
        /*status*/
        l[4] === "generating"
      ), P(
        e,
        "border",
        /*border*/
        l[12]
      ), $(
        e,
        "position",
        /*absolute*/
        l[10] ? "absolute" : "static"
      ), $(
        e,
        "padding",
        /*absolute*/
        l[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(a, _) {
      v(a, e, _), ~t && r[t].m(e, null), l[33](e), f = !0;
    },
    p(a, _) {
      let c = t;
      t = s(a), t === c ? ~t && r[t].p(a, _) : (n && (De(), H(r[c], 1, 1, () => {
        r[c] = null;
      }), Ae()), ~t ? (n = r[t], n ? n.p(a, _) : (n = r[t] = o[t](a), n.c()), X(n, 1), n.m(e, null)) : n = null), (!f || _[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      a[8] + " " + /*show_progress*/
      a[6] + " svelte-vopvsi")) && Y(e, "class", i), (!f || _[0] & /*variant, show_progress, status, show_progress*/
      336) && P(e, "hide", !/*status*/
      a[4] || /*status*/
      a[4] === "complete" || /*show_progress*/
      a[6] === "hidden"), (!f || _[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && P(
        e,
        "translucent",
        /*variant*/
        a[8] === "center" && /*status*/
        (a[4] === "pending" || /*status*/
        a[4] === "error") || /*translucent*/
        a[11] || /*show_progress*/
        a[6] === "minimal"
      ), (!f || _[0] & /*variant, show_progress, status*/
      336) && P(
        e,
        "generating",
        /*status*/
        a[4] === "generating"
      ), (!f || _[0] & /*variant, show_progress, border*/
      4416) && P(
        e,
        "border",
        /*border*/
        a[12]
      ), _[0] & /*absolute*/
      1024 && $(
        e,
        "position",
        /*absolute*/
        a[10] ? "absolute" : "static"
      ), _[0] & /*absolute*/
      1024 && $(
        e,
        "padding",
        /*absolute*/
        a[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(a) {
      f || (X(n), f = !0);
    },
    o(a) {
      H(n), f = !1;
    },
    d(a) {
      a && k(e), ~t && r[t].d(), l[33](null);
    }
  };
}
var xn = function(l, e, t, n) {
  function i(f) {
    return f instanceof t ? f : new t(function(o) {
      o(f);
    });
  }
  return new (t || (t = Promise))(function(f, o) {
    function r(_) {
      try {
        a(n.next(_));
      } catch (c) {
        o(c);
      }
    }
    function s(_) {
      try {
        a(n.throw(_));
      } catch (c) {
        o(c);
      }
    }
    function a(_) {
      _.done ? f(_.value) : i(_.value).then(r, s);
    }
    a((n = n.apply(l, e || [])).next());
  });
};
let pe = [], Ne = !1;
function $n(l) {
  return xn(this, arguments, void 0, function* (e, t = !0) {
    if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
      if (pe.push(e), !Ne)
        Ne = !0;
      else
        return;
      yield Bn(), requestAnimationFrame(() => {
        let n = [0, 0];
        for (let i = 0; i < pe.length; i++) {
          const o = pe[i].getBoundingClientRect();
          (i === 0 || o.top + window.scrollY <= n[0]) && (n[0] = o.top + window.scrollY, n[1] = i);
        }
        window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), Ne = !1, pe = [];
      });
    }
  });
}
function ei(l, e, t) {
  let n, { $$slots: i = {}, $$scope: f } = e;
  this && this.__awaiter;
  const o = Dn();
  let { i18n: r } = e, { eta: s = null } = e, { queue_position: a } = e, { queue_size: _ } = e, { status: c } = e, { scroll_to_output: w = !1 } = e, { timer: b = !0 } = e, { show_progress: y = "full" } = e, { message: S = null } = e, { progress: q = null } = e, { variant: z = "default" } = e, { loading_text: d = "Loading..." } = e, { absolute: u = !0 } = e, { translucent: m = !1 } = e, { border: C = !1 } = e, { autoscroll: g } = e, V, L = !1, G = 0, J = 0, Q = null, W = null, p = 0, I = null, ee, x = null, Re = !0;
  const Yt = () => {
    t(0, s = t(27, Q = t(19, de = null))), t(25, G = performance.now()), t(26, J = 0), L = !0, Ue();
  };
  function Ue() {
    requestAnimationFrame(() => {
      t(26, J = (performance.now() - G) / 1e3), L && Ue();
    });
  }
  function He() {
    t(26, J = 0), t(0, s = t(27, Q = t(19, de = null))), L && (L = !1);
  }
  An(() => {
    L && He();
  });
  let de = null;
  function Gt(h) {
    ft[h ? "unshift" : "push"](() => {
      x = h, t(16, x), t(7, q), t(14, I), t(15, ee);
    });
  }
  const Ot = () => {
    o("clear_status");
  };
  function Rt(h) {
    ft[h ? "unshift" : "push"](() => {
      V = h, t(13, V);
    });
  }
  return l.$$set = (h) => {
    "i18n" in h && t(1, r = h.i18n), "eta" in h && t(0, s = h.eta), "queue_position" in h && t(2, a = h.queue_position), "queue_size" in h && t(3, _ = h.queue_size), "status" in h && t(4, c = h.status), "scroll_to_output" in h && t(22, w = h.scroll_to_output), "timer" in h && t(5, b = h.timer), "show_progress" in h && t(6, y = h.show_progress), "message" in h && t(23, S = h.message), "progress" in h && t(7, q = h.progress), "variant" in h && t(8, z = h.variant), "loading_text" in h && t(9, d = h.loading_text), "absolute" in h && t(10, u = h.absolute), "translucent" in h && t(11, m = h.translucent), "border" in h && t(12, C = h.border), "autoscroll" in h && t(24, g = h.autoscroll), "$$scope" in h && t(29, f = h.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    436207617 && (s === null && t(0, s = Q), s != null && Q !== s && (t(28, W = (performance.now() - G) / 1e3 + s), t(19, de = W.toFixed(1)), t(27, Q = s))), l.$$.dirty[0] & /*eta_from_start, timer_diff*/
    335544320 && t(17, p = W === null || W <= 0 || !J ? null : Math.min(J / W, 1)), l.$$.dirty[0] & /*progress*/
    128 && q != null && t(18, Re = !1), l.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (q != null ? t(14, I = q.map((h) => {
      if (h.index != null && h.length != null)
        return h.index / h.length;
      if (h.progress != null)
        return h.progress;
    })) : t(14, I = null), I ? (t(15, ee = I[I.length - 1]), x && (ee === 0 ? t(16, x.style.transition = "0", x) : t(16, x.style.transition = "150ms", x))) : t(15, ee = void 0)), l.$$.dirty[0] & /*status*/
    16 && (c === "pending" ? Yt() : He()), l.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && V && w && (c === "pending" || c === "complete") && $n(V, g), l.$$.dirty[0] & /*status, message*/
    8388624, l.$$.dirty[0] & /*timer_diff*/
    67108864 && t(20, n = J.toFixed(1));
  }, [
    s,
    r,
    a,
    _,
    c,
    b,
    y,
    q,
    z,
    d,
    u,
    m,
    C,
    V,
    I,
    ee,
    x,
    p,
    Re,
    de,
    n,
    o,
    w,
    S,
    g,
    G,
    J,
    Q,
    W,
    f,
    i,
    Gt,
    Ot,
    Rt
  ];
}
class ti extends Zn {
  constructor(e) {
    super(), jn(
      this,
      e,
      ei,
      Wn,
      Pn,
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
  SvelteComponent: li,
  append: le,
  assign: ni,
  attr: Z,
  binding_callbacks: ii,
  create_component: Te,
  destroy_component: Xe,
  destroy_each: fi,
  detach: Se,
  element: oe,
  ensure_array_like: vt,
  get_spread_object: si,
  get_spread_update: oi,
  init: ai,
  insert: ze,
  listen: ke,
  mount_component: Ye,
  run_all: ri,
  safe_not_equal: _i,
  set_data: Tt,
  set_input_value: yt,
  space: Ze,
  text: Xt,
  to_number: ui,
  transition_in: Ge,
  transition_out: Oe
} = window.__gradio__svelte__internal, { afterUpdate: ci } = window.__gradio__svelte__internal;
function qt(l, e, t) {
  const n = l.slice();
  return n[12] = e[t][0], n[26] = e[t][1], n;
}
function di(l) {
  let e;
  return {
    c() {
      e = Xt(
        /*label*/
        l[12]
      );
    },
    m(t, n) {
      ze(t, e, n);
    },
    p(t, n) {
      n & /*label*/
      4096 && Tt(
        e,
        /*label*/
        t[12]
      );
    },
    d(t) {
      t && Se(e);
    }
  };
}
function Ct(l) {
  let e, t = (
    /*label*/
    l[12] + ""
  ), n;
  return {
    c() {
      e = oe("span"), n = Xt(t);
    },
    m(i, f) {
      ze(i, e, f), le(e, n);
    },
    p(i, f) {
      f & /*categories*/
      2048 && t !== (t = /*label*/
      i[12] + "") && Tt(n, t);
    },
    d(i) {
      i && Se(e);
    }
  };
}
function mi(l) {
  let e, t, n, i, f, o, r, s, a, _, c, w, b, y, S;
  const q = [
    { autoscroll: (
      /*gradio*/
      l[1].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      l[1].i18n
    ) },
    /*loading_status*/
    l[10]
  ];
  let z = {};
  for (let m = 0; m < q.length; m += 1)
    z = ni(z, q[m]);
  e = new ti({ props: z }), e.$on(
    "clear_status",
    /*clear_status_handler*/
    l[20]
  ), o = new Jl({
    props: {
      show_label: (
        /*show_label*/
        l[9]
      ),
      info: (
        /*info*/
        l[5]
      ),
      $$slots: { default: [di] },
      $$scope: { ctx: l }
    }
  });
  let d = vt(
    /*categories*/
    l[11]
  ), u = [];
  for (let m = 0; m < d.length; m += 1)
    u[m] = Ct(qt(l, d, m));
  return {
    c() {
      Te(e.$$.fragment), t = Ze(), n = oe("div"), i = oe("div"), f = oe("label"), Te(o.$$.fragment), r = Ze(), s = oe("div");
      for (let m = 0; m < u.length; m += 1)
        u[m].c();
      a = Ze(), _ = oe("input"), Z(
        f,
        "for",
        /*id*/
        l[15]
      ), Z(i, "class", "head svelte-rzyrb9"), Z(s, "class", "labels svelte-rzyrb9"), Z(_, "type", "range"), Z(
        _,
        "id",
        /*id*/
        l[15]
      ), Z(_, "name", "cowbell"), Z(_, "min", 0), Z(_, "max", c = /*categories*/
      l[11].length - 1), Z(_, "step", 1), _.disabled = /*disabled*/
      l[14], Z(_, "aria-label", w = `range slider for ${/*label*/
      l[12]}`), Z(_, "class", "slider svelte-rzyrb9"), Z(n, "class", "wrap svelte-rzyrb9");
    },
    m(m, C) {
      Ye(e, m, C), ze(m, t, C), ze(m, n, C), le(n, i), le(i, f), Ye(o, f, null), le(n, r), le(n, s);
      for (let g = 0; g < u.length; g += 1)
        u[g] && u[g].m(s, null);
      le(n, a), le(n, _), yt(
        _,
        /*value*/
        l[0]
      ), l[22](_), b = !0, y || (S = [
        ke(
          _,
          "change",
          /*input_change_input_handler*/
          l[21]
        ),
        ke(
          _,
          "input",
          /*input_change_input_handler*/
          l[21]
        ),
        ke(
          _,
          "input",
          /*handle_input*/
          l[17]
        ),
        ke(
          _,
          "pointerup",
          /*handle_release*/
          l[16]
        )
      ], y = !0);
    },
    p(m, C) {
      const g = C & /*gradio, loading_status*/
      1026 ? oi(q, [
        C & /*gradio*/
        2 && { autoscroll: (
          /*gradio*/
          m[1].autoscroll
        ) },
        C & /*gradio*/
        2 && { i18n: (
          /*gradio*/
          m[1].i18n
        ) },
        C & /*loading_status*/
        1024 && si(
          /*loading_status*/
          m[10]
        )
      ]) : {};
      e.$set(g);
      const V = {};
      if (C & /*show_label*/
      512 && (V.show_label = /*show_label*/
      m[9]), C & /*info*/
      32 && (V.info = /*info*/
      m[5]), C & /*$$scope, label*/
      536875008 && (V.$$scope = { dirty: C, ctx: m }), o.$set(V), C & /*categories*/
      2048) {
        d = vt(
          /*categories*/
          m[11]
        );
        let L;
        for (L = 0; L < d.length; L += 1) {
          const G = qt(m, d, L);
          u[L] ? u[L].p(G, C) : (u[L] = Ct(G), u[L].c(), u[L].m(s, null));
        }
        for (; L < u.length; L += 1)
          u[L].d(1);
        u.length = d.length;
      }
      (!b || C & /*categories*/
      2048 && c !== (c = /*categories*/
      m[11].length - 1)) && Z(_, "max", c), (!b || C & /*disabled*/
      16384) && (_.disabled = /*disabled*/
      m[14]), (!b || C & /*label*/
      4096 && w !== (w = `range slider for ${/*label*/
      m[12]}`)) && Z(_, "aria-label", w), C & /*value*/
      1 && yt(
        _,
        /*value*/
        m[0]
      );
    },
    i(m) {
      b || (Ge(e.$$.fragment, m), Ge(o.$$.fragment, m), b = !0);
    },
    o(m) {
      Oe(e.$$.fragment, m), Oe(o.$$.fragment, m), b = !1;
    },
    d(m) {
      m && (Se(t), Se(n)), Xe(e, m), Xe(o), fi(u, m), l[22](null), y = !1, ri(S);
    }
  };
}
function bi(l) {
  let e, t;
  return e = new ul({
    props: {
      visible: (
        /*visible*/
        l[4]
      ),
      elem_id: (
        /*elem_id*/
        l[2]
      ),
      elem_classes: (
        /*elem_classes*/
        l[3]
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
      $$slots: { default: [mi] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      Te(e.$$.fragment);
    },
    m(n, i) {
      Ye(e, n, i), t = !0;
    },
    p(n, [i]) {
      const f = {};
      i & /*visible*/
      16 && (f.visible = /*visible*/
      n[4]), i & /*elem_id*/
      4 && (f.elem_id = /*elem_id*/
      n[2]), i & /*elem_classes*/
      8 && (f.elem_classes = /*elem_classes*/
      n[3]), i & /*container*/
      64 && (f.container = /*container*/
      n[6]), i & /*scale*/
      128 && (f.scale = /*scale*/
      n[7]), i & /*min_width*/
      256 && (f.min_width = /*min_width*/
      n[8]), i & /*$$scope, categories, disabled, label, value, rangeInput, show_label, info, gradio, loading_status*/
      536903203 && (f.$$scope = { dirty: i, ctx: n }), e.$set(f);
    },
    i(n) {
      t || (Ge(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Oe(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Xe(e, n);
    }
  };
}
let gi = 0;
function hi(l, e, t) {
  let n, { gradio: i } = e, { elem_id: f = "" } = e, { elem_classes: o = [] } = e, { visible: r = !0 } = e, { value: s = 0 } = e, { label: a = i.i18n("slider.slider") } = e, { info: _ = void 0 } = e, { container: c = !0 } = e, { scale: w = null } = e, { min_width: b = void 0 } = e, { show_label: y } = e, { interactive: S } = e, { loading_status: q } = e, { value_is_output: z = !1 } = e, { categories: d = [] } = e, u;
  const m = `range_id_${gi++}`;
  function C() {
    i.dispatch("change"), z || i.dispatch("input");
  }
  ci(() => {
    t(18, z = !1), V();
  });
  function g(p) {
    const I = parseInt(u.value), ee = d[I];
    t(0, s = ee[1]), i.dispatch("release", s);
  }
  function V() {
    u && (t(13, u.max = (d.length - 1).toString(), u), G(), u.addEventListener("input", L));
  }
  function L() {
    const p = parseInt(u.value), I = d[p];
    t(0, s = I[1]), G();
  }
  function G() {
    if (u) {
      const p = d.findIndex((I) => I[1] === s);
      if (p !== -1) {
        t(13, u.value = p.toString(), u);
        const I = p / (d.length - 1) * 100;
        t(13, u.style.backgroundSize = I + "% 100%", u);
      }
    }
  }
  const J = () => i.dispatch("clear_status", q);
  function Q() {
    s = ui(this.value), t(0, s);
  }
  function W(p) {
    ii[p ? "unshift" : "push"](() => {
      u = p, t(13, u);
    });
  }
  return l.$$set = (p) => {
    "gradio" in p && t(1, i = p.gradio), "elem_id" in p && t(2, f = p.elem_id), "elem_classes" in p && t(3, o = p.elem_classes), "visible" in p && t(4, r = p.visible), "value" in p && t(0, s = p.value), "label" in p && t(12, a = p.label), "info" in p && t(5, _ = p.info), "container" in p && t(6, c = p.container), "scale" in p && t(7, w = p.scale), "min_width" in p && t(8, b = p.min_width), "show_label" in p && t(9, y = p.show_label), "interactive" in p && t(19, S = p.interactive), "loading_status" in p && t(10, q = p.loading_status), "value_is_output" in p && t(18, z = p.value_is_output), "categories" in p && t(11, d = p.categories);
  }, l.$$.update = () => {
    l.$$.dirty & /*interactive*/
    524288 && t(14, n = !S), l.$$.dirty & /*value, categories*/
    2049 && s !== void 0 && d.findIndex((I) => I[1] === s) !== -1 && C();
  }, [
    s,
    i,
    f,
    o,
    r,
    _,
    c,
    w,
    b,
    y,
    q,
    d,
    a,
    u,
    n,
    m,
    g,
    L,
    z,
    S,
    J,
    Q,
    W
  ];
}
class wi extends li {
  constructor(e) {
    super(), ai(this, e, hi, bi, _i, {
      gradio: 1,
      elem_id: 2,
      elem_classes: 3,
      visible: 4,
      value: 0,
      label: 12,
      info: 5,
      container: 6,
      scale: 7,
      min_width: 8,
      show_label: 9,
      interactive: 19,
      loading_status: 10,
      value_is_output: 18,
      categories: 11
    });
  }
}
export {
  wi as default
};
