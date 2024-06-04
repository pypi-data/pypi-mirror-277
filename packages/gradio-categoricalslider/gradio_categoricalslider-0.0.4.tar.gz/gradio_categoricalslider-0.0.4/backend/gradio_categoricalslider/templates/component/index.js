const {
  SvelteComponent: Kt,
  assign: Qt,
  create_slot: Wt,
  detach: xt,
  element: $t,
  get_all_dirty_from_scope: el,
  get_slot_changes: tl,
  get_spread_update: ll,
  init: nl,
  insert: il,
  safe_not_equal: fl,
  set_dynamic_element_data: He,
  set_style: Z,
  toggle_class: O,
  transition_in: Ct,
  transition_out: Ft,
  update_slot_base: sl
} = window.__gradio__svelte__internal;
function ol(n) {
  let e, t, l;
  const i = (
    /*#slots*/
    n[18].default
  ), f = Wt(
    i,
    n,
    /*$$scope*/
    n[17],
    null
  );
  let o = [
    { "data-testid": (
      /*test_id*/
      n[7]
    ) },
    { id: (
      /*elem_id*/
      n[2]
    ) },
    {
      class: t = "block " + /*elem_classes*/
      n[3].join(" ") + " svelte-nl1om8"
    }
  ], r = {};
  for (let s = 0; s < o.length; s += 1)
    r = Qt(r, o[s]);
  return {
    c() {
      e = $t(
        /*tag*/
        n[14]
      ), f && f.c(), He(
        /*tag*/
        n[14]
      )(e, r), O(
        e,
        "hidden",
        /*visible*/
        n[10] === !1
      ), O(
        e,
        "padded",
        /*padding*/
        n[6]
      ), O(
        e,
        "border_focus",
        /*border_mode*/
        n[5] === "focus"
      ), O(
        e,
        "border_contrast",
        /*border_mode*/
        n[5] === "contrast"
      ), O(e, "hide-container", !/*explicit_call*/
      n[8] && !/*container*/
      n[9]), Z(
        e,
        "height",
        /*get_dimension*/
        n[15](
          /*height*/
          n[0]
        )
      ), Z(e, "width", typeof /*width*/
      n[1] == "number" ? `calc(min(${/*width*/
      n[1]}px, 100%))` : (
        /*get_dimension*/
        n[15](
          /*width*/
          n[1]
        )
      )), Z(
        e,
        "border-style",
        /*variant*/
        n[4]
      ), Z(
        e,
        "overflow",
        /*allow_overflow*/
        n[11] ? "visible" : "hidden"
      ), Z(
        e,
        "flex-grow",
        /*scale*/
        n[12]
      ), Z(e, "min-width", `calc(min(${/*min_width*/
      n[13]}px, 100%))`), Z(e, "border-width", "var(--block-border-width)");
    },
    m(s, a) {
      il(s, e, a), f && f.m(e, null), l = !0;
    },
    p(s, a) {
      f && f.p && (!l || a & /*$$scope*/
      131072) && sl(
        f,
        i,
        s,
        /*$$scope*/
        s[17],
        l ? tl(
          i,
          /*$$scope*/
          s[17],
          a,
          null
        ) : el(
          /*$$scope*/
          s[17]
        ),
        null
      ), He(
        /*tag*/
        s[14]
      )(e, r = ll(o, [
        (!l || a & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          s[7]
        ) },
        (!l || a & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          s[2]
        ) },
        (!l || a & /*elem_classes*/
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
      1 && Z(
        e,
        "height",
        /*get_dimension*/
        s[15](
          /*height*/
          s[0]
        )
      ), a & /*width*/
      2 && Z(e, "width", typeof /*width*/
      s[1] == "number" ? `calc(min(${/*width*/
      s[1]}px, 100%))` : (
        /*get_dimension*/
        s[15](
          /*width*/
          s[1]
        )
      )), a & /*variant*/
      16 && Z(
        e,
        "border-style",
        /*variant*/
        s[4]
      ), a & /*allow_overflow*/
      2048 && Z(
        e,
        "overflow",
        /*allow_overflow*/
        s[11] ? "visible" : "hidden"
      ), a & /*scale*/
      4096 && Z(
        e,
        "flex-grow",
        /*scale*/
        s[12]
      ), a & /*min_width*/
      8192 && Z(e, "min-width", `calc(min(${/*min_width*/
      s[13]}px, 100%))`);
    },
    i(s) {
      l || (Ct(f, s), l = !0);
    },
    o(s) {
      Ft(f, s), l = !1;
    },
    d(s) {
      s && xt(e), f && f.d(s);
    }
  };
}
function al(n) {
  let e, t = (
    /*tag*/
    n[14] && ol(n)
  );
  return {
    c() {
      t && t.c();
    },
    m(l, i) {
      t && t.m(l, i), e = !0;
    },
    p(l, [i]) {
      /*tag*/
      l[14] && t.p(l, i);
    },
    i(l) {
      e || (Ct(t, l), e = !0);
    },
    o(l) {
      Ft(t, l), e = !1;
    },
    d(l) {
      t && t.d(l);
    }
  };
}
function rl(n, e, t) {
  let { $$slots: l = {}, $$scope: i } = e, { height: f = void 0 } = e, { width: o = void 0 } = e, { elem_id: r = "" } = e, { elem_classes: s = [] } = e, { variant: a = "solid" } = e, { border_mode: _ = "base" } = e, { padding: c = !0 } = e, { type: w = "normal" } = e, { test_id: b = void 0 } = e, { explicit_call: y = !1 } = e, { container: S = !0 } = e, { visible: q = !0 } = e, { allow_overflow: z = !0 } = e, { scale: d = null } = e, { min_width: u = 0 } = e, m = w === "fieldset" ? "fieldset" : "div";
  const F = (g) => {
    if (g !== void 0) {
      if (typeof g == "number")
        return g + "px";
      if (typeof g == "string")
        return g;
    }
  };
  return n.$$set = (g) => {
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
    F,
    w,
    i,
    l
  ];
}
class _l extends Kt {
  constructor(e) {
    super(), nl(this, e, rl, al, fl, {
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
  SvelteComponent: ul,
  attr: cl,
  create_slot: dl,
  detach: ml,
  element: bl,
  get_all_dirty_from_scope: gl,
  get_slot_changes: hl,
  init: wl,
  insert: pl,
  safe_not_equal: kl,
  transition_in: vl,
  transition_out: yl,
  update_slot_base: ql
} = window.__gradio__svelte__internal;
function Cl(n) {
  let e, t;
  const l = (
    /*#slots*/
    n[1].default
  ), i = dl(
    l,
    n,
    /*$$scope*/
    n[0],
    null
  );
  return {
    c() {
      e = bl("div"), i && i.c(), cl(e, "class", "svelte-1hnfib2");
    },
    m(f, o) {
      pl(f, e, o), i && i.m(e, null), t = !0;
    },
    p(f, [o]) {
      i && i.p && (!t || o & /*$$scope*/
      1) && ql(
        i,
        l,
        f,
        /*$$scope*/
        f[0],
        t ? hl(
          l,
          /*$$scope*/
          f[0],
          o,
          null
        ) : gl(
          /*$$scope*/
          f[0]
        ),
        null
      );
    },
    i(f) {
      t || (vl(i, f), t = !0);
    },
    o(f) {
      yl(i, f), t = !1;
    },
    d(f) {
      f && ml(e), i && i.d(f);
    }
  };
}
function Fl(n, e, t) {
  let { $$slots: l = {}, $$scope: i } = e;
  return n.$$set = (f) => {
    "$$scope" in f && t(0, i = f.$$scope);
  }, [i, l];
}
class Sl extends ul {
  constructor(e) {
    super(), wl(this, e, Fl, Cl, kl, {});
  }
}
const {
  SvelteComponent: zl,
  attr: Je,
  check_outros: Ll,
  create_component: Ml,
  create_slot: Vl,
  destroy_component: Il,
  detach: ke,
  element: Nl,
  empty: Zl,
  get_all_dirty_from_scope: jl,
  get_slot_changes: Pl,
  group_outros: Bl,
  init: Al,
  insert: ve,
  mount_component: Dl,
  safe_not_equal: El,
  set_data: Tl,
  space: Xl,
  text: Yl,
  toggle_class: ne,
  transition_in: ce,
  transition_out: ye,
  update_slot_base: Gl
} = window.__gradio__svelte__internal;
function Ke(n) {
  let e, t;
  return e = new Sl({
    props: {
      $$slots: { default: [Ol] },
      $$scope: { ctx: n }
    }
  }), {
    c() {
      Ml(e.$$.fragment);
    },
    m(l, i) {
      Dl(e, l, i), t = !0;
    },
    p(l, i) {
      const f = {};
      i & /*$$scope, info*/
      10 && (f.$$scope = { dirty: i, ctx: l }), e.$set(f);
    },
    i(l) {
      t || (ce(e.$$.fragment, l), t = !0);
    },
    o(l) {
      ye(e.$$.fragment, l), t = !1;
    },
    d(l) {
      Il(e, l);
    }
  };
}
function Ol(n) {
  let e;
  return {
    c() {
      e = Yl(
        /*info*/
        n[1]
      );
    },
    m(t, l) {
      ve(t, e, l);
    },
    p(t, l) {
      l & /*info*/
      2 && Tl(
        e,
        /*info*/
        t[1]
      );
    },
    d(t) {
      t && ke(e);
    }
  };
}
function Rl(n) {
  let e, t, l, i;
  const f = (
    /*#slots*/
    n[2].default
  ), o = Vl(
    f,
    n,
    /*$$scope*/
    n[3],
    null
  );
  let r = (
    /*info*/
    n[1] && Ke(n)
  );
  return {
    c() {
      e = Nl("span"), o && o.c(), t = Xl(), r && r.c(), l = Zl(), Je(e, "data-testid", "block-info"), Je(e, "class", "svelte-22c38v"), ne(e, "sr-only", !/*show_label*/
      n[0]), ne(e, "hide", !/*show_label*/
      n[0]), ne(
        e,
        "has-info",
        /*info*/
        n[1] != null
      );
    },
    m(s, a) {
      ve(s, e, a), o && o.m(e, null), ve(s, t, a), r && r.m(s, a), ve(s, l, a), i = !0;
    },
    p(s, [a]) {
      o && o.p && (!i || a & /*$$scope*/
      8) && Gl(
        o,
        f,
        s,
        /*$$scope*/
        s[3],
        i ? Pl(
          f,
          /*$$scope*/
          s[3],
          a,
          null
        ) : jl(
          /*$$scope*/
          s[3]
        ),
        null
      ), (!i || a & /*show_label*/
      1) && ne(e, "sr-only", !/*show_label*/
      s[0]), (!i || a & /*show_label*/
      1) && ne(e, "hide", !/*show_label*/
      s[0]), (!i || a & /*info*/
      2) && ne(
        e,
        "has-info",
        /*info*/
        s[1] != null
      ), /*info*/
      s[1] ? r ? (r.p(s, a), a & /*info*/
      2 && ce(r, 1)) : (r = Ke(s), r.c(), ce(r, 1), r.m(l.parentNode, l)) : r && (Bl(), ye(r, 1, 1, () => {
        r = null;
      }), Ll());
    },
    i(s) {
      i || (ce(o, s), ce(r), i = !0);
    },
    o(s) {
      ye(o, s), ye(r), i = !1;
    },
    d(s) {
      s && (ke(e), ke(t), ke(l)), o && o.d(s), r && r.d(s);
    }
  };
}
function Ul(n, e, t) {
  let { $$slots: l = {}, $$scope: i } = e, { show_label: f = !0 } = e, { info: o = void 0 } = e;
  return n.$$set = (r) => {
    "show_label" in r && t(0, f = r.show_label), "info" in r && t(1, o = r.info), "$$scope" in r && t(3, i = r.$$scope);
  }, [f, o, l, i];
}
class Hl extends zl {
  constructor(e) {
    super(), Al(this, e, Ul, Rl, El, { show_label: 0, info: 1 });
  }
}
const {
  SvelteComponent: Jl,
  append: Ze,
  attr: Q,
  bubble: Kl,
  create_component: Ql,
  destroy_component: Wl,
  detach: St,
  element: je,
  init: xl,
  insert: zt,
  listen: $l,
  mount_component: en,
  safe_not_equal: tn,
  set_data: ln,
  set_style: ie,
  space: nn,
  text: fn,
  toggle_class: I,
  transition_in: sn,
  transition_out: on
} = window.__gradio__svelte__internal;
function Qe(n) {
  let e, t;
  return {
    c() {
      e = je("span"), t = fn(
        /*label*/
        n[1]
      ), Q(e, "class", "svelte-1lrphxw");
    },
    m(l, i) {
      zt(l, e, i), Ze(e, t);
    },
    p(l, i) {
      i & /*label*/
      2 && ln(
        t,
        /*label*/
        l[1]
      );
    },
    d(l) {
      l && St(e);
    }
  };
}
function an(n) {
  let e, t, l, i, f, o, r, s = (
    /*show_label*/
    n[2] && Qe(n)
  );
  return i = new /*Icon*/
  n[0]({}), {
    c() {
      e = je("button"), s && s.c(), t = nn(), l = je("div"), Ql(i.$$.fragment), Q(l, "class", "svelte-1lrphxw"), I(
        l,
        "small",
        /*size*/
        n[4] === "small"
      ), I(
        l,
        "large",
        /*size*/
        n[4] === "large"
      ), I(
        l,
        "medium",
        /*size*/
        n[4] === "medium"
      ), e.disabled = /*disabled*/
      n[7], Q(
        e,
        "aria-label",
        /*label*/
        n[1]
      ), Q(
        e,
        "aria-haspopup",
        /*hasPopup*/
        n[8]
      ), Q(
        e,
        "title",
        /*label*/
        n[1]
      ), Q(e, "class", "svelte-1lrphxw"), I(
        e,
        "pending",
        /*pending*/
        n[3]
      ), I(
        e,
        "padded",
        /*padded*/
        n[5]
      ), I(
        e,
        "highlight",
        /*highlight*/
        n[6]
      ), I(
        e,
        "transparent",
        /*transparent*/
        n[9]
      ), ie(e, "color", !/*disabled*/
      n[7] && /*_color*/
      n[12] ? (
        /*_color*/
        n[12]
      ) : "var(--block-label-text-color)"), ie(e, "--bg-color", /*disabled*/
      n[7] ? "auto" : (
        /*background*/
        n[10]
      )), ie(
        e,
        "margin-left",
        /*offset*/
        n[11] + "px"
      );
    },
    m(a, _) {
      zt(a, e, _), s && s.m(e, null), Ze(e, t), Ze(e, l), en(i, l, null), f = !0, o || (r = $l(
        e,
        "click",
        /*click_handler*/
        n[14]
      ), o = !0);
    },
    p(a, [_]) {
      /*show_label*/
      a[2] ? s ? s.p(a, _) : (s = Qe(a), s.c(), s.m(e, t)) : s && (s.d(1), s = null), (!f || _ & /*size*/
      16) && I(
        l,
        "small",
        /*size*/
        a[4] === "small"
      ), (!f || _ & /*size*/
      16) && I(
        l,
        "large",
        /*size*/
        a[4] === "large"
      ), (!f || _ & /*size*/
      16) && I(
        l,
        "medium",
        /*size*/
        a[4] === "medium"
      ), (!f || _ & /*disabled*/
      128) && (e.disabled = /*disabled*/
      a[7]), (!f || _ & /*label*/
      2) && Q(
        e,
        "aria-label",
        /*label*/
        a[1]
      ), (!f || _ & /*hasPopup*/
      256) && Q(
        e,
        "aria-haspopup",
        /*hasPopup*/
        a[8]
      ), (!f || _ & /*label*/
      2) && Q(
        e,
        "title",
        /*label*/
        a[1]
      ), (!f || _ & /*pending*/
      8) && I(
        e,
        "pending",
        /*pending*/
        a[3]
      ), (!f || _ & /*padded*/
      32) && I(
        e,
        "padded",
        /*padded*/
        a[5]
      ), (!f || _ & /*highlight*/
      64) && I(
        e,
        "highlight",
        /*highlight*/
        a[6]
      ), (!f || _ & /*transparent*/
      512) && I(
        e,
        "transparent",
        /*transparent*/
        a[9]
      ), _ & /*disabled, _color*/
      4224 && ie(e, "color", !/*disabled*/
      a[7] && /*_color*/
      a[12] ? (
        /*_color*/
        a[12]
      ) : "var(--block-label-text-color)"), _ & /*disabled, background*/
      1152 && ie(e, "--bg-color", /*disabled*/
      a[7] ? "auto" : (
        /*background*/
        a[10]
      )), _ & /*offset*/
      2048 && ie(
        e,
        "margin-left",
        /*offset*/
        a[11] + "px"
      );
    },
    i(a) {
      f || (sn(i.$$.fragment, a), f = !0);
    },
    o(a) {
      on(i.$$.fragment, a), f = !1;
    },
    d(a) {
      a && St(e), s && s.d(), Wl(i), o = !1, r();
    }
  };
}
function rn(n, e, t) {
  let l, { Icon: i } = e, { label: f = "" } = e, { show_label: o = !1 } = e, { pending: r = !1 } = e, { size: s = "small" } = e, { padded: a = !0 } = e, { highlight: _ = !1 } = e, { disabled: c = !1 } = e, { hasPopup: w = !1 } = e, { color: b = "var(--block-label-text-color)" } = e, { transparent: y = !1 } = e, { background: S = "var(--background-fill-primary)" } = e, { offset: q = 0 } = e;
  function z(d) {
    Kl.call(this, n, d);
  }
  return n.$$set = (d) => {
    "Icon" in d && t(0, i = d.Icon), "label" in d && t(1, f = d.label), "show_label" in d && t(2, o = d.show_label), "pending" in d && t(3, r = d.pending), "size" in d && t(4, s = d.size), "padded" in d && t(5, a = d.padded), "highlight" in d && t(6, _ = d.highlight), "disabled" in d && t(7, c = d.disabled), "hasPopup" in d && t(8, w = d.hasPopup), "color" in d && t(13, b = d.color), "transparent" in d && t(9, y = d.transparent), "background" in d && t(10, S = d.background), "offset" in d && t(11, q = d.offset);
  }, n.$$.update = () => {
    n.$$.dirty & /*highlight, color*/
    8256 && t(12, l = _ ? "var(--color-accent)" : b);
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
    l,
    b,
    z
  ];
}
class _n extends Jl {
  constructor(e) {
    super(), xl(this, e, rn, an, tn, {
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
  SvelteComponent: un,
  append: Me,
  attr: A,
  detach: cn,
  init: dn,
  insert: mn,
  noop: Ve,
  safe_not_equal: bn,
  set_style: R,
  svg_element: he
} = window.__gradio__svelte__internal;
function gn(n) {
  let e, t, l, i;
  return {
    c() {
      e = he("svg"), t = he("g"), l = he("path"), i = he("path"), A(l, "d", "M18,6L6.087,17.913"), R(l, "fill", "none"), R(l, "fill-rule", "nonzero"), R(l, "stroke-width", "2px"), A(t, "transform", "matrix(1.14096,-0.140958,-0.140958,1.14096,-0.0559523,0.0559523)"), A(i, "d", "M4.364,4.364L19.636,19.636"), R(i, "fill", "none"), R(i, "fill-rule", "nonzero"), R(i, "stroke-width", "2px"), A(e, "width", "100%"), A(e, "height", "100%"), A(e, "viewBox", "0 0 24 24"), A(e, "version", "1.1"), A(e, "xmlns", "http://www.w3.org/2000/svg"), A(e, "xmlns:xlink", "http://www.w3.org/1999/xlink"), A(e, "xml:space", "preserve"), A(e, "stroke", "currentColor"), R(e, "fill-rule", "evenodd"), R(e, "clip-rule", "evenodd"), R(e, "stroke-linecap", "round"), R(e, "stroke-linejoin", "round");
    },
    m(f, o) {
      mn(f, e, o), Me(e, t), Me(t, l), Me(e, i);
    },
    p: Ve,
    i: Ve,
    o: Ve,
    d(f) {
      f && cn(e);
    }
  };
}
class hn extends un {
  constructor(e) {
    super(), dn(this, e, null, gn, bn, {});
  }
}
const wn = [
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
], We = {
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
wn.reduce(
  (n, { color: e, primary: t, secondary: l }) => ({
    ...n,
    [e]: {
      primary: We[e][t],
      secondary: We[e][l]
    }
  }),
  {}
);
function oe(n) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; n > 1e3 && t < e.length - 1; )
    n /= 1e3, t++;
  let l = e[t];
  return (Number.isInteger(n) ? n : n.toFixed(1)) + l;
}
function qe() {
}
function pn(n, e) {
  return n != n ? e == e : n !== e || n && typeof n == "object" || typeof n == "function";
}
const Lt = typeof window < "u";
let xe = Lt ? () => window.performance.now() : () => Date.now(), Mt = Lt ? (n) => requestAnimationFrame(n) : qe;
const ae = /* @__PURE__ */ new Set();
function Vt(n) {
  ae.forEach((e) => {
    e.c(n) || (ae.delete(e), e.f());
  }), ae.size !== 0 && Mt(Vt);
}
function kn(n) {
  let e;
  return ae.size === 0 && Mt(Vt), {
    promise: new Promise((t) => {
      ae.add(e = { c: n, f: t });
    }),
    abort() {
      ae.delete(e);
    }
  };
}
const fe = [];
function vn(n, e = qe) {
  let t;
  const l = /* @__PURE__ */ new Set();
  function i(r) {
    if (pn(n, r) && (n = r, t)) {
      const s = !fe.length;
      for (const a of l)
        a[1](), fe.push(a, n);
      if (s) {
        for (let a = 0; a < fe.length; a += 2)
          fe[a][0](fe[a + 1]);
        fe.length = 0;
      }
    }
  }
  function f(r) {
    i(r(n));
  }
  function o(r, s = qe) {
    const a = [r, s];
    return l.add(a), l.size === 1 && (t = e(i, f) || qe), r(n), () => {
      l.delete(a), l.size === 0 && t && (t(), t = null);
    };
  }
  return { set: i, update: f, subscribe: o };
}
function $e(n) {
  return Object.prototype.toString.call(n) === "[object Date]";
}
function Pe(n, e, t, l) {
  if (typeof t == "number" || $e(t)) {
    const i = l - t, f = (t - e) / (n.dt || 1 / 60), o = n.opts.stiffness * i, r = n.opts.damping * f, s = (o - r) * n.inv_mass, a = (f + s) * n.dt;
    return Math.abs(a) < n.opts.precision && Math.abs(i) < n.opts.precision ? l : (n.settled = !1, $e(t) ? new Date(t.getTime() + a) : t + a);
  } else {
    if (Array.isArray(t))
      return t.map(
        (i, f) => Pe(n, e[f], t[f], l[f])
      );
    if (typeof t == "object") {
      const i = {};
      for (const f in t)
        i[f] = Pe(n, e[f], t[f], l[f]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function et(n, e = {}) {
  const t = vn(n), { stiffness: l = 0.15, damping: i = 0.8, precision: f = 0.01 } = e;
  let o, r, s, a = n, _ = n, c = 1, w = 0, b = !1;
  function y(q, z = {}) {
    _ = q;
    const d = s = {};
    return n == null || z.hard || S.stiffness >= 1 && S.damping >= 1 ? (b = !0, o = xe(), a = q, t.set(n = _), Promise.resolve()) : (z.soft && (w = 1 / ((z.soft === !0 ? 0.5 : +z.soft) * 60), c = 0), r || (o = xe(), b = !1, r = kn((u) => {
      if (b)
        return b = !1, r = null, !1;
      c = Math.min(c + w, 1);
      const m = {
        inv_mass: c,
        opts: S,
        settled: !0,
        dt: (u - o) * 60 / 1e3
      }, F = Pe(m, a, n, _);
      return o = u, a = n, t.set(n = F), m.settled && (r = null), !m.settled;
    })), new Promise((u) => {
      r.promise.then(() => {
        d === s && u();
      });
    }));
  }
  const S = {
    set: y,
    update: (q, z) => y(q(_, n), z),
    subscribe: t.subscribe,
    stiffness: l,
    damping: i,
    precision: f
  };
  return S;
}
const {
  SvelteComponent: yn,
  append: D,
  attr: C,
  component_subscribe: tt,
  detach: qn,
  element: Cn,
  init: Fn,
  insert: Sn,
  noop: lt,
  safe_not_equal: zn,
  set_style: we,
  svg_element: E,
  toggle_class: nt
} = window.__gradio__svelte__internal, { onMount: Ln } = window.__gradio__svelte__internal;
function Mn(n) {
  let e, t, l, i, f, o, r, s, a, _, c, w;
  return {
    c() {
      e = Cn("div"), t = E("svg"), l = E("g"), i = E("path"), f = E("path"), o = E("path"), r = E("path"), s = E("g"), a = E("path"), _ = E("path"), c = E("path"), w = E("path"), C(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), C(i, "fill", "#FF7C00"), C(i, "fill-opacity", "0.4"), C(i, "class", "svelte-43sxxs"), C(f, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), C(f, "fill", "#FF7C00"), C(f, "class", "svelte-43sxxs"), C(o, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), C(o, "fill", "#FF7C00"), C(o, "fill-opacity", "0.4"), C(o, "class", "svelte-43sxxs"), C(r, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), C(r, "fill", "#FF7C00"), C(r, "class", "svelte-43sxxs"), we(l, "transform", "translate(" + /*$top*/
      n[1][0] + "px, " + /*$top*/
      n[1][1] + "px)"), C(a, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), C(a, "fill", "#FF7C00"), C(a, "fill-opacity", "0.4"), C(a, "class", "svelte-43sxxs"), C(_, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), C(_, "fill", "#FF7C00"), C(_, "class", "svelte-43sxxs"), C(c, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), C(c, "fill", "#FF7C00"), C(c, "fill-opacity", "0.4"), C(c, "class", "svelte-43sxxs"), C(w, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), C(w, "fill", "#FF7C00"), C(w, "class", "svelte-43sxxs"), we(s, "transform", "translate(" + /*$bottom*/
      n[2][0] + "px, " + /*$bottom*/
      n[2][1] + "px)"), C(t, "viewBox", "-1200 -1200 3000 3000"), C(t, "fill", "none"), C(t, "xmlns", "http://www.w3.org/2000/svg"), C(t, "class", "svelte-43sxxs"), C(e, "class", "svelte-43sxxs"), nt(
        e,
        "margin",
        /*margin*/
        n[0]
      );
    },
    m(b, y) {
      Sn(b, e, y), D(e, t), D(t, l), D(l, i), D(l, f), D(l, o), D(l, r), D(t, s), D(s, a), D(s, _), D(s, c), D(s, w);
    },
    p(b, [y]) {
      y & /*$top*/
      2 && we(l, "transform", "translate(" + /*$top*/
      b[1][0] + "px, " + /*$top*/
      b[1][1] + "px)"), y & /*$bottom*/
      4 && we(s, "transform", "translate(" + /*$bottom*/
      b[2][0] + "px, " + /*$bottom*/
      b[2][1] + "px)"), y & /*margin*/
      1 && nt(
        e,
        "margin",
        /*margin*/
        b[0]
      );
    },
    i: lt,
    o: lt,
    d(b) {
      b && qn(e);
    }
  };
}
function Vn(n, e, t) {
  let l, i;
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
      function F(V) {
        try {
          g(q.throw(V));
        } catch (L) {
          u(L);
        }
      }
      function g(V) {
        V.done ? d(V.value) : z(V.value).then(m, F);
      }
      g((q = q.apply(b, y || [])).next());
    });
  };
  let { margin: o = !0 } = e;
  const r = et([0, 0]);
  tt(n, r, (b) => t(1, l = b));
  const s = et([0, 0]);
  tt(n, s, (b) => t(2, i = b));
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
  return Ln(() => (w(), () => a = !0)), n.$$set = (b) => {
    "margin" in b && t(0, o = b.margin);
  }, [o, l, i, r, s];
}
class In extends yn {
  constructor(e) {
    super(), Fn(this, e, Vn, Mn, zn, { margin: 0 });
  }
}
const {
  SvelteComponent: Nn,
  append: le,
  attr: X,
  binding_callbacks: it,
  check_outros: Be,
  create_component: It,
  create_slot: Nt,
  destroy_component: Zt,
  destroy_each: jt,
  detach: k,
  element: U,
  empty: re,
  ensure_array_like: Ce,
  get_all_dirty_from_scope: Pt,
  get_slot_changes: Bt,
  group_outros: Ae,
  init: Zn,
  insert: v,
  mount_component: At,
  noop: De,
  safe_not_equal: jn,
  set_data: B,
  set_style: $,
  space: P,
  text: M,
  toggle_class: j,
  transition_in: T,
  transition_out: H,
  update_slot_base: Dt
} = window.__gradio__svelte__internal, { tick: Pn } = window.__gradio__svelte__internal, { onDestroy: Bn } = window.__gradio__svelte__internal, { createEventDispatcher: An } = window.__gradio__svelte__internal, Dn = (n) => ({}), ft = (n) => ({}), En = (n) => ({}), st = (n) => ({});
function ot(n, e, t) {
  const l = n.slice();
  return l[41] = e[t], l[43] = t, l;
}
function at(n, e, t) {
  const l = n.slice();
  return l[41] = e[t], l;
}
function Tn(n) {
  let e, t, l, i, f = (
    /*i18n*/
    n[1]("common.error") + ""
  ), o, r, s;
  t = new _n({
    props: {
      Icon: hn,
      label: (
        /*i18n*/
        n[1]("common.clear")
      ),
      disabled: !1
    }
  }), t.$on(
    "click",
    /*click_handler*/
    n[32]
  );
  const a = (
    /*#slots*/
    n[30].error
  ), _ = Nt(
    a,
    n,
    /*$$scope*/
    n[29],
    ft
  );
  return {
    c() {
      e = U("div"), It(t.$$.fragment), l = P(), i = U("span"), o = M(f), r = P(), _ && _.c(), X(e, "class", "clear-status svelte-vopvsi"), X(i, "class", "error svelte-vopvsi");
    },
    m(c, w) {
      v(c, e, w), At(t, e, null), v(c, l, w), v(c, i, w), le(i, o), v(c, r, w), _ && _.m(c, w), s = !0;
    },
    p(c, w) {
      const b = {};
      w[0] & /*i18n*/
      2 && (b.label = /*i18n*/
      c[1]("common.clear")), t.$set(b), (!s || w[0] & /*i18n*/
      2) && f !== (f = /*i18n*/
      c[1]("common.error") + "") && B(o, f), _ && _.p && (!s || w[0] & /*$$scope*/
      536870912) && Dt(
        _,
        a,
        c,
        /*$$scope*/
        c[29],
        s ? Bt(
          a,
          /*$$scope*/
          c[29],
          w,
          Dn
        ) : Pt(
          /*$$scope*/
          c[29]
        ),
        ft
      );
    },
    i(c) {
      s || (T(t.$$.fragment, c), T(_, c), s = !0);
    },
    o(c) {
      H(t.$$.fragment, c), H(_, c), s = !1;
    },
    d(c) {
      c && (k(e), k(l), k(i), k(r)), Zt(t), _ && _.d(c);
    }
  };
}
function Xn(n) {
  let e, t, l, i, f, o, r, s, a, _ = (
    /*variant*/
    n[8] === "default" && /*show_eta_bar*/
    n[18] && /*show_progress*/
    n[6] === "full" && rt(n)
  );
  function c(u, m) {
    if (
      /*progress*/
      u[7]
    )
      return On;
    if (
      /*queue_position*/
      u[2] !== null && /*queue_size*/
      u[3] !== void 0 && /*queue_position*/
      u[2] >= 0
    )
      return Gn;
    if (
      /*queue_position*/
      u[2] === 0
    )
      return Yn;
  }
  let w = c(n), b = w && w(n), y = (
    /*timer*/
    n[5] && ct(n)
  );
  const S = [Jn, Hn], q = [];
  function z(u, m) {
    return (
      /*last_progress_level*/
      u[15] != null ? 0 : (
        /*show_progress*/
        u[6] === "full" ? 1 : -1
      )
    );
  }
  ~(f = z(n)) && (o = q[f] = S[f](n));
  let d = !/*timer*/
  n[5] && pt(n);
  return {
    c() {
      _ && _.c(), e = P(), t = U("div"), b && b.c(), l = P(), y && y.c(), i = P(), o && o.c(), r = P(), d && d.c(), s = re(), X(t, "class", "progress-text svelte-vopvsi"), j(
        t,
        "meta-text-center",
        /*variant*/
        n[8] === "center"
      ), j(
        t,
        "meta-text",
        /*variant*/
        n[8] === "default"
      );
    },
    m(u, m) {
      _ && _.m(u, m), v(u, e, m), v(u, t, m), b && b.m(t, null), le(t, l), y && y.m(t, null), v(u, i, m), ~f && q[f].m(u, m), v(u, r, m), d && d.m(u, m), v(u, s, m), a = !0;
    },
    p(u, m) {
      /*variant*/
      u[8] === "default" && /*show_eta_bar*/
      u[18] && /*show_progress*/
      u[6] === "full" ? _ ? _.p(u, m) : (_ = rt(u), _.c(), _.m(e.parentNode, e)) : _ && (_.d(1), _ = null), w === (w = c(u)) && b ? b.p(u, m) : (b && b.d(1), b = w && w(u), b && (b.c(), b.m(t, l))), /*timer*/
      u[5] ? y ? y.p(u, m) : (y = ct(u), y.c(), y.m(t, null)) : y && (y.d(1), y = null), (!a || m[0] & /*variant*/
      256) && j(
        t,
        "meta-text-center",
        /*variant*/
        u[8] === "center"
      ), (!a || m[0] & /*variant*/
      256) && j(
        t,
        "meta-text",
        /*variant*/
        u[8] === "default"
      );
      let F = f;
      f = z(u), f === F ? ~f && q[f].p(u, m) : (o && (Ae(), H(q[F], 1, 1, () => {
        q[F] = null;
      }), Be()), ~f ? (o = q[f], o ? o.p(u, m) : (o = q[f] = S[f](u), o.c()), T(o, 1), o.m(r.parentNode, r)) : o = null), /*timer*/
      u[5] ? d && (Ae(), H(d, 1, 1, () => {
        d = null;
      }), Be()) : d ? (d.p(u, m), m[0] & /*timer*/
      32 && T(d, 1)) : (d = pt(u), d.c(), T(d, 1), d.m(s.parentNode, s));
    },
    i(u) {
      a || (T(o), T(d), a = !0);
    },
    o(u) {
      H(o), H(d), a = !1;
    },
    d(u) {
      u && (k(e), k(t), k(i), k(r), k(s)), _ && _.d(u), b && b.d(), y && y.d(), ~f && q[f].d(u), d && d.d(u);
    }
  };
}
function rt(n) {
  let e, t = `translateX(${/*eta_level*/
  (n[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = U("div"), X(e, "class", "eta-bar svelte-vopvsi"), $(e, "transform", t);
    },
    m(l, i) {
      v(l, e, i);
    },
    p(l, i) {
      i[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (l[17] || 0) * 100 - 100}%)`) && $(e, "transform", t);
    },
    d(l) {
      l && k(e);
    }
  };
}
function Yn(n) {
  let e;
  return {
    c() {
      e = M("processing |");
    },
    m(t, l) {
      v(t, e, l);
    },
    p: De,
    d(t) {
      t && k(e);
    }
  };
}
function Gn(n) {
  let e, t = (
    /*queue_position*/
    n[2] + 1 + ""
  ), l, i, f, o;
  return {
    c() {
      e = M("queue: "), l = M(t), i = M("/"), f = M(
        /*queue_size*/
        n[3]
      ), o = M(" |");
    },
    m(r, s) {
      v(r, e, s), v(r, l, s), v(r, i, s), v(r, f, s), v(r, o, s);
    },
    p(r, s) {
      s[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      r[2] + 1 + "") && B(l, t), s[0] & /*queue_size*/
      8 && B(
        f,
        /*queue_size*/
        r[3]
      );
    },
    d(r) {
      r && (k(e), k(l), k(i), k(f), k(o));
    }
  };
}
function On(n) {
  let e, t = Ce(
    /*progress*/
    n[7]
  ), l = [];
  for (let i = 0; i < t.length; i += 1)
    l[i] = ut(at(n, t, i));
  return {
    c() {
      for (let i = 0; i < l.length; i += 1)
        l[i].c();
      e = re();
    },
    m(i, f) {
      for (let o = 0; o < l.length; o += 1)
        l[o] && l[o].m(i, f);
      v(i, e, f);
    },
    p(i, f) {
      if (f[0] & /*progress*/
      128) {
        t = Ce(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const r = at(i, t, o);
          l[o] ? l[o].p(r, f) : (l[o] = ut(r), l[o].c(), l[o].m(e.parentNode, e));
        }
        for (; o < l.length; o += 1)
          l[o].d(1);
        l.length = t.length;
      }
    },
    d(i) {
      i && k(e), jt(l, i);
    }
  };
}
function _t(n) {
  let e, t = (
    /*p*/
    n[41].unit + ""
  ), l, i, f = " ", o;
  function r(_, c) {
    return (
      /*p*/
      _[41].length != null ? Un : Rn
    );
  }
  let s = r(n), a = s(n);
  return {
    c() {
      a.c(), e = P(), l = M(t), i = M(" | "), o = M(f);
    },
    m(_, c) {
      a.m(_, c), v(_, e, c), v(_, l, c), v(_, i, c), v(_, o, c);
    },
    p(_, c) {
      s === (s = r(_)) && a ? a.p(_, c) : (a.d(1), a = s(_), a && (a.c(), a.m(e.parentNode, e))), c[0] & /*progress*/
      128 && t !== (t = /*p*/
      _[41].unit + "") && B(l, t);
    },
    d(_) {
      _ && (k(e), k(l), k(i), k(o)), a.d(_);
    }
  };
}
function Rn(n) {
  let e = oe(
    /*p*/
    n[41].index || 0
  ) + "", t;
  return {
    c() {
      t = M(e);
    },
    m(l, i) {
      v(l, t, i);
    },
    p(l, i) {
      i[0] & /*progress*/
      128 && e !== (e = oe(
        /*p*/
        l[41].index || 0
      ) + "") && B(t, e);
    },
    d(l) {
      l && k(t);
    }
  };
}
function Un(n) {
  let e = oe(
    /*p*/
    n[41].index || 0
  ) + "", t, l, i = oe(
    /*p*/
    n[41].length
  ) + "", f;
  return {
    c() {
      t = M(e), l = M("/"), f = M(i);
    },
    m(o, r) {
      v(o, t, r), v(o, l, r), v(o, f, r);
    },
    p(o, r) {
      r[0] & /*progress*/
      128 && e !== (e = oe(
        /*p*/
        o[41].index || 0
      ) + "") && B(t, e), r[0] & /*progress*/
      128 && i !== (i = oe(
        /*p*/
        o[41].length
      ) + "") && B(f, i);
    },
    d(o) {
      o && (k(t), k(l), k(f));
    }
  };
}
function ut(n) {
  let e, t = (
    /*p*/
    n[41].index != null && _t(n)
  );
  return {
    c() {
      t && t.c(), e = re();
    },
    m(l, i) {
      t && t.m(l, i), v(l, e, i);
    },
    p(l, i) {
      /*p*/
      l[41].index != null ? t ? t.p(l, i) : (t = _t(l), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(l) {
      l && k(e), t && t.d(l);
    }
  };
}
function ct(n) {
  let e, t = (
    /*eta*/
    n[0] ? `/${/*formatted_eta*/
    n[19]}` : ""
  ), l, i;
  return {
    c() {
      e = M(
        /*formatted_timer*/
        n[20]
      ), l = M(t), i = M("s");
    },
    m(f, o) {
      v(f, e, o), v(f, l, o), v(f, i, o);
    },
    p(f, o) {
      o[0] & /*formatted_timer*/
      1048576 && B(
        e,
        /*formatted_timer*/
        f[20]
      ), o[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      f[0] ? `/${/*formatted_eta*/
      f[19]}` : "") && B(l, t);
    },
    d(f) {
      f && (k(e), k(l), k(i));
    }
  };
}
function Hn(n) {
  let e, t;
  return e = new In({
    props: { margin: (
      /*variant*/
      n[8] === "default"
    ) }
  }), {
    c() {
      It(e.$$.fragment);
    },
    m(l, i) {
      At(e, l, i), t = !0;
    },
    p(l, i) {
      const f = {};
      i[0] & /*variant*/
      256 && (f.margin = /*variant*/
      l[8] === "default"), e.$set(f);
    },
    i(l) {
      t || (T(e.$$.fragment, l), t = !0);
    },
    o(l) {
      H(e.$$.fragment, l), t = !1;
    },
    d(l) {
      Zt(e, l);
    }
  };
}
function Jn(n) {
  let e, t, l, i, f, o = `${/*last_progress_level*/
  n[15] * 100}%`, r = (
    /*progress*/
    n[7] != null && dt(n)
  );
  return {
    c() {
      e = U("div"), t = U("div"), r && r.c(), l = P(), i = U("div"), f = U("div"), X(t, "class", "progress-level-inner svelte-vopvsi"), X(f, "class", "progress-bar svelte-vopvsi"), $(f, "width", o), X(i, "class", "progress-bar-wrap svelte-vopvsi"), X(e, "class", "progress-level svelte-vopvsi");
    },
    m(s, a) {
      v(s, e, a), le(e, t), r && r.m(t, null), le(e, l), le(e, i), le(i, f), n[31](f);
    },
    p(s, a) {
      /*progress*/
      s[7] != null ? r ? r.p(s, a) : (r = dt(s), r.c(), r.m(t, null)) : r && (r.d(1), r = null), a[0] & /*last_progress_level*/
      32768 && o !== (o = `${/*last_progress_level*/
      s[15] * 100}%`) && $(f, "width", o);
    },
    i: De,
    o: De,
    d(s) {
      s && k(e), r && r.d(), n[31](null);
    }
  };
}
function dt(n) {
  let e, t = Ce(
    /*progress*/
    n[7]
  ), l = [];
  for (let i = 0; i < t.length; i += 1)
    l[i] = wt(ot(n, t, i));
  return {
    c() {
      for (let i = 0; i < l.length; i += 1)
        l[i].c();
      e = re();
    },
    m(i, f) {
      for (let o = 0; o < l.length; o += 1)
        l[o] && l[o].m(i, f);
      v(i, e, f);
    },
    p(i, f) {
      if (f[0] & /*progress_level, progress*/
      16512) {
        t = Ce(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const r = ot(i, t, o);
          l[o] ? l[o].p(r, f) : (l[o] = wt(r), l[o].c(), l[o].m(e.parentNode, e));
        }
        for (; o < l.length; o += 1)
          l[o].d(1);
        l.length = t.length;
      }
    },
    d(i) {
      i && k(e), jt(l, i);
    }
  };
}
function mt(n) {
  let e, t, l, i, f = (
    /*i*/
    n[43] !== 0 && Kn()
  ), o = (
    /*p*/
    n[41].desc != null && bt(n)
  ), r = (
    /*p*/
    n[41].desc != null && /*progress_level*/
    n[14] && /*progress_level*/
    n[14][
      /*i*/
      n[43]
    ] != null && gt()
  ), s = (
    /*progress_level*/
    n[14] != null && ht(n)
  );
  return {
    c() {
      f && f.c(), e = P(), o && o.c(), t = P(), r && r.c(), l = P(), s && s.c(), i = re();
    },
    m(a, _) {
      f && f.m(a, _), v(a, e, _), o && o.m(a, _), v(a, t, _), r && r.m(a, _), v(a, l, _), s && s.m(a, _), v(a, i, _);
    },
    p(a, _) {
      /*p*/
      a[41].desc != null ? o ? o.p(a, _) : (o = bt(a), o.c(), o.m(t.parentNode, t)) : o && (o.d(1), o = null), /*p*/
      a[41].desc != null && /*progress_level*/
      a[14] && /*progress_level*/
      a[14][
        /*i*/
        a[43]
      ] != null ? r || (r = gt(), r.c(), r.m(l.parentNode, l)) : r && (r.d(1), r = null), /*progress_level*/
      a[14] != null ? s ? s.p(a, _) : (s = ht(a), s.c(), s.m(i.parentNode, i)) : s && (s.d(1), s = null);
    },
    d(a) {
      a && (k(e), k(t), k(l), k(i)), f && f.d(a), o && o.d(a), r && r.d(a), s && s.d(a);
    }
  };
}
function Kn(n) {
  let e;
  return {
    c() {
      e = M(" /");
    },
    m(t, l) {
      v(t, e, l);
    },
    d(t) {
      t && k(e);
    }
  };
}
function bt(n) {
  let e = (
    /*p*/
    n[41].desc + ""
  ), t;
  return {
    c() {
      t = M(e);
    },
    m(l, i) {
      v(l, t, i);
    },
    p(l, i) {
      i[0] & /*progress*/
      128 && e !== (e = /*p*/
      l[41].desc + "") && B(t, e);
    },
    d(l) {
      l && k(t);
    }
  };
}
function gt(n) {
  let e;
  return {
    c() {
      e = M("-");
    },
    m(t, l) {
      v(t, e, l);
    },
    d(t) {
      t && k(e);
    }
  };
}
function ht(n) {
  let e = (100 * /*progress_level*/
  (n[14][
    /*i*/
    n[43]
  ] || 0)).toFixed(1) + "", t, l;
  return {
    c() {
      t = M(e), l = M("%");
    },
    m(i, f) {
      v(i, t, f), v(i, l, f);
    },
    p(i, f) {
      f[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[43]
      ] || 0)).toFixed(1) + "") && B(t, e);
    },
    d(i) {
      i && (k(t), k(l));
    }
  };
}
function wt(n) {
  let e, t = (
    /*p*/
    (n[41].desc != null || /*progress_level*/
    n[14] && /*progress_level*/
    n[14][
      /*i*/
      n[43]
    ] != null) && mt(n)
  );
  return {
    c() {
      t && t.c(), e = re();
    },
    m(l, i) {
      t && t.m(l, i), v(l, e, i);
    },
    p(l, i) {
      /*p*/
      l[41].desc != null || /*progress_level*/
      l[14] && /*progress_level*/
      l[14][
        /*i*/
        l[43]
      ] != null ? t ? t.p(l, i) : (t = mt(l), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(l) {
      l && k(e), t && t.d(l);
    }
  };
}
function pt(n) {
  let e, t, l, i;
  const f = (
    /*#slots*/
    n[30]["additional-loading-text"]
  ), o = Nt(
    f,
    n,
    /*$$scope*/
    n[29],
    st
  );
  return {
    c() {
      e = U("p"), t = M(
        /*loading_text*/
        n[9]
      ), l = P(), o && o.c(), X(e, "class", "loading svelte-vopvsi");
    },
    m(r, s) {
      v(r, e, s), le(e, t), v(r, l, s), o && o.m(r, s), i = !0;
    },
    p(r, s) {
      (!i || s[0] & /*loading_text*/
      512) && B(
        t,
        /*loading_text*/
        r[9]
      ), o && o.p && (!i || s[0] & /*$$scope*/
      536870912) && Dt(
        o,
        f,
        r,
        /*$$scope*/
        r[29],
        i ? Bt(
          f,
          /*$$scope*/
          r[29],
          s,
          En
        ) : Pt(
          /*$$scope*/
          r[29]
        ),
        st
      );
    },
    i(r) {
      i || (T(o, r), i = !0);
    },
    o(r) {
      H(o, r), i = !1;
    },
    d(r) {
      r && (k(e), k(l)), o && o.d(r);
    }
  };
}
function Qn(n) {
  let e, t, l, i, f;
  const o = [Xn, Tn], r = [];
  function s(a, _) {
    return (
      /*status*/
      a[4] === "pending" ? 0 : (
        /*status*/
        a[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = s(n)) && (l = r[t] = o[t](n)), {
    c() {
      e = U("div"), l && l.c(), X(e, "class", i = "wrap " + /*variant*/
      n[8] + " " + /*show_progress*/
      n[6] + " svelte-vopvsi"), j(e, "hide", !/*status*/
      n[4] || /*status*/
      n[4] === "complete" || /*show_progress*/
      n[6] === "hidden"), j(
        e,
        "translucent",
        /*variant*/
        n[8] === "center" && /*status*/
        (n[4] === "pending" || /*status*/
        n[4] === "error") || /*translucent*/
        n[11] || /*show_progress*/
        n[6] === "minimal"
      ), j(
        e,
        "generating",
        /*status*/
        n[4] === "generating"
      ), j(
        e,
        "border",
        /*border*/
        n[12]
      ), $(
        e,
        "position",
        /*absolute*/
        n[10] ? "absolute" : "static"
      ), $(
        e,
        "padding",
        /*absolute*/
        n[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(a, _) {
      v(a, e, _), ~t && r[t].m(e, null), n[33](e), f = !0;
    },
    p(a, _) {
      let c = t;
      t = s(a), t === c ? ~t && r[t].p(a, _) : (l && (Ae(), H(r[c], 1, 1, () => {
        r[c] = null;
      }), Be()), ~t ? (l = r[t], l ? l.p(a, _) : (l = r[t] = o[t](a), l.c()), T(l, 1), l.m(e, null)) : l = null), (!f || _[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      a[8] + " " + /*show_progress*/
      a[6] + " svelte-vopvsi")) && X(e, "class", i), (!f || _[0] & /*variant, show_progress, status, show_progress*/
      336) && j(e, "hide", !/*status*/
      a[4] || /*status*/
      a[4] === "complete" || /*show_progress*/
      a[6] === "hidden"), (!f || _[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && j(
        e,
        "translucent",
        /*variant*/
        a[8] === "center" && /*status*/
        (a[4] === "pending" || /*status*/
        a[4] === "error") || /*translucent*/
        a[11] || /*show_progress*/
        a[6] === "minimal"
      ), (!f || _[0] & /*variant, show_progress, status*/
      336) && j(
        e,
        "generating",
        /*status*/
        a[4] === "generating"
      ), (!f || _[0] & /*variant, show_progress, border*/
      4416) && j(
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
      f || (T(l), f = !0);
    },
    o(a) {
      H(l), f = !1;
    },
    d(a) {
      a && k(e), ~t && r[t].d(), n[33](null);
    }
  };
}
var Wn = function(n, e, t, l) {
  function i(f) {
    return f instanceof t ? f : new t(function(o) {
      o(f);
    });
  }
  return new (t || (t = Promise))(function(f, o) {
    function r(_) {
      try {
        a(l.next(_));
      } catch (c) {
        o(c);
      }
    }
    function s(_) {
      try {
        a(l.throw(_));
      } catch (c) {
        o(c);
      }
    }
    function a(_) {
      _.done ? f(_.value) : i(_.value).then(r, s);
    }
    a((l = l.apply(n, e || [])).next());
  });
};
let pe = [], Ie = !1;
function xn(n) {
  return Wn(this, arguments, void 0, function* (e, t = !0) {
    if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
      if (pe.push(e), !Ie)
        Ie = !0;
      else
        return;
      yield Pn(), requestAnimationFrame(() => {
        let l = [0, 0];
        for (let i = 0; i < pe.length; i++) {
          const o = pe[i].getBoundingClientRect();
          (i === 0 || o.top + window.scrollY <= l[0]) && (l[0] = o.top + window.scrollY, l[1] = i);
        }
        window.scrollTo({ top: l[0] - 20, behavior: "smooth" }), Ie = !1, pe = [];
      });
    }
  });
}
function $n(n, e, t) {
  let l, { $$slots: i = {}, $$scope: f } = e;
  this && this.__awaiter;
  const o = An();
  let { i18n: r } = e, { eta: s = null } = e, { queue_position: a } = e, { queue_size: _ } = e, { status: c } = e, { scroll_to_output: w = !1 } = e, { timer: b = !0 } = e, { show_progress: y = "full" } = e, { message: S = null } = e, { progress: q = null } = e, { variant: z = "default" } = e, { loading_text: d = "Loading..." } = e, { absolute: u = !0 } = e, { translucent: m = !1 } = e, { border: F = !1 } = e, { autoscroll: g } = e, V, L = !1, Y = 0, J = 0, W = null, p = null, G = 0, K = null, _e, x = null, Oe = !0;
  const Xt = () => {
    t(0, s = t(27, W = t(19, de = null))), t(25, Y = performance.now()), t(26, J = 0), L = !0, Re();
  };
  function Re() {
    requestAnimationFrame(() => {
      t(26, J = (performance.now() - Y) / 1e3), L && Re();
    });
  }
  function Ue() {
    t(26, J = 0), t(0, s = t(27, W = t(19, de = null))), L && (L = !1);
  }
  Bn(() => {
    L && Ue();
  });
  let de = null;
  function Yt(h) {
    it[h ? "unshift" : "push"](() => {
      x = h, t(16, x), t(7, q), t(14, K), t(15, _e);
    });
  }
  const Gt = () => {
    o("clear_status");
  };
  function Ot(h) {
    it[h ? "unshift" : "push"](() => {
      V = h, t(13, V);
    });
  }
  return n.$$set = (h) => {
    "i18n" in h && t(1, r = h.i18n), "eta" in h && t(0, s = h.eta), "queue_position" in h && t(2, a = h.queue_position), "queue_size" in h && t(3, _ = h.queue_size), "status" in h && t(4, c = h.status), "scroll_to_output" in h && t(22, w = h.scroll_to_output), "timer" in h && t(5, b = h.timer), "show_progress" in h && t(6, y = h.show_progress), "message" in h && t(23, S = h.message), "progress" in h && t(7, q = h.progress), "variant" in h && t(8, z = h.variant), "loading_text" in h && t(9, d = h.loading_text), "absolute" in h && t(10, u = h.absolute), "translucent" in h && t(11, m = h.translucent), "border" in h && t(12, F = h.border), "autoscroll" in h && t(24, g = h.autoscroll), "$$scope" in h && t(29, f = h.$$scope);
  }, n.$$.update = () => {
    n.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    436207617 && (s === null && t(0, s = W), s != null && W !== s && (t(28, p = (performance.now() - Y) / 1e3 + s), t(19, de = p.toFixed(1)), t(27, W = s))), n.$$.dirty[0] & /*eta_from_start, timer_diff*/
    335544320 && t(17, G = p === null || p <= 0 || !J ? null : Math.min(J / p, 1)), n.$$.dirty[0] & /*progress*/
    128 && q != null && t(18, Oe = !1), n.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (q != null ? t(14, K = q.map((h) => {
      if (h.index != null && h.length != null)
        return h.index / h.length;
      if (h.progress != null)
        return h.progress;
    })) : t(14, K = null), K ? (t(15, _e = K[K.length - 1]), x && (_e === 0 ? t(16, x.style.transition = "0", x) : t(16, x.style.transition = "150ms", x))) : t(15, _e = void 0)), n.$$.dirty[0] & /*status*/
    16 && (c === "pending" ? Xt() : Ue()), n.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && V && w && (c === "pending" || c === "complete") && xn(V, g), n.$$.dirty[0] & /*status, message*/
    8388624, n.$$.dirty[0] & /*timer_diff*/
    67108864 && t(20, l = J.toFixed(1));
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
    F,
    V,
    K,
    _e,
    x,
    G,
    Oe,
    de,
    l,
    o,
    w,
    S,
    g,
    Y,
    J,
    W,
    p,
    f,
    i,
    Yt,
    Gt,
    Ot
  ];
}
class ei extends Nn {
  constructor(e) {
    super(), Zn(
      this,
      e,
      $n,
      Qn,
      jn,
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
  SvelteComponent: ti,
  append: te,
  assign: li,
  attr: N,
  binding_callbacks: ni,
  create_component: Ee,
  destroy_component: Te,
  destroy_each: ii,
  detach: Fe,
  element: se,
  ensure_array_like: kt,
  get_spread_object: fi,
  get_spread_update: si,
  init: oi,
  insert: Se,
  listen: vt,
  mount_component: Xe,
  run_all: ai,
  safe_not_equal: ri,
  set_data: Et,
  space: Ne,
  text: Tt,
  transition_in: Ye,
  transition_out: Ge
} = window.__gradio__svelte__internal, { afterUpdate: _i } = window.__gradio__svelte__internal;
function yt(n, e, t) {
  const l = n.slice();
  return l[11] = e[t][0], l[25] = e[t][1], l;
}
function ui(n) {
  let e;
  return {
    c() {
      e = Tt(
        /*label*/
        n[11]
      );
    },
    m(t, l) {
      Se(t, e, l);
    },
    p(t, l) {
      l & /*label*/
      2048 && Et(
        e,
        /*label*/
        t[11]
      );
    },
    d(t) {
      t && Fe(e);
    }
  };
}
function qt(n) {
  let e, t = (
    /*label*/
    n[11] + ""
  ), l;
  return {
    c() {
      e = se("span"), l = Tt(t);
    },
    m(i, f) {
      Se(i, e, f), te(e, l);
    },
    p(i, f) {
      f & /*categories*/
      1024 && t !== (t = /*label*/
      i[11] + "") && Et(l, t);
    },
    d(i) {
      i && Fe(e);
    }
  };
}
function ci(n) {
  let e, t, l, i, f, o, r, s, a, _, c, w, b, y, S;
  const q = [
    { autoscroll: (
      /*gradio*/
      n[0].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      n[0].i18n
    ) },
    /*loading_status*/
    n[9]
  ];
  let z = {};
  for (let m = 0; m < q.length; m += 1)
    z = li(z, q[m]);
  e = new ei({ props: z }), e.$on(
    "clear_status",
    /*clear_status_handler*/
    n[20]
  ), o = new Hl({
    props: {
      show_label: (
        /*show_label*/
        n[8]
      ),
      info: (
        /*info*/
        n[4]
      ),
      $$slots: { default: [ui] },
      $$scope: { ctx: n }
    }
  });
  let d = kt(
    /*categories*/
    n[10]
  ), u = [];
  for (let m = 0; m < d.length; m += 1)
    u[m] = qt(yt(n, d, m));
  return {
    c() {
      Ee(e.$$.fragment), t = Ne(), l = se("div"), i = se("div"), f = se("label"), Ee(o.$$.fragment), r = Ne(), s = se("div");
      for (let m = 0; m < u.length; m += 1)
        u[m].c();
      a = Ne(), _ = se("input"), N(
        f,
        "for",
        /*id*/
        n[14]
      ), N(i, "class", "head svelte-rzyrb9"), N(s, "class", "labels svelte-rzyrb9"), N(_, "type", "range"), N(
        _,
        "id",
        /*id*/
        n[14]
      ), N(_, "name", "cowbell"), N(_, "min", 0), N(_, "max", c = /*categories*/
      n[10].length - 1), N(_, "step", 1), _.disabled = /*disabled*/
      n[13], N(_, "aria-label", w = `range slider for ${/*label*/
      n[11]}`), N(_, "class", "slider svelte-rzyrb9"), N(l, "class", "wrap svelte-rzyrb9");
    },
    m(m, F) {
      Xe(e, m, F), Se(m, t, F), Se(m, l, F), te(l, i), te(i, f), Xe(o, f, null), te(l, r), te(l, s);
      for (let g = 0; g < u.length; g += 1)
        u[g] && u[g].m(s, null);
      te(l, a), te(l, _), n[21](_), b = !0, y || (S = [
        vt(
          _,
          "input",
          /*handle_input*/
          n[16]
        ),
        vt(
          _,
          "pointerup",
          /*handle_release*/
          n[15]
        )
      ], y = !0);
    },
    p(m, F) {
      const g = F & /*gradio, loading_status*/
      513 ? si(q, [
        F & /*gradio*/
        1 && { autoscroll: (
          /*gradio*/
          m[0].autoscroll
        ) },
        F & /*gradio*/
        1 && { i18n: (
          /*gradio*/
          m[0].i18n
        ) },
        F & /*loading_status*/
        512 && fi(
          /*loading_status*/
          m[9]
        )
      ]) : {};
      e.$set(g);
      const V = {};
      if (F & /*show_label*/
      256 && (V.show_label = /*show_label*/
      m[8]), F & /*info*/
      16 && (V.info = /*info*/
      m[4]), F & /*$$scope, label*/
      268437504 && (V.$$scope = { dirty: F, ctx: m }), o.$set(V), F & /*categories*/
      1024) {
        d = kt(
          /*categories*/
          m[10]
        );
        let L;
        for (L = 0; L < d.length; L += 1) {
          const Y = yt(m, d, L);
          u[L] ? u[L].p(Y, F) : (u[L] = qt(Y), u[L].c(), u[L].m(s, null));
        }
        for (; L < u.length; L += 1)
          u[L].d(1);
        u.length = d.length;
      }
      (!b || F & /*categories*/
      1024 && c !== (c = /*categories*/
      m[10].length - 1)) && N(_, "max", c), (!b || F & /*disabled*/
      8192) && (_.disabled = /*disabled*/
      m[13]), (!b || F & /*label*/
      2048 && w !== (w = `range slider for ${/*label*/
      m[11]}`)) && N(_, "aria-label", w);
    },
    i(m) {
      b || (Ye(e.$$.fragment, m), Ye(o.$$.fragment, m), b = !0);
    },
    o(m) {
      Ge(e.$$.fragment, m), Ge(o.$$.fragment, m), b = !1;
    },
    d(m) {
      m && (Fe(t), Fe(l)), Te(e, m), Te(o), ii(u, m), n[21](null), y = !1, ai(S);
    }
  };
}
function di(n) {
  let e, t;
  return e = new _l({
    props: {
      visible: (
        /*visible*/
        n[3]
      ),
      elem_id: (
        /*elem_id*/
        n[1]
      ),
      elem_classes: (
        /*elem_classes*/
        n[2]
      ),
      container: (
        /*container*/
        n[5]
      ),
      scale: (
        /*scale*/
        n[6]
      ),
      min_width: (
        /*min_width*/
        n[7]
      ),
      $$slots: { default: [ci] },
      $$scope: { ctx: n }
    }
  }), {
    c() {
      Ee(e.$$.fragment);
    },
    m(l, i) {
      Xe(e, l, i), t = !0;
    },
    p(l, [i]) {
      const f = {};
      i & /*visible*/
      8 && (f.visible = /*visible*/
      l[3]), i & /*elem_id*/
      2 && (f.elem_id = /*elem_id*/
      l[1]), i & /*elem_classes*/
      4 && (f.elem_classes = /*elem_classes*/
      l[2]), i & /*container*/
      32 && (f.container = /*container*/
      l[5]), i & /*scale*/
      64 && (f.scale = /*scale*/
      l[6]), i & /*min_width*/
      128 && (f.min_width = /*min_width*/
      l[7]), i & /*$$scope, categories, disabled, label, rangeInput, show_label, info, gradio, loading_status*/
      268451601 && (f.$$scope = { dirty: i, ctx: l }), e.$set(f);
    },
    i(l) {
      t || (Ye(e.$$.fragment, l), t = !0);
    },
    o(l) {
      Ge(e.$$.fragment, l), t = !1;
    },
    d(l) {
      Te(e, l);
    }
  };
}
let mi = 0;
function bi(n, e, t) {
  let l, { gradio: i } = e, { elem_id: f = "" } = e, { elem_classes: o = [] } = e, { visible: r = !0 } = e, { value: s = 0 } = e, { label: a = i.i18n("slider.slider") } = e, { info: _ = void 0 } = e, { container: c = !0 } = e, { scale: w = null } = e, { min_width: b = void 0 } = e, { show_label: y } = e, { interactive: S } = e, { loading_status: q } = e, { value_is_output: z = !1 } = e, { categories: d = [] } = e, u;
  const m = `range_id_${mi++}`;
  function F() {
    i.dispatch("change"), z || i.dispatch("input");
  }
  _i(() => {
    t(18, z = !1), V();
  });
  function g(p) {
    const G = parseInt(u.value), K = d[G];
    t(17, s = K[1]), i.dispatch("release", s);
  }
  function V() {
    u && (t(12, u.max = (d.length - 1).toString(), u), Y(), u.addEventListener("input", L));
  }
  function L() {
    const p = parseInt(u.value), G = d[p];
    t(17, s = G[1]), Y();
  }
  function Y() {
    if (u) {
      const p = d.findIndex((G) => G[1] === s);
      if (p !== -1) {
        t(12, u.value = p.toString(), u);
        const G = p / (d.length - 1) * 100;
        t(12, u.style.backgroundSize = G + "% 100%", u);
      }
    }
  }
  const J = () => i.dispatch("clear_status", q);
  function W(p) {
    ni[p ? "unshift" : "push"](() => {
      u = p, t(12, u);
    });
  }
  return n.$$set = (p) => {
    "gradio" in p && t(0, i = p.gradio), "elem_id" in p && t(1, f = p.elem_id), "elem_classes" in p && t(2, o = p.elem_classes), "visible" in p && t(3, r = p.visible), "value" in p && t(17, s = p.value), "label" in p && t(11, a = p.label), "info" in p && t(4, _ = p.info), "container" in p && t(5, c = p.container), "scale" in p && t(6, w = p.scale), "min_width" in p && t(7, b = p.min_width), "show_label" in p && t(8, y = p.show_label), "interactive" in p && t(19, S = p.interactive), "loading_status" in p && t(9, q = p.loading_status), "value_is_output" in p && t(18, z = p.value_is_output), "categories" in p && t(10, d = p.categories);
  }, n.$$.update = () => {
    n.$$.dirty & /*interactive*/
    524288 && t(13, l = !S), n.$$.dirty & /*value*/
    131072 && F();
  }, [
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
    l,
    m,
    g,
    L,
    s,
    z,
    S,
    J,
    W
  ];
}
class gi extends ti {
  constructor(e) {
    super(), oi(this, e, bi, di, ri, {
      gradio: 0,
      elem_id: 1,
      elem_classes: 2,
      visible: 3,
      value: 17,
      label: 11,
      info: 4,
      container: 5,
      scale: 6,
      min_width: 7,
      show_label: 8,
      interactive: 19,
      loading_status: 9,
      value_is_output: 18,
      categories: 10
    });
  }
}
export {
  gi as default
};
