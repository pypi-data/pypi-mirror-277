/* PrismJS 1.29.0
https://prismjs.com/download.html#themes=prism&languages=markup+clike+bash+c+cpp+cmake+csv+git+java+kotlin+latex+makefile+markdown+mermaid+powershell+python+regex+swift+yaml */
var _self = "undefined" != typeof window ? window : "undefined" != typeof WorkerGlobalScope && self instanceof WorkerGlobalScope ? self : {},
	Prism = function (e) {
		var n = /(?:^|\s)lang(?:uage)?-([\w-]+)(?=\s|$)/i, t = 0, r = {}, a = {
			manual: e.Prism && e.Prism.manual,
			disableWorkerMessageHandler: e.Prism && e.Prism.disableWorkerMessageHandler,
			util: {
				encode: function e(n) {
					return n instanceof i ? new i(n.type, e(n.content), n.alias) : Array.isArray(n) ? n.map(e) : n.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/\u00a0/g, " ")
				}, type: function (e) {
					return Object.prototype.toString.call(e).slice(8, -1)
				}, objId: function (e) {
					return e.__id || Object.defineProperty(e, "__id", {value: ++t}), e.__id
				}, clone: function e(n, t) {
					var r, i;
					switch (t = t || {}, a.util.type(n)) {
						case"Object":
							if (i = a.util.objId(n), t[i]) return t[i];
							for (var l in r = {}, t[i] = r, n) n.hasOwnProperty(l) && (r[l] = e(n[l], t));
							return r;
						case"Array":
							return i = a.util.objId(n), t[i] ? t[i] : (r = [], t[i] = r, n.forEach((function (n, a) {
								r[a] = e(n, t)
							})), r);
						default:
							return n
					}
				}, getLanguage: function (e) {
					for (; e;) {
						var t = n.exec(e.className);
						if (t) return t[1].toLowerCase();
						e = e.parentElement
					}
					return "none"
				}, setLanguage: function (e, t) {
					e.className = e.className.replace(RegExp(n, "gi"), ""), e.classList.add("language-" + t)
				}, currentScript: function () {
					if ("undefined" == typeof document) return null;
					if ("currentScript" in document) return document.currentScript;
					try {
						throw new Error
					} catch (r) {
						var e = (/at [^(\r\n]*\((.*):[^:]+:[^:]+\)$/i.exec(r.stack) || [])[1];
						if (e) {
							var n = document.getElementsByTagName("script");
							for (var t in n) if (n[t].src == e) return n[t]
						}
						return null
					}
				}, isActive: function (e, n, t) {
					for (var r = "no-" + n; e;) {
						var a = e.classList;
						if (a.contains(n)) return !0;
						if (a.contains(r)) return !1;
						e = e.parentElement
					}
					return !!t
				}
			},
			languages: {
				plain: r, plaintext: r, text: r, txt: r, extend: function (e, n) {
					var t = a.util.clone(a.languages[e]);
					for (var r in n) t[r] = n[r];
					return t
				}, insertBefore: function (e, n, t, r) {
					var i = (r = r || a.languages)[e], l = {};
					for (var o in i) if (i.hasOwnProperty(o)) {
						if (o == n) for (var s in t) t.hasOwnProperty(s) && (l[s] = t[s]);
						t.hasOwnProperty(o) || (l[o] = i[o])
					}
					var u = r[e];
					return r[e] = l, a.languages.DFS(a.languages, (function (n, t) {
						t === u && n != e && (this[n] = l)
					})), l
				}, DFS: function e(n, t, r, i) {
					i = i || {};
					var l = a.util.objId;
					for (var o in n) if (n.hasOwnProperty(o)) {
						t.call(n, o, n[o], r || o);
						var s = n[o], u = a.util.type(s);
						"Object" !== u || i[l(s)] ? "Array" !== u || i[l(s)] || (i[l(s)] = !0, e(s, t, o, i)) : (i[l(s)] = !0, e(s, t, null, i))
					}
				}
			},
			plugins: {},
			highlightAll: function (e, n) {
				a.highlightAllUnder(document, e, n)
			},
			highlightAllUnder: function (e, n, t) {
				var r = {
					callback: t,
					container: e,
					selector: 'code[class*="language-"], [class*="language-"] code, code[class*="lang-"], [class*="lang-"] code'
				};
				a.hooks.run("before-highlightall", r), r.elements = Array.prototype.slice.apply(r.container.querySelectorAll(r.selector)), a.hooks.run("before-all-elements-highlight", r);
				for (var i, l = 0; i = r.elements[l++];) a.highlightElement(i, !0 === n, r.callback)
			},
			highlightElement: function (n, t, r) {
				var i = a.util.getLanguage(n), l = a.languages[i];
				a.util.setLanguage(n, i);
				var o = n.parentElement;
				o && "pre" === o.nodeName.toLowerCase() && a.util.setLanguage(o, i);
				var s = {element: n, language: i, grammar: l, code: n.textContent};

				function u(e) {
					s.highlightedCode = e, a.hooks.run("before-insert", s), s.element.innerHTML = s.highlightedCode, a.hooks.run("after-highlight", s), a.hooks.run("complete", s), r && r.call(s.element)
				}

				if (a.hooks.run("before-sanity-check", s), (o = s.element.parentElement) && "pre" === o.nodeName.toLowerCase() && !o.hasAttribute("tabindex") && o.setAttribute("tabindex", "0"), !s.code) return a.hooks.run("complete", s), void (r && r.call(s.element));
				if (a.hooks.run("before-highlight", s), s.grammar) if (t && e.Worker) {
					var c = new Worker(a.filename);
					c.onmessage = function (e) {
						u(e.data)
					}, c.postMessage(JSON.stringify({language: s.language, code: s.code, immediateClose: !0}))
				} else u(a.highlight(s.code, s.grammar, s.language)); else u(a.util.encode(s.code))
			},
			highlight: function (e, n, t) {
				var r = {code: e, grammar: n, language: t};
				if (a.hooks.run("before-tokenize", r), !r.grammar) throw new Error('The language "' + r.language + '" has no grammar.');
				return r.tokens = a.tokenize(r.code, r.grammar), a.hooks.run("after-tokenize", r), i.stringify(a.util.encode(r.tokens), r.language)
			},
			tokenize: function (e, n) {
				var t = n.rest;
				if (t) {
					for (var r in t) n[r] = t[r];
					delete n.rest
				}
				var a = new s;
				return u(a, a.head, e), o(e, a, n, a.head, 0), function (e) {
					for (var n = [], t = e.head.next; t !== e.tail;) n.push(t.value), t = t.next;
					return n
				}(a)
			},
			hooks: {
				all: {}, add: function (e, n) {
					var t = a.hooks.all;
					t[e] = t[e] || [], t[e].push(n)
				}, run: function (e, n) {
					var t = a.hooks.all[e];
					if (t && t.length) for (var r, i = 0; r = t[i++];) r(n)
				}
			},
			Token: i
		};

		function i(e, n, t, r) {
			this.type = e, this.content = n, this.alias = t, this.length = 0 | (r || "").length
		}

		function l(e, n, t, r) {
			e.lastIndex = n;
			var a = e.exec(t);
			if (a && r && a[1]) {
				var i = a[1].length;
				a.index += i, a[0] = a[0].slice(i)
			}
			return a
		}

		function o(e, n, t, r, s, g) {
			for (var f in t) if (t.hasOwnProperty(f) && t[f]) {
				var h = t[f];
				h = Array.isArray(h) ? h : [h];
				for (var d = 0; d < h.length; ++d) {
					if (g && g.cause == f + "," + d) return;
					var v = h[d], p = v.inside, m = !!v.lookbehind, y = !!v.greedy, k = v.alias;
					if (y && !v.pattern.global) {
						var x = v.pattern.toString().match(/[imsuy]*$/)[0];
						v.pattern = RegExp(v.pattern.source, x + "g")
					}
					for (var b = v.pattern || v, w = r.next, A = s; w !== n.tail && !(g && A >= g.reach); A += w.value.length, w = w.next) {
						var E = w.value;
						if (n.length > e.length) return;
						if (!(E instanceof i)) {
							var P, L = 1;
							if (y) {
								if (!(P = l(b, A, e, m)) || P.index >= e.length) break;
								var S = P.index, O = P.index + P[0].length, j = A;
								for (j += w.value.length; S >= j;) j += (w = w.next).value.length;
								if (A = j -= w.value.length, w.value instanceof i) continue;
								for (var C = w; C !== n.tail && (j < O || "string" == typeof C.value); C = C.next) L++, j += C.value.length;
								L--, E = e.slice(A, j), P.index -= A
							} else if (!(P = l(b, 0, E, m))) continue;
							S = P.index;
							var N = P[0], _ = E.slice(0, S), M = E.slice(S + N.length), W = A + E.length;
							g && W > g.reach && (g.reach = W);
							var z = w.prev;
							if (_ && (z = u(n, z, _), A += _.length), c(n, z, L), w = u(n, z, new i(f, p ? a.tokenize(N, p) : N, k, N)), M && u(n, w, M), L > 1) {
								var I = {cause: f + "," + d, reach: W};
								o(e, n, t, w.prev, A, I), g && I.reach > g.reach && (g.reach = I.reach)
							}
						}
					}
				}
			}
		}

		function s() {
			var e = {value: null, prev: null, next: null}, n = {value: null, prev: e, next: null};
			e.next = n, this.head = e, this.tail = n, this.length = 0
		}

		function u(e, n, t) {
			var r = n.next, a = {value: t, prev: n, next: r};
			return n.next = a, r.prev = a, e.length++, a
		}

		function c(e, n, t) {
			for (var r = n.next, a = 0; a < t && r !== e.tail; a++) r = r.next;
			n.next = r, r.prev = n, e.length -= a
		}

		if (e.Prism = a, i.stringify = function e(n, t) {
			if ("string" == typeof n) return n;
			if (Array.isArray(n)) {
				var r = "";
				return n.forEach((function (n) {
					r += e(n, t)
				})), r
			}
			var i = {
				type: n.type,
				content: e(n.content, t),
				tag: "span",
				classes: ["token", n.type],
				attributes: {},
				language: t
			}, l = n.alias;
			l && (Array.isArray(l) ? Array.prototype.push.apply(i.classes, l) : i.classes.push(l)), a.hooks.run("wrap", i);
			var o = "";
			for (var s in i.attributes) o += " " + s + '="' + (i.attributes[s] || "").replace(/"/g, "&quot;") + '"';
			return "<" + i.tag + ' class="' + i.classes.join(" ") + '"' + o + ">" + i.content + "</" + i.tag + ">"
		}, !e.document) return e.addEventListener ? (a.disableWorkerMessageHandler || e.addEventListener("message", (function (n) {
			var t = JSON.parse(n.data), r = t.language, i = t.code, l = t.immediateClose;
			e.postMessage(a.highlight(i, a.languages[r], r)), l && e.close()
		}), !1), a) : a;
		var g = a.util.currentScript();

		function f() {
			a.manual || a.highlightAll()
		}

		if (g && (a.filename = g.src, g.hasAttribute("data-manual") && (a.manual = !0)), !a.manual) {
			var h = document.readyState;
			"loading" === h || "interactive" === h && g && g.defer ? document.addEventListener("DOMContentLoaded", f) : window.requestAnimationFrame ? window.requestAnimationFrame(f) : window.setTimeout(f, 16)
		}
		return a
	}(_self);
"undefined" != typeof module && module.exports && (module.exports = Prism), "undefined" != typeof global && (global.Prism = Prism);
Prism.languages.markup = {
	comment: {pattern: /<!--(?:(?!<!--)[\s\S])*?-->/, greedy: !0},
	prolog: {pattern: /<\?[\s\S]+?\?>/, greedy: !0},
	doctype: {
		pattern: /<!DOCTYPE(?:[^>"'[\]]|"[^"]*"|'[^']*')+(?:\[(?:[^<"'\]]|"[^"]*"|'[^']*'|<(?!!--)|<!--(?:[^-]|-(?!->))*-->)*\]\s*)?>/i,
		greedy: !0,
		inside: {
			"internal-subset": {pattern: /(^[^\[]*\[)[\s\S]+(?=\]>$)/, lookbehind: !0, greedy: !0, inside: null},
			string: {pattern: /"[^"]*"|'[^']*'/, greedy: !0},
			punctuation: /^<!|>$|[[\]]/,
			"doctype-tag": /^DOCTYPE/i,
			name: /[^\s<>'"]+/
		}
	},
	cdata: {pattern: /<!\[CDATA\[[\s\S]*?\]\]>/i, greedy: !0},
	tag: {
		pattern: /<\/?(?!\d)[^\s>\/=$<%]+(?:\s(?:\s*[^\s>\/=]+(?:\s*=\s*(?:"[^"]*"|'[^']*'|[^\s'">=]+(?=[\s>]))|(?=[\s/>])))+)?\s*\/?>/,
		greedy: !0,
		inside: {
			tag: {pattern: /^<\/?[^\s>\/]+/, inside: {punctuation: /^<\/?/, namespace: /^[^\s>\/:]+:/}},
			"special-attr": [],
			"attr-value": {
				pattern: /=\s*(?:"[^"]*"|'[^']*'|[^\s'">=]+)/,
				inside: {
					punctuation: [{pattern: /^=/, alias: "attr-equals"}, {
						pattern: /^(\s*)["']|["']$/,
						lookbehind: !0
					}]
				}
			},
			punctuation: /\/?>/,
			"attr-name": {pattern: /[^\s>\/]+/, inside: {namespace: /^[^\s>\/:]+:/}}
		}
	},
	entity: [{pattern: /&[\da-z]{1,8};/i, alias: "named-entity"}, /&#x?[\da-f]{1,8};/i]
}, Prism.languages.markup.tag.inside["attr-value"].inside.entity = Prism.languages.markup.entity, Prism.languages.markup.doctype.inside["internal-subset"].inside = Prism.languages.markup, Prism.hooks.add("wrap", (function (a) {
	"entity" === a.type && (a.attributes.title = a.content.replace(/&amp;/, "&"))
})), Object.defineProperty(Prism.languages.markup.tag, "addInlined", {
	value: function (a, e) {
		var s = {};
		s["language-" + e] = {
			pattern: /(^<!\[CDATA\[)[\s\S]+?(?=\]\]>$)/i,
			lookbehind: !0,
			inside: Prism.languages[e]
		}, s.cdata = /^<!\[CDATA\[|\]\]>$/i;
		var t = {"included-cdata": {pattern: /<!\[CDATA\[[\s\S]*?\]\]>/i, inside: s}};
		t["language-" + e] = {pattern: /[\s\S]+/, inside: Prism.languages[e]};
		var n = {};
		n[a] = {
			pattern: RegExp("(<__[^>]*>)(?:<!\\[CDATA\\[(?:[^\\]]|\\](?!\\]>))*\\]\\]>|(?!<!\\[CDATA\\[)[^])*?(?=</__>)".replace(/__/g, (function () {
				return a
			})), "i"), lookbehind: !0, greedy: !0, inside: t
		}, Prism.languages.insertBefore("markup", "cdata", n)
	}
}), Object.defineProperty(Prism.languages.markup.tag, "addAttribute", {
	value: function (a, e) {
		Prism.languages.markup.tag.inside["special-attr"].push({
			pattern: RegExp("(^|[\"'\\s])(?:" + a + ")\\s*=\\s*(?:\"[^\"]*\"|'[^']*'|[^\\s'\">=]+(?=[\\s>]))", "i"),
			lookbehind: !0,
			inside: {
				"attr-name": /^[^\s=]+/,
				"attr-value": {
					pattern: /=[\s\S]+/,
					inside: {
						value: {
							pattern: /(^=\s*(["']|(?!["'])))\S[\s\S]*(?=\2$)/,
							lookbehind: !0,
							alias: [e, "language-" + e],
							inside: Prism.languages[e]
						}, punctuation: [{pattern: /^=/, alias: "attr-equals"}, /"|'/]
					}
				}
			}
		})
	}
}), Prism.languages.html = Prism.languages.markup, Prism.languages.mathml = Prism.languages.markup, Prism.languages.svg = Prism.languages.markup, Prism.languages.xml = Prism.languages.extend("markup", {}), Prism.languages.ssml = Prism.languages.xml, Prism.languages.atom = Prism.languages.xml, Prism.languages.rss = Prism.languages.xml;
Prism.languages.clike = {
	comment: [{
		pattern: /(^|[^\\])\/\*[\s\S]*?(?:\*\/|$)/,
		lookbehind: !0,
		greedy: !0
	}, {pattern: /(^|[^\\:])\/\/.*/, lookbehind: !0, greedy: !0}],
	string: {pattern: /(["'])(?:\\(?:\r\n|[\s\S])|(?!\1)[^\\\r\n])*\1/, greedy: !0},
	"class-name": {
		pattern: /(\b(?:class|extends|implements|instanceof|interface|new|trait)\s+|\bcatch\s+\()[\w.\\]+/i,
		lookbehind: !0,
		inside: {punctuation: /[.\\]/}
	},
	keyword: /\b(?:break|catch|continue|do|else|finally|for|function|if|in|instanceof|new|null|return|throw|try|while)\b/,
	boolean: /\b(?:false|true)\b/,
	function: /\b\w+(?=\()/,
	number: /\b0x[\da-f]+\b|(?:\b\d+(?:\.\d*)?|\B\.\d+)(?:e[+-]?\d+)?/i,
	operator: /[<>]=?|[!=]=?=?|--?|\+\+?|&&?|\|\|?|[?*/~^%]/,
	punctuation: /[{}[\];(),.:]/
};
!function (e) {
	var t = "\\b(?:BASH|BASHOPTS|BASH_ALIASES|BASH_ARGC|BASH_ARGV|BASH_CMDS|BASH_COMPLETION_COMPAT_DIR|BASH_LINENO|BASH_REMATCH|BASH_SOURCE|BASH_VERSINFO|BASH_VERSION|COLORTERM|COLUMNS|COMP_WORDBREAKS|DBUS_SESSION_BUS_ADDRESS|DEFAULTS_PATH|DESKTOP_SESSION|DIRSTACK|DISPLAY|EUID|GDMSESSION|GDM_LANG|GNOME_KEYRING_CONTROL|GNOME_KEYRING_PID|GPG_AGENT_INFO|GROUPS|HISTCONTROL|HISTFILE|HISTFILESIZE|HISTSIZE|HOME|HOSTNAME|HOSTTYPE|IFS|INSTANCE|JOB|LANG|LANGUAGE|LC_ADDRESS|LC_ALL|LC_IDENTIFICATION|LC_MEASUREMENT|LC_MONETARY|LC_NAME|LC_NUMERIC|LC_PAPER|LC_TELEPHONE|LC_TIME|LESSCLOSE|LESSOPEN|LINES|LOGNAME|LS_COLORS|MACHTYPE|MAILCHECK|MANDATORY_PATH|NO_AT_BRIDGE|OLDPWD|OPTERR|OPTIND|ORBIT_SOCKETDIR|OSTYPE|PAPERSIZE|PATH|PIPESTATUS|PPID|PS1|PS2|PS3|PS4|PWD|RANDOM|REPLY|SECONDS|SELINUX_INIT|SESSION|SESSIONTYPE|SESSION_MANAGER|SHELL|SHELLOPTS|SHLVL|SSH_AUTH_SOCK|TERM|UID|UPSTART_EVENTS|UPSTART_INSTANCE|UPSTART_JOB|UPSTART_SESSION|USER|WINDOWID|XAUTHORITY|XDG_CONFIG_DIRS|XDG_CURRENT_DESKTOP|XDG_DATA_DIRS|XDG_GREETER_DATA_DIR|XDG_MENU_PREFIX|XDG_RUNTIME_DIR|XDG_SEAT|XDG_SEAT_PATH|XDG_SESSION_DESKTOP|XDG_SESSION_ID|XDG_SESSION_PATH|XDG_SESSION_TYPE|XDG_VTNR|XMODIFIERS)\\b",
		a = {pattern: /(^(["']?)\w+\2)[ \t]+\S.*/, lookbehind: !0, alias: "punctuation", inside: null}, n = {
			bash: a,
			environment: {pattern: RegExp("\\$" + t), alias: "constant"},
			variable: [{
				pattern: /\$?\(\([\s\S]+?\)\)/,
				greedy: !0,
				inside: {
					variable: [{pattern: /(^\$\(\([\s\S]+)\)\)/, lookbehind: !0}, /^\$\(\(/],
					number: /\b0x[\dA-Fa-f]+\b|(?:\b\d+(?:\.\d*)?|\B\.\d+)(?:[Ee]-?\d+)?/,
					operator: /--|\+\+|\*\*=?|<<=?|>>=?|&&|\|\||[=!+\-*/%<>^&|]=?|[?~:]/,
					punctuation: /\(\(?|\)\)?|,|;/
				}
			}, {
				pattern: /\$\((?:\([^)]+\)|[^()])+\)|`[^`]+`/,
				greedy: !0,
				inside: {variable: /^\$\(|^`|\)$|`$/}
			}, {
				pattern: /\$\{[^}]+\}/,
				greedy: !0,
				inside: {
					operator: /:[-=?+]?|[!\/]|##?|%%?|\^\^?|,,?/,
					punctuation: /[\[\]]/,
					environment: {pattern: RegExp("(\\{)" + t), lookbehind: !0, alias: "constant"}
				}
			}, /\$(?:\w+|[#?*!@$])/],
			entity: /\\(?:[abceEfnrtv\\"]|O?[0-7]{1,3}|U[0-9a-fA-F]{8}|u[0-9a-fA-F]{4}|x[0-9a-fA-F]{1,2})/
		};
	e.languages.bash = {
		shebang: {pattern: /^#!\s*\/.*/, alias: "important"},
		comment: {pattern: /(^|[^"{\\$])#.*/, lookbehind: !0},
		"function-name": [{
			pattern: /(\bfunction\s+)[\w-]+(?=(?:\s*\(?:\s*\))?\s*\{)/,
			lookbehind: !0,
			alias: "function"
		}, {pattern: /\b[\w-]+(?=\s*\(\s*\)\s*\{)/, alias: "function"}],
		"for-or-select": {pattern: /(\b(?:for|select)\s+)\w+(?=\s+in\s)/, alias: "variable", lookbehind: !0},
		"assign-left": {
			pattern: /(^|[\s;|&]|[<>]\()\w+(?:\.\w+)*(?=\+?=)/,
			inside: {environment: {pattern: RegExp("(^|[\\s;|&]|[<>]\\()" + t), lookbehind: !0, alias: "constant"}},
			alias: "variable",
			lookbehind: !0
		},
		parameter: {pattern: /(^|\s)-{1,2}(?:\w+:[+-]?)?\w+(?:\.\w+)*(?=[=\s]|$)/, alias: "variable", lookbehind: !0},
		string: [{
			pattern: /((?:^|[^<])<<-?\s*)(\w+)\s[\s\S]*?(?:\r?\n|\r)\2/,
			lookbehind: !0,
			greedy: !0,
			inside: n
		}, {
			pattern: /((?:^|[^<])<<-?\s*)(["'])(\w+)\2\s[\s\S]*?(?:\r?\n|\r)\3/,
			lookbehind: !0,
			greedy: !0,
			inside: {bash: a}
		}, {
			pattern: /(^|[^\\](?:\\\\)*)"(?:\\[\s\S]|\$\([^)]+\)|\$(?!\()|`[^`]+`|[^"\\`$])*"/,
			lookbehind: !0,
			greedy: !0,
			inside: n
		}, {pattern: /(^|[^$\\])'[^']*'/, lookbehind: !0, greedy: !0}, {
			pattern: /\$'(?:[^'\\]|\\[\s\S])*'/,
			greedy: !0,
			inside: {entity: n.entity}
		}],
		environment: {pattern: RegExp("\\$?" + t), alias: "constant"},
		variable: n.variable,
		function: {
			pattern: /(^|[\s;|&]|[<>]\()(?:add|apropos|apt|apt-cache|apt-get|aptitude|aspell|automysqlbackup|awk|basename|bash|bc|bconsole|bg|bzip2|cal|cargo|cat|cfdisk|chgrp|chkconfig|chmod|chown|chroot|cksum|clear|cmp|column|comm|composer|cp|cron|crontab|csplit|curl|cut|date|dc|dd|ddrescue|debootstrap|df|diff|diff3|dig|dir|dircolors|dirname|dirs|dmesg|docker|docker-compose|du|egrep|eject|env|ethtool|expand|expect|expr|fdformat|fdisk|fg|fgrep|file|find|fmt|fold|format|free|fsck|ftp|fuser|gawk|git|gparted|grep|groupadd|groupdel|groupmod|groups|grub-mkconfig|gzip|halt|head|hg|history|host|hostname|htop|iconv|id|ifconfig|ifdown|ifup|import|install|ip|java|jobs|join|kill|killall|less|link|ln|locate|logname|logrotate|look|lpc|lpr|lprint|lprintd|lprintq|lprm|ls|lsof|lynx|make|man|mc|mdadm|mkconfig|mkdir|mke2fs|mkfifo|mkfs|mkisofs|mknod|mkswap|mmv|more|most|mount|mtools|mtr|mutt|mv|nano|nc|netstat|nice|nl|node|nohup|notify-send|npm|nslookup|op|open|parted|passwd|paste|pathchk|ping|pkill|pnpm|podman|podman-compose|popd|pr|printcap|printenv|ps|pushd|pv|quota|quotacheck|quotactl|ram|rar|rcp|reboot|remsync|rename|renice|rev|rm|rmdir|rpm|rsync|scp|screen|sdiff|sed|sendmail|seq|service|sftp|sh|shellcheck|shuf|shutdown|sleep|slocate|sort|split|ssh|stat|strace|su|sudo|sum|suspend|swapon|sync|sysctl|tac|tail|tar|tee|time|timeout|top|touch|tr|traceroute|tsort|tty|umount|uname|unexpand|uniq|units|unrar|unshar|unzip|update-grub|uptime|useradd|userdel|usermod|users|uudecode|uuencode|v|vcpkg|vdir|vi|vim|virsh|vmstat|wait|watch|wc|wget|whereis|which|who|whoami|write|xargs|xdg-open|yarn|yes|zenity|zip|zsh|zypper)(?=$|[)\s;|&])/,
			lookbehind: !0
		},
		keyword: {
			pattern: /(^|[\s;|&]|[<>]\()(?:case|do|done|elif|else|esac|fi|for|function|if|in|select|then|until|while)(?=$|[)\s;|&])/,
			lookbehind: !0
		},
		builtin: {
			pattern: /(^|[\s;|&]|[<>]\()(?:\.|:|alias|bind|break|builtin|caller|cd|command|continue|declare|echo|enable|eval|exec|exit|export|getopts|hash|help|let|local|logout|mapfile|printf|pwd|read|readarray|readonly|return|set|shift|shopt|source|test|times|trap|type|typeset|ulimit|umask|unalias|unset)(?=$|[)\s;|&])/,
			lookbehind: !0,
			alias: "class-name"
		},
		boolean: {pattern: /(^|[\s;|&]|[<>]\()(?:false|true)(?=$|[)\s;|&])/, lookbehind: !0},
		"file-descriptor": {pattern: /\B&\d\b/, alias: "important"},
		operator: {
			pattern: /\d?<>|>\||\+=|=[=~]?|!=?|<<[<-]?|[&\d]?>>|\d[<>]&?|[<>][&=]?|&[>&]?|\|[&|]?/,
			inside: {"file-descriptor": {pattern: /^\d/, alias: "important"}}
		},
		punctuation: /\$?\(\(?|\)\)?|\.\.|[{}[\];\\]/,
		number: {pattern: /(^|\s)(?:[1-9]\d*|0)(?:[.,]\d+)?\b/, lookbehind: !0}
	}, a.inside = e.languages.bash;
	for (var s = ["comment", "function-name", "for-or-select", "assign-left", "parameter", "string", "environment", "function", "keyword", "builtin", "boolean", "file-descriptor", "operator", "punctuation", "number"], o = n.variable[1].inside, i = 0; i < s.length; i++) o[s[i]] = e.languages.bash[s[i]];
	e.languages.sh = e.languages.bash, e.languages.shell = e.languages.bash
}(Prism);
Prism.languages.c = Prism.languages.extend("clike", {
	comment: {
		pattern: /\/\/(?:[^\r\n\\]|\\(?:\r\n?|\n|(?![\r\n])))*|\/\*[\s\S]*?(?:\*\/|$)/,
		greedy: !0
	},
	string: {pattern: /"(?:\\(?:\r\n|[\s\S])|[^"\\\r\n])*"/, greedy: !0},
	"class-name": {
		pattern: /(\b(?:enum|struct)\s+(?:__attribute__\s*\(\([\s\S]*?\)\)\s*)?)\w+|\b[a-z]\w*_t\b/,
		lookbehind: !0
	},
	keyword: /\b(?:_Alignas|_Alignof|_Atomic|_Bool|_Complex|_Generic|_Imaginary|_Noreturn|_Static_assert|_Thread_local|__attribute__|asm|auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|inline|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|typeof|union|unsigned|void|volatile|while)\b/,
	function: /\b[a-z_]\w*(?=\s*\()/i,
	number: /(?:\b0x(?:[\da-f]+(?:\.[\da-f]*)?|\.[\da-f]+)(?:p[+-]?\d+)?|(?:\b\d+(?:\.\d*)?|\B\.\d+)(?:e[+-]?\d+)?)[ful]{0,4}/i,
	operator: />>=?|<<=?|->|([-+&|:])\1|[?:~]|[-+*/%&|^!=<>]=?/
}), Prism.languages.insertBefore("c", "string", {
	char: {
		pattern: /'(?:\\(?:\r\n|[\s\S])|[^'\\\r\n]){0,32}'/,
		greedy: !0
	}
}), Prism.languages.insertBefore("c", "string", {
	macro: {
		pattern: /(^[\t ]*)#\s*[a-z](?:[^\r\n\\/]|\/(?!\*)|\/\*(?:[^*]|\*(?!\/))*\*\/|\\(?:\r\n|[\s\S]))*/im,
		lookbehind: !0,
		greedy: !0,
		alias: "property",
		inside: {
			string: [{pattern: /^(#\s*include\s*)<[^>]+>/, lookbehind: !0}, Prism.languages.c.string],
			char: Prism.languages.c.char,
			comment: Prism.languages.c.comment,
			"macro-name": [{
				pattern: /(^#\s*define\s+)\w+\b(?!\()/i,
				lookbehind: !0
			}, {pattern: /(^#\s*define\s+)\w+\b(?=\()/i, lookbehind: !0, alias: "function"}],
			directive: {pattern: /^(#\s*)[a-z]+/, lookbehind: !0, alias: "keyword"},
			"directive-hash": /^#/,
			punctuation: /##|\\(?=[\r\n])/,
			expression: {pattern: /\S[\s\S]*/, inside: Prism.languages.c}
		}
	}
}), Prism.languages.insertBefore("c", "function", {constant: /\b(?:EOF|NULL|SEEK_CUR|SEEK_END|SEEK_SET|__DATE__|__FILE__|__LINE__|__TIMESTAMP__|__TIME__|__func__|stderr|stdin|stdout)\b/}), delete Prism.languages.c.boolean;
!function (e) {
	var t = /\b(?:alignas|alignof|asm|auto|bool|break|case|catch|char|char16_t|char32_t|char8_t|class|co_await|co_return|co_yield|compl|concept|const|const_cast|consteval|constexpr|constinit|continue|decltype|default|delete|do|double|dynamic_cast|else|enum|explicit|export|extern|final|float|for|friend|goto|if|import|inline|int|int16_t|int32_t|int64_t|int8_t|long|module|mutable|namespace|new|noexcept|nullptr|operator|override|private|protected|public|register|reinterpret_cast|requires|return|short|signed|sizeof|static|static_assert|static_cast|struct|switch|template|this|thread_local|throw|try|typedef|typeid|typename|uint16_t|uint32_t|uint64_t|uint8_t|union|unsigned|using|virtual|void|volatile|wchar_t|while)\b/,
		n = "\\b(?!<keyword>)\\w+(?:\\s*\\.\\s*\\w+)*\\b".replace(/<keyword>/g, (function () {
			return t.source
		}));
	e.languages.cpp = e.languages.extend("c", {
		"class-name": [{
			pattern: RegExp("(\\b(?:class|concept|enum|struct|typename)\\s+)(?!<keyword>)\\w+".replace(/<keyword>/g, (function () {
				return t.source
			}))), lookbehind: !0
		}, /\b[A-Z]\w*(?=\s*::\s*\w+\s*\()/, /\b[A-Z_]\w*(?=\s*::\s*~\w+\s*\()/i, /\b\w+(?=\s*<(?:[^<>]|<(?:[^<>]|<[^<>]*>)*>)*>\s*::\s*\w+\s*\()/],
		keyword: t,
		number: {
			pattern: /(?:\b0b[01']+|\b0x(?:[\da-f']+(?:\.[\da-f']*)?|\.[\da-f']+)(?:p[+-]?[\d']+)?|(?:\b[\d']+(?:\.[\d']*)?|\B\.[\d']+)(?:e[+-]?[\d']+)?)[ful]{0,4}/i,
			greedy: !0
		},
		operator: />>=?|<<=?|->|--|\+\+|&&|\|\||[?:~]|<=>|[-+*/%&|^!=<>]=?|\b(?:and|and_eq|bitand|bitor|not|not_eq|or|or_eq|xor|xor_eq)\b/,
		boolean: /\b(?:false|true)\b/
	}), e.languages.insertBefore("cpp", "string", {
		module: {
			pattern: RegExp('(\\b(?:import|module)\\s+)(?:"(?:\\\\(?:\r\n|[^])|[^"\\\\\r\n])*"|<[^<>\r\n]*>|' + "<mod-name>(?:\\s*:\\s*<mod-name>)?|:\\s*<mod-name>".replace(/<mod-name>/g, (function () {
				return n
			})) + ")"), lookbehind: !0, greedy: !0, inside: {string: /^[<"][\s\S]+/, operator: /:/, punctuation: /\./}
		}, "raw-string": {pattern: /R"([^()\\ ]{0,16})\([\s\S]*?\)\1"/, alias: "string", greedy: !0}
	}), e.languages.insertBefore("cpp", "keyword", {
		"generic-function": {
			pattern: /\b(?!operator\b)[a-z_]\w*\s*<(?:[^<>]|<[^<>]*>)*>(?=\s*\()/i,
			inside: {function: /^\w+/, generic: {pattern: /<[\s\S]+/, alias: "class-name", inside: e.languages.cpp}}
		}
	}), e.languages.insertBefore("cpp", "operator", {
		"double-colon": {
			pattern: /::/,
			alias: "punctuation"
		}
	}), e.languages.insertBefore("cpp", "class-name", {
		"base-clause": {
			pattern: /(\b(?:class|struct)\s+\w+\s*:\s*)[^;{}"'\s]+(?:\s+[^;{}"'\s]+)*(?=\s*[;{])/,
			lookbehind: !0,
			greedy: !0,
			inside: e.languages.extend("cpp", {})
		}
	}), e.languages.insertBefore("inside", "double-colon", {"class-name": /\b[a-z_]\w*\b(?!\s*::)/i}, e.languages.cpp["base-clause"])
}(Prism);
Prism.languages.cmake = {
	comment: /#.*/,
	string: {
		pattern: /"(?:[^\\"]|\\.)*"/,
		greedy: !0,
		inside: {
			interpolation: {
				pattern: /\$\{(?:[^{}$]|\$\{[^{}$]*\})*\}/,
				inside: {punctuation: /\$\{|\}/, variable: /\w+/}
			}
		}
	},
	variable: /\b(?:CMAKE_\w+|\w+_(?:(?:BINARY|SOURCE)_DIR|DESCRIPTION|HOMEPAGE_URL|ROOT|VERSION(?:_MAJOR|_MINOR|_PATCH|_TWEAK)?)|(?:ANDROID|APPLE|BORLAND|BUILD_SHARED_LIBS|CACHE|CPACK_(?:ABSOLUTE_DESTINATION_FILES|COMPONENT_INCLUDE_TOPLEVEL_DIRECTORY|ERROR_ON_ABSOLUTE_INSTALL_DESTINATION|INCLUDE_TOPLEVEL_DIRECTORY|INSTALL_DEFAULT_DIRECTORY_PERMISSIONS|INSTALL_SCRIPT|PACKAGING_INSTALL_PREFIX|SET_DESTDIR|WARN_ON_ABSOLUTE_INSTALL_DESTINATION)|CTEST_(?:BINARY_DIRECTORY|BUILD_COMMAND|BUILD_NAME|BZR_COMMAND|BZR_UPDATE_OPTIONS|CHANGE_ID|CHECKOUT_COMMAND|CONFIGURATION_TYPE|CONFIGURE_COMMAND|COVERAGE_COMMAND|COVERAGE_EXTRA_FLAGS|CURL_OPTIONS|CUSTOM_(?:COVERAGE_EXCLUDE|ERROR_EXCEPTION|ERROR_MATCH|ERROR_POST_CONTEXT|ERROR_PRE_CONTEXT|MAXIMUM_FAILED_TEST_OUTPUT_SIZE|MAXIMUM_NUMBER_OF_(?:ERRORS|WARNINGS)|MAXIMUM_PASSED_TEST_OUTPUT_SIZE|MEMCHECK_IGNORE|POST_MEMCHECK|POST_TEST|PRE_MEMCHECK|PRE_TEST|TESTS_IGNORE|WARNING_EXCEPTION|WARNING_MATCH)|CVS_CHECKOUT|CVS_COMMAND|CVS_UPDATE_OPTIONS|DROP_LOCATION|DROP_METHOD|DROP_SITE|DROP_SITE_CDASH|DROP_SITE_PASSWORD|DROP_SITE_USER|EXTRA_COVERAGE_GLOB|GIT_COMMAND|GIT_INIT_SUBMODULES|GIT_UPDATE_CUSTOM|GIT_UPDATE_OPTIONS|HG_COMMAND|HG_UPDATE_OPTIONS|LABELS_FOR_SUBPROJECTS|MEMORYCHECK_(?:COMMAND|COMMAND_OPTIONS|SANITIZER_OPTIONS|SUPPRESSIONS_FILE|TYPE)|NIGHTLY_START_TIME|P4_CLIENT|P4_COMMAND|P4_OPTIONS|P4_UPDATE_OPTIONS|RUN_CURRENT_SCRIPT|SCP_COMMAND|SITE|SOURCE_DIRECTORY|SUBMIT_URL|SVN_COMMAND|SVN_OPTIONS|SVN_UPDATE_OPTIONS|TEST_LOAD|TEST_TIMEOUT|TRIGGER_SITE|UPDATE_COMMAND|UPDATE_OPTIONS|UPDATE_VERSION_ONLY|USE_LAUNCHERS)|CYGWIN|ENV|EXECUTABLE_OUTPUT_PATH|GHS-MULTI|IOS|LIBRARY_OUTPUT_PATH|MINGW|MSVC(?:10|11|12|14|60|70|71|80|90|_IDE|_TOOLSET_VERSION|_VERSION)?|MSYS|PROJECT_NAME|UNIX|WIN32|WINCE|WINDOWS_PHONE|WINDOWS_STORE|XCODE))\b/,
	property: /\b(?:cxx_\w+|(?:ARCHIVE_OUTPUT_(?:DIRECTORY|NAME)|COMPILE_DEFINITIONS|COMPILE_PDB_NAME|COMPILE_PDB_OUTPUT_DIRECTORY|EXCLUDE_FROM_DEFAULT_BUILD|IMPORTED_(?:IMPLIB|LIBNAME|LINK_DEPENDENT_LIBRARIES|LINK_INTERFACE_LANGUAGES|LINK_INTERFACE_LIBRARIES|LINK_INTERFACE_MULTIPLICITY|LOCATION|NO_SONAME|OBJECTS|SONAME)|INTERPROCEDURAL_OPTIMIZATION|LIBRARY_OUTPUT_DIRECTORY|LIBRARY_OUTPUT_NAME|LINK_FLAGS|LINK_INTERFACE_LIBRARIES|LINK_INTERFACE_MULTIPLICITY|LOCATION|MAP_IMPORTED_CONFIG|OSX_ARCHITECTURES|OUTPUT_NAME|PDB_NAME|PDB_OUTPUT_DIRECTORY|RUNTIME_OUTPUT_DIRECTORY|RUNTIME_OUTPUT_NAME|STATIC_LIBRARY_FLAGS|VS_CSHARP|VS_DOTNET_REFERENCEPROP|VS_DOTNET_REFERENCE|VS_GLOBAL_SECTION_POST|VS_GLOBAL_SECTION_PRE|VS_GLOBAL|XCODE_ATTRIBUTE)_\w+|\w+_(?:CLANG_TIDY|COMPILER_LAUNCHER|CPPCHECK|CPPLINT|INCLUDE_WHAT_YOU_USE|OUTPUT_NAME|POSTFIX|VISIBILITY_PRESET)|ABSTRACT|ADDITIONAL_MAKE_CLEAN_FILES|ADVANCED|ALIASED_TARGET|ALLOW_DUPLICATE_CUSTOM_TARGETS|ANDROID_(?:ANT_ADDITIONAL_OPTIONS|API|API_MIN|ARCH|ASSETS_DIRECTORIES|GUI|JAR_DEPENDENCIES|NATIVE_LIB_DEPENDENCIES|NATIVE_LIB_DIRECTORIES|PROCESS_MAX|PROGUARD|PROGUARD_CONFIG_PATH|SECURE_PROPS_PATH|SKIP_ANT_STEP|STL_TYPE)|ARCHIVE_OUTPUT_DIRECTORY|ATTACHED_FILES|ATTACHED_FILES_ON_FAIL|AUTOGEN_(?:BUILD_DIR|ORIGIN_DEPENDS|PARALLEL|SOURCE_GROUP|TARGETS_FOLDER|TARGET_DEPENDS)|AUTOMOC|AUTOMOC_(?:COMPILER_PREDEFINES|DEPEND_FILTERS|EXECUTABLE|MACRO_NAMES|MOC_OPTIONS|SOURCE_GROUP|TARGETS_FOLDER)|AUTORCC|AUTORCC_EXECUTABLE|AUTORCC_OPTIONS|AUTORCC_SOURCE_GROUP|AUTOUIC|AUTOUIC_EXECUTABLE|AUTOUIC_OPTIONS|AUTOUIC_SEARCH_PATHS|BINARY_DIR|BUILDSYSTEM_TARGETS|BUILD_RPATH|BUILD_RPATH_USE_ORIGIN|BUILD_WITH_INSTALL_NAME_DIR|BUILD_WITH_INSTALL_RPATH|BUNDLE|BUNDLE_EXTENSION|CACHE_VARIABLES|CLEAN_NO_CUSTOM|COMMON_LANGUAGE_RUNTIME|COMPATIBLE_INTERFACE_(?:BOOL|NUMBER_MAX|NUMBER_MIN|STRING)|COMPILE_(?:DEFINITIONS|FEATURES|FLAGS|OPTIONS|PDB_NAME|PDB_OUTPUT_DIRECTORY)|COST|CPACK_DESKTOP_SHORTCUTS|CPACK_NEVER_OVERWRITE|CPACK_PERMANENT|CPACK_STARTUP_SHORTCUTS|CPACK_START_MENU_SHORTCUTS|CPACK_WIX_ACL|CROSSCOMPILING_EMULATOR|CUDA_EXTENSIONS|CUDA_PTX_COMPILATION|CUDA_RESOLVE_DEVICE_SYMBOLS|CUDA_SEPARABLE_COMPILATION|CUDA_STANDARD|CUDA_STANDARD_REQUIRED|CXX_EXTENSIONS|CXX_STANDARD|CXX_STANDARD_REQUIRED|C_EXTENSIONS|C_STANDARD|C_STANDARD_REQUIRED|DEBUG_CONFIGURATIONS|DEFINE_SYMBOL|DEFINITIONS|DEPENDS|DEPLOYMENT_ADDITIONAL_FILES|DEPLOYMENT_REMOTE_DIRECTORY|DISABLED|DISABLED_FEATURES|ECLIPSE_EXTRA_CPROJECT_CONTENTS|ECLIPSE_EXTRA_NATURES|ENABLED_FEATURES|ENABLED_LANGUAGES|ENABLE_EXPORTS|ENVIRONMENT|EXCLUDE_FROM_ALL|EXCLUDE_FROM_DEFAULT_BUILD|EXPORT_NAME|EXPORT_PROPERTIES|EXTERNAL_OBJECT|EchoString|FAIL_REGULAR_EXPRESSION|FIND_LIBRARY_USE_LIB32_PATHS|FIND_LIBRARY_USE_LIB64_PATHS|FIND_LIBRARY_USE_LIBX32_PATHS|FIND_LIBRARY_USE_OPENBSD_VERSIONING|FIXTURES_CLEANUP|FIXTURES_REQUIRED|FIXTURES_SETUP|FOLDER|FRAMEWORK|Fortran_FORMAT|Fortran_MODULE_DIRECTORY|GENERATED|GENERATOR_FILE_NAME|GENERATOR_IS_MULTI_CONFIG|GHS_INTEGRITY_APP|GHS_NO_SOURCE_GROUP_FILE|GLOBAL_DEPENDS_DEBUG_MODE|GLOBAL_DEPENDS_NO_CYCLES|GNUtoMS|HAS_CXX|HEADER_FILE_ONLY|HELPSTRING|IMPLICIT_DEPENDS_INCLUDE_TRANSFORM|IMPORTED|IMPORTED_(?:COMMON_LANGUAGE_RUNTIME|CONFIGURATIONS|GLOBAL|IMPLIB|LIBNAME|LINK_DEPENDENT_LIBRARIES|LINK_INTERFACE_(?:LANGUAGES|LIBRARIES|MULTIPLICITY)|LOCATION|NO_SONAME|OBJECTS|SONAME)|IMPORT_PREFIX|IMPORT_SUFFIX|INCLUDE_DIRECTORIES|INCLUDE_REGULAR_EXPRESSION|INSTALL_NAME_DIR|INSTALL_RPATH|INSTALL_RPATH_USE_LINK_PATH|INTERFACE_(?:AUTOUIC_OPTIONS|COMPILE_DEFINITIONS|COMPILE_FEATURES|COMPILE_OPTIONS|INCLUDE_DIRECTORIES|LINK_DEPENDS|LINK_DIRECTORIES|LINK_LIBRARIES|LINK_OPTIONS|POSITION_INDEPENDENT_CODE|SOURCES|SYSTEM_INCLUDE_DIRECTORIES)|INTERPROCEDURAL_OPTIMIZATION|IN_TRY_COMPILE|IOS_INSTALL_COMBINED|JOB_POOLS|JOB_POOL_COMPILE|JOB_POOL_LINK|KEEP_EXTENSION|LABELS|LANGUAGE|LIBRARY_OUTPUT_DIRECTORY|LINKER_LANGUAGE|LINK_(?:DEPENDS|DEPENDS_NO_SHARED|DIRECTORIES|FLAGS|INTERFACE_LIBRARIES|INTERFACE_MULTIPLICITY|LIBRARIES|OPTIONS|SEARCH_END_STATIC|SEARCH_START_STATIC|WHAT_YOU_USE)|LISTFILE_STACK|LOCATION|MACOSX_BUNDLE|MACOSX_BUNDLE_INFO_PLIST|MACOSX_FRAMEWORK_INFO_PLIST|MACOSX_PACKAGE_LOCATION|MACOSX_RPATH|MACROS|MANUALLY_ADDED_DEPENDENCIES|MEASUREMENT|MODIFIED|NAME|NO_SONAME|NO_SYSTEM_FROM_IMPORTED|OBJECT_DEPENDS|OBJECT_OUTPUTS|OSX_ARCHITECTURES|OUTPUT_NAME|PACKAGES_FOUND|PACKAGES_NOT_FOUND|PARENT_DIRECTORY|PASS_REGULAR_EXPRESSION|PDB_NAME|PDB_OUTPUT_DIRECTORY|POSITION_INDEPENDENT_CODE|POST_INSTALL_SCRIPT|PREDEFINED_TARGETS_FOLDER|PREFIX|PRE_INSTALL_SCRIPT|PRIVATE_HEADER|PROCESSORS|PROCESSOR_AFFINITY|PROJECT_LABEL|PUBLIC_HEADER|REPORT_UNDEFINED_PROPERTIES|REQUIRED_FILES|RESOURCE|RESOURCE_LOCK|RULE_LAUNCH_COMPILE|RULE_LAUNCH_CUSTOM|RULE_LAUNCH_LINK|RULE_MESSAGES|RUNTIME_OUTPUT_DIRECTORY|RUN_SERIAL|SKIP_AUTOGEN|SKIP_AUTOMOC|SKIP_AUTORCC|SKIP_AUTOUIC|SKIP_BUILD_RPATH|SKIP_RETURN_CODE|SOURCES|SOURCE_DIR|SOVERSION|STATIC_LIBRARY_FLAGS|STATIC_LIBRARY_OPTIONS|STRINGS|SUBDIRECTORIES|SUFFIX|SYMBOLIC|TARGET_ARCHIVES_MAY_BE_SHARED_LIBS|TARGET_MESSAGES|TARGET_SUPPORTS_SHARED_LIBS|TESTS|TEST_INCLUDE_FILE|TEST_INCLUDE_FILES|TIMEOUT|TIMEOUT_AFTER_MATCH|TYPE|USE_FOLDERS|VALUE|VARIABLES|VERSION|VISIBILITY_INLINES_HIDDEN|VS_(?:CONFIGURATION_TYPE|COPY_TO_OUT_DIR|DEBUGGER_(?:COMMAND|COMMAND_ARGUMENTS|ENVIRONMENT|WORKING_DIRECTORY)|DEPLOYMENT_CONTENT|DEPLOYMENT_LOCATION|DOTNET_REFERENCES|DOTNET_REFERENCES_COPY_LOCAL|INCLUDE_IN_VSIX|IOT_STARTUP_TASK|KEYWORD|RESOURCE_GENERATOR|SCC_AUXPATH|SCC_LOCALPATH|SCC_PROJECTNAME|SCC_PROVIDER|SDK_REFERENCES|SHADER_(?:DISABLE_OPTIMIZATIONS|ENABLE_DEBUG|ENTRYPOINT|FLAGS|MODEL|OBJECT_FILE_NAME|OUTPUT_HEADER_FILE|TYPE|VARIABLE_NAME)|STARTUP_PROJECT|TOOL_OVERRIDE|USER_PROPS|WINRT_COMPONENT|WINRT_EXTENSIONS|WINRT_REFERENCES|XAML_TYPE)|WILL_FAIL|WIN32_EXECUTABLE|WINDOWS_EXPORT_ALL_SYMBOLS|WORKING_DIRECTORY|WRAP_EXCLUDE|XCODE_(?:EMIT_EFFECTIVE_PLATFORM_NAME|EXPLICIT_FILE_TYPE|FILE_ATTRIBUTES|LAST_KNOWN_FILE_TYPE|PRODUCT_TYPE|SCHEME_(?:ADDRESS_SANITIZER|ADDRESS_SANITIZER_USE_AFTER_RETURN|ARGUMENTS|DISABLE_MAIN_THREAD_CHECKER|DYNAMIC_LIBRARY_LOADS|DYNAMIC_LINKER_API_USAGE|ENVIRONMENT|EXECUTABLE|GUARD_MALLOC|MAIN_THREAD_CHECKER_STOP|MALLOC_GUARD_EDGES|MALLOC_SCRIBBLE|MALLOC_STACK|THREAD_SANITIZER(?:_STOP)?|UNDEFINED_BEHAVIOUR_SANITIZER(?:_STOP)?|ZOMBIE_OBJECTS))|XCTEST)\b/,
	keyword: /\b(?:add_compile_definitions|add_compile_options|add_custom_command|add_custom_target|add_definitions|add_dependencies|add_executable|add_library|add_link_options|add_subdirectory|add_test|aux_source_directory|break|build_command|build_name|cmake_host_system_information|cmake_minimum_required|cmake_parse_arguments|cmake_policy|configure_file|continue|create_test_sourcelist|ctest_build|ctest_configure|ctest_coverage|ctest_empty_binary_directory|ctest_memcheck|ctest_read_custom_files|ctest_run_script|ctest_sleep|ctest_start|ctest_submit|ctest_test|ctest_update|ctest_upload|define_property|else|elseif|enable_language|enable_testing|endforeach|endfunction|endif|endmacro|endwhile|exec_program|execute_process|export|export_library_dependencies|file|find_file|find_library|find_package|find_path|find_program|fltk_wrap_ui|foreach|function|get_cmake_property|get_directory_property|get_filename_component|get_property|get_source_file_property|get_target_property|get_test_property|if|include|include_directories|include_external_msproject|include_guard|include_regular_expression|install|install_files|install_programs|install_targets|link_directories|link_libraries|list|load_cache|load_command|macro|make_directory|mark_as_advanced|math|message|option|output_required_files|project|qt_wrap_cpp|qt_wrap_ui|remove|remove_definitions|return|separate_arguments|set|set_directory_properties|set_property|set_source_files_properties|set_target_properties|set_tests_properties|site_name|source_group|string|subdir_depends|subdirs|target_compile_definitions|target_compile_features|target_compile_options|target_include_directories|target_link_directories|target_link_libraries|target_link_options|target_sources|try_compile|try_run|unset|use_mangled_mesa|utility_source|variable_requires|variable_watch|while|write_file)(?=\s*\()\b/,
	boolean: /\b(?:FALSE|OFF|ON|TRUE)\b/,
	namespace: /\b(?:INTERFACE|PRIVATE|PROPERTIES|PUBLIC|SHARED|STATIC|TARGET_OBJECTS)\b/,
	operator: /\b(?:AND|DEFINED|EQUAL|GREATER|LESS|MATCHES|NOT|OR|STREQUAL|STRGREATER|STRLESS|VERSION_EQUAL|VERSION_GREATER|VERSION_LESS)\b/,
	inserted: {pattern: /\b\w+::\w+\b/, alias: "class-name"},
	number: /\b\d+(?:\.\d+)*\b/,
	function: /\b[a-z_]\w*(?=\s*\()\b/i,
	punctuation: /[()>}]|\$[<{]/
};
Prism.languages.csv = {value: /[^\r\n,"]+|"(?:[^"]|"")*"(?!")/, punctuation: /,/};
Prism.languages.git = {
	comment: /^#.*/m,
	deleted: /^[-–].*/m,
	inserted: /^\+.*/m,
	string: /("|')(?:\\.|(?!\1)[^\\\r\n])*\1/,
	command: {pattern: /^.*\$ git .*$/m, inside: {parameter: /\s--?\w+/}},
	coord: /^@@.*@@$/m,
	"commit-sha1": /^commit \w{40}$/m
};
!function (e) {
	var n = /\b(?:abstract|assert|boolean|break|byte|case|catch|char|class|const|continue|default|do|double|else|enum|exports|extends|final|finally|float|for|goto|if|implements|import|instanceof|int|interface|long|module|native|new|non-sealed|null|open|opens|package|permits|private|protected|provides|public|record(?!\s*[(){}[\]<>=%~.:,;?+\-*/&|^])|requires|return|sealed|short|static|strictfp|super|switch|synchronized|this|throw|throws|to|transient|transitive|try|uses|var|void|volatile|while|with|yield)\b/,
		t = "(?:[a-z]\\w*\\s*\\.\\s*)*(?:[A-Z]\\w*\\s*\\.\\s*)*", s = {
			pattern: RegExp("(^|[^\\w.])" + t + "[A-Z](?:[\\d_A-Z]*[a-z]\\w*)?\\b"),
			lookbehind: !0,
			inside: {
				namespace: {pattern: /^[a-z]\w*(?:\s*\.\s*[a-z]\w*)*(?:\s*\.)?/, inside: {punctuation: /\./}},
				punctuation: /\./
			}
		};
	e.languages.java = e.languages.extend("clike", {
		string: {
			pattern: /(^|[^\\])"(?:\\.|[^"\\\r\n])*"/,
			lookbehind: !0,
			greedy: !0
		},
		"class-name": [s, {
			pattern: RegExp("(^|[^\\w.])" + t + "[A-Z]\\w*(?=\\s+\\w+\\s*[;,=()]|\\s*(?:\\[[\\s,]*\\]\\s*)?::\\s*new\\b)"),
			lookbehind: !0,
			inside: s.inside
		}, {
			pattern: RegExp("(\\b(?:class|enum|extends|implements|instanceof|interface|new|record|throws)\\s+)" + t + "[A-Z]\\w*\\b"),
			lookbehind: !0,
			inside: s.inside
		}],
		keyword: n,
		function: [e.languages.clike.function, {pattern: /(::\s*)[a-z_]\w*/, lookbehind: !0}],
		number: /\b0b[01][01_]*L?\b|\b0x(?:\.[\da-f_p+-]+|[\da-f_]+(?:\.[\da-f_p+-]+)?)\b|(?:\b\d[\d_]*(?:\.[\d_]*)?|\B\.\d[\d_]*)(?:e[+-]?\d[\d_]*)?[dfl]?/i,
		operator: {pattern: /(^|[^.])(?:<<=?|>>>?=?|->|--|\+\+|&&|\|\||::|[?:~]|[-+*/%&|^!=<>]=?)/m, lookbehind: !0},
		constant: /\b[A-Z][A-Z_\d]+\b/
	}), e.languages.insertBefore("java", "string", {
		"triple-quoted-string": {
			pattern: /"""[ \t]*[\r\n](?:(?:"|"")?(?:\\.|[^"\\]))*"""/,
			greedy: !0,
			alias: "string"
		}, char: {pattern: /'(?:\\.|[^'\\\r\n]){1,6}'/, greedy: !0}
	}), e.languages.insertBefore("java", "class-name", {
		annotation: {
			pattern: /(^|[^.])@\w+(?:\s*\.\s*\w+)*/,
			lookbehind: !0,
			alias: "punctuation"
		},
		generics: {
			pattern: /<(?:[\w\s,.?]|&(?!&)|<(?:[\w\s,.?]|&(?!&)|<(?:[\w\s,.?]|&(?!&)|<(?:[\w\s,.?]|&(?!&))*>)*>)*>)*>/,
			inside: {"class-name": s, keyword: n, punctuation: /[<>(),.:]/, operator: /[?&|]/}
		},
		import: [{
			pattern: RegExp("(\\bimport\\s+)" + t + "(?:[A-Z]\\w*|\\*)(?=\\s*;)"),
			lookbehind: !0,
			inside: {namespace: s.inside.namespace, punctuation: /\./, operator: /\*/, "class-name": /\w+/}
		}, {
			pattern: RegExp("(\\bimport\\s+static\\s+)" + t + "(?:\\w+|\\*)(?=\\s*;)"),
			lookbehind: !0,
			alias: "static",
			inside: {
				namespace: s.inside.namespace,
				static: /\b\w+$/,
				punctuation: /\./,
				operator: /\*/,
				"class-name": /\w+/
			}
		}],
		namespace: {
			pattern: RegExp("(\\b(?:exports|import(?:\\s+static)?|module|open|opens|package|provides|requires|to|transitive|uses|with)\\s+)(?!<keyword>)[a-z]\\w*(?:\\.[a-z]\\w*)*\\.?".replace(/<keyword>/g, (function () {
				return n.source
			}))), lookbehind: !0, inside: {punctuation: /\./}
		}
	})
}(Prism);
!function (n) {
	n.languages.kotlin = n.languages.extend("clike", {
		keyword: {
			pattern: /(^|[^.])\b(?:abstract|actual|annotation|as|break|by|catch|class|companion|const|constructor|continue|crossinline|data|do|dynamic|else|enum|expect|external|final|finally|for|fun|get|if|import|in|infix|init|inline|inner|interface|internal|is|lateinit|noinline|null|object|open|operator|out|override|package|private|protected|public|reified|return|sealed|set|super|suspend|tailrec|this|throw|to|try|typealias|val|var|vararg|when|where|while)\b/,
			lookbehind: !0
		},
		function: [{
			pattern: /(?:`[^\r\n`]+`|\b\w+)(?=\s*\()/,
			greedy: !0
		}, {pattern: /(\.)(?:`[^\r\n`]+`|\w+)(?=\s*\{)/, lookbehind: !0, greedy: !0}],
		number: /\b(?:0[xX][\da-fA-F]+(?:_[\da-fA-F]+)*|0[bB][01]+(?:_[01]+)*|\d+(?:_\d+)*(?:\.\d+(?:_\d+)*)?(?:[eE][+-]?\d+(?:_\d+)*)?[fFL]?)\b/,
		operator: /\+[+=]?|-[-=>]?|==?=?|!(?:!|==?)?|[\/*%<>]=?|[?:]:?|\.\.|&&|\|\||\b(?:and|inv|or|shl|shr|ushr|xor)\b/
	}), delete n.languages.kotlin["class-name"];
	var e = {
		"interpolation-punctuation": {pattern: /^\$\{?|\}$/, alias: "punctuation"},
		expression: {pattern: /[\s\S]+/, inside: n.languages.kotlin}
	};
	n.languages.insertBefore("kotlin", "string", {
		"string-literal": [{
			pattern: /"""(?:[^$]|\$(?:(?!\{)|\{[^{}]*\}))*?"""/,
			alias: "multiline",
			inside: {interpolation: {pattern: /\$(?:[a-z_]\w*|\{[^{}]*\})/i, inside: e}, string: /[\s\S]+/}
		}, {
			pattern: /"(?:[^"\\\r\n$]|\\.|\$(?:(?!\{)|\{[^{}]*\}))*"/,
			alias: "singleline",
			inside: {
				interpolation: {
					pattern: /((?:^|[^\\])(?:\\{2})*)\$(?:[a-z_]\w*|\{[^{}]*\})/i,
					lookbehind: !0,
					inside: e
				}, string: /[\s\S]+/
			}
		}], char: {pattern: /'(?:[^'\\\r\n]|\\(?:.|u[a-fA-F0-9]{0,4}))'/, greedy: !0}
	}), delete n.languages.kotlin.string, n.languages.insertBefore("kotlin", "keyword", {
		annotation: {
			pattern: /\B@(?:\w+:)?(?:[A-Z]\w*|\[[^\]]+\])/,
			alias: "builtin"
		}
	}), n.languages.insertBefore("kotlin", "function", {
		label: {
			pattern: /\b\w+@|@\w+\b/,
			alias: "symbol"
		}
	}), n.languages.kt = n.languages.kotlin, n.languages.kts = n.languages.kotlin
}(Prism);
!function (a) {
	var e = /\\(?:[^a-z()[\]]|[a-z*]+)/i, n = {"equation-command": {pattern: e, alias: "regex"}};
	a.languages.latex = {
		comment: /%.*/,
		cdata: {pattern: /(\\begin\{((?:lstlisting|verbatim)\*?)\})[\s\S]*?(?=\\end\{\2\})/, lookbehind: !0},
		equation: [{
			pattern: /\$\$(?:\\[\s\S]|[^\\$])+\$\$|\$(?:\\[\s\S]|[^\\$])+\$|\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]/,
			inside: n,
			alias: "string"
		}, {
			pattern: /(\\begin\{((?:align|eqnarray|equation|gather|math|multline)\*?)\})[\s\S]*?(?=\\end\{\2\})/,
			lookbehind: !0,
			inside: n,
			alias: "string"
		}],
		keyword: {
			pattern: /(\\(?:begin|cite|documentclass|end|label|ref|usepackage)(?:\[[^\]]+\])?\{)[^}]+(?=\})/,
			lookbehind: !0
		},
		url: {pattern: /(\\url\{)[^}]+(?=\})/, lookbehind: !0},
		headline: {
			pattern: /(\\(?:chapter|frametitle|paragraph|part|section|subparagraph|subsection|subsubparagraph|subsubsection|subsubsubparagraph)\*?(?:\[[^\]]+\])?\{)[^}]+(?=\})/,
			lookbehind: !0,
			alias: "class-name"
		},
		function: {pattern: e, alias: "selector"},
		punctuation: /[[\]{}&]/
	}, a.languages.tex = a.languages.latex, a.languages.context = a.languages.latex
}(Prism);
Prism.languages.makefile = {
	comment: {pattern: /(^|[^\\])#(?:\\(?:\r\n|[\s\S])|[^\\\r\n])*/, lookbehind: !0},
	string: {pattern: /(["'])(?:\\(?:\r\n|[\s\S])|(?!\1)[^\\\r\n])*\1/, greedy: !0},
	"builtin-target": {pattern: /\.[A-Z][^:#=\s]+(?=\s*:(?!=))/, alias: "builtin"},
	target: {
		pattern: /^(?:[^:=\s]|[ \t]+(?![\s:]))+(?=\s*:(?!=))/m,
		alias: "symbol",
		inside: {variable: /\$+(?:(?!\$)[^(){}:#=\s]+|(?=[({]))/}
	},
	variable: /\$+(?:(?!\$)[^(){}:#=\s]+|\([@*%<^+?][DF]\)|(?=[({]))/,
	keyword: /-include\b|\b(?:define|else|endef|endif|export|ifn?def|ifn?eq|include|override|private|sinclude|undefine|unexport|vpath)\b/,
	function: {
		pattern: /(\()(?:abspath|addsuffix|and|basename|call|dir|error|eval|file|filter(?:-out)?|findstring|firstword|flavor|foreach|guile|if|info|join|lastword|load|notdir|or|origin|patsubst|realpath|shell|sort|strip|subst|suffix|value|warning|wildcard|word(?:list|s)?)(?=[ \t])/,
		lookbehind: !0
	},
	operator: /(?:::|[?:+!])?=|[|@]/,
	punctuation: /[:;(){}]/
};
!function (n) {
	function e(n) {
		return n = n.replace(/<inner>/g, (function () {
			return "(?:\\\\.|[^\\\\\n\r]|(?:\n|\r\n?)(?![\r\n]))"
		})), RegExp("((?:^|[^\\\\])(?:\\\\{2})*)(?:" + n + ")")
	}

	var t = "(?:\\\\.|``(?:[^`\r\n]|`(?!`))+``|`[^`\r\n]+`|[^\\\\|\r\n`])+",
		a = "\\|?__(?:\\|__)+\\|?(?:(?:\n|\r\n?)|(?![^]))".replace(/__/g, (function () {
			return t
		})), i = "\\|?[ \t]*:?-{3,}:?[ \t]*(?:\\|[ \t]*:?-{3,}:?[ \t]*)+\\|?(?:\n|\r\n?)";
	n.languages.markdown = n.languages.extend("markup", {}), n.languages.insertBefore("markdown", "prolog", {
		"front-matter-block": {
			pattern: /(^(?:\s*[\r\n])?)---(?!.)[\s\S]*?[\r\n]---(?!.)/,
			lookbehind: !0,
			greedy: !0,
			inside: {
				punctuation: /^---|---$/,
				"front-matter": {pattern: /\S+(?:\s+\S+)*/, alias: ["yaml", "language-yaml"], inside: n.languages.yaml}
			}
		},
		blockquote: {pattern: /^>(?:[\t ]*>)*/m, alias: "punctuation"},
		table: {
			pattern: RegExp("^" + a + i + "(?:" + a + ")*", "m"),
			inside: {
				"table-data-rows": {
					pattern: RegExp("^(" + a + i + ")(?:" + a + ")*$"),
					lookbehind: !0,
					inside: {"table-data": {pattern: RegExp(t), inside: n.languages.markdown}, punctuation: /\|/}
				},
				"table-line": {
					pattern: RegExp("^(" + a + ")" + i + "$"),
					lookbehind: !0,
					inside: {punctuation: /\||:?-{3,}:?/}
				},
				"table-header-row": {
					pattern: RegExp("^" + a + "$"),
					inside: {
						"table-header": {pattern: RegExp(t), alias: "important", inside: n.languages.markdown},
						punctuation: /\|/
					}
				}
			}
		},
		code: [{
			pattern: /((?:^|\n)[ \t]*\n|(?:^|\r\n?)[ \t]*\r\n?)(?: {4}|\t).+(?:(?:\n|\r\n?)(?: {4}|\t).+)*/,
			lookbehind: !0,
			alias: "keyword"
		}, {
			pattern: /^```[\s\S]*?^```$/m,
			greedy: !0,
			inside: {
				"code-block": {pattern: /^(```.*(?:\n|\r\n?))[\s\S]+?(?=(?:\n|\r\n?)^```$)/m, lookbehind: !0},
				"code-language": {pattern: /^(```).+/, lookbehind: !0},
				punctuation: /```/
			}
		}],
		title: [{
			pattern: /\S.*(?:\n|\r\n?)(?:==+|--+)(?=[ \t]*$)/m,
			alias: "important",
			inside: {punctuation: /==+$|--+$/}
		}, {pattern: /(^\s*)#.+/m, lookbehind: !0, alias: "important", inside: {punctuation: /^#+|#+$/}}],
		hr: {pattern: /(^\s*)([*-])(?:[\t ]*\2){2,}(?=\s*$)/m, lookbehind: !0, alias: "punctuation"},
		list: {pattern: /(^\s*)(?:[*+-]|\d+\.)(?=[\t ].)/m, lookbehind: !0, alias: "punctuation"},
		"url-reference": {
			pattern: /!?\[[^\]]+\]:[\t ]+(?:\S+|<(?:\\.|[^>\\])+>)(?:[\t ]+(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|\((?:\\.|[^)\\])*\)))?/,
			inside: {
				variable: {pattern: /^(!?\[)[^\]]+/, lookbehind: !0},
				string: /(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|\((?:\\.|[^)\\])*\))$/,
				punctuation: /^[\[\]!:]|[<>]/
			},
			alias: "url"
		},
		bold: {
			pattern: e("\\b__(?:(?!_)<inner>|_(?:(?!_)<inner>)+_)+__\\b|\\*\\*(?:(?!\\*)<inner>|\\*(?:(?!\\*)<inner>)+\\*)+\\*\\*"),
			lookbehind: !0,
			greedy: !0,
			inside: {content: {pattern: /(^..)[\s\S]+(?=..$)/, lookbehind: !0, inside: {}}, punctuation: /\*\*|__/}
		},
		italic: {
			pattern: e("\\b_(?:(?!_)<inner>|__(?:(?!_)<inner>)+__)+_\\b|\\*(?:(?!\\*)<inner>|\\*\\*(?:(?!\\*)<inner>)+\\*\\*)+\\*"),
			lookbehind: !0,
			greedy: !0,
			inside: {content: {pattern: /(^.)[\s\S]+(?=.$)/, lookbehind: !0, inside: {}}, punctuation: /[*_]/}
		},
		strike: {
			pattern: e("(~~?)(?:(?!~)<inner>)+\\2"),
			lookbehind: !0,
			greedy: !0,
			inside: {content: {pattern: /(^~~?)[\s\S]+(?=\1$)/, lookbehind: !0, inside: {}}, punctuation: /~~?/}
		},
		"code-snippet": {
			pattern: /(^|[^\\`])(?:``[^`\r\n]+(?:`[^`\r\n]+)*``(?!`)|`[^`\r\n]+`(?!`))/,
			lookbehind: !0,
			greedy: !0,
			alias: ["code", "keyword"]
		},
		url: {
			pattern: e('!?\\[(?:(?!\\])<inner>)+\\](?:\\([^\\s)]+(?:[\t ]+"(?:\\\\.|[^"\\\\])*")?\\)|[ \t]?\\[(?:(?!\\])<inner>)+\\])'),
			lookbehind: !0,
			greedy: !0,
			inside: {
				operator: /^!/,
				content: {pattern: /(^\[)[^\]]+(?=\])/, lookbehind: !0, inside: {}},
				variable: {pattern: /(^\][ \t]?\[)[^\]]+(?=\]$)/, lookbehind: !0},
				url: {pattern: /(^\]\()[^\s)]+/, lookbehind: !0},
				string: {pattern: /(^[ \t]+)"(?:\\.|[^"\\])*"(?=\)$)/, lookbehind: !0}
			}
		}
	}), ["url", "bold", "italic", "strike"].forEach((function (e) {
		["url", "bold", "italic", "strike", "code-snippet"].forEach((function (t) {
			e !== t && (n.languages.markdown[e].inside.content.inside[t] = n.languages.markdown[t])
		}))
	})), n.hooks.add("after-tokenize", (function (n) {
		"markdown" !== n.language && "md" !== n.language || function n(e) {
			if (e && "string" != typeof e) for (var t = 0, a = e.length; t < a; t++) {
				var i = e[t];
				if ("code" === i.type) {
					var r = i.content[1], o = i.content[3];
					if (r && o && "code-language" === r.type && "code-block" === o.type && "string" == typeof r.content) {
						var l = r.content.replace(/\b#/g, "sharp").replace(/\b\+\+/g, "pp"),
							s = "language-" + (l = (/[a-z][\w-]*/i.exec(l) || [""])[0].toLowerCase());
						o.alias ? "string" == typeof o.alias ? o.alias = [o.alias, s] : o.alias.push(s) : o.alias = [s]
					}
				} else n(i.content)
			}
		}(n.tokens)
	})), n.hooks.add("wrap", (function (e) {
		if ("code-block" === e.type) {
			for (var t = "", a = 0, i = e.classes.length; a < i; a++) {
				var s = e.classes[a], d = /language-(.+)/.exec(s);
				if (d) {
					t = d[1];
					break
				}
			}
			var p = n.languages[t];
			if (p) e.content = n.highlight(e.content.replace(r, "").replace(/&(\w{1,8}|#x?[\da-f]{1,8});/gi, (function (n, e) {
				var t;
				return "#" === (e = e.toLowerCase())[0] ? (t = "x" === e[1] ? parseInt(e.slice(2), 16) : Number(e.slice(1)), l(t)) : o[e] || n
			})), p, t); else if (t && "none" !== t && n.plugins.autoloader) {
				var u = "md-" + (new Date).valueOf() + "-" + Math.floor(1e16 * Math.random());
				e.attributes.id = u, n.plugins.autoloader.loadLanguages(t, (function () {
					var e = document.getElementById(u);
					e && (e.innerHTML = n.highlight(e.textContent, n.languages[t], t))
				}))
			}
		}
	}));
	var r = RegExp(n.languages.markup.tag.pattern.source, "gi"), o = {amp: "&", lt: "<", gt: ">", quot: '"'},
		l = String.fromCodePoint || String.fromCharCode;
	n.languages.md = n.languages.markdown
}(Prism);
Prism.languages.mermaid = {
	comment: {pattern: /%%.*/, greedy: !0},
	style: {
		pattern: /^([ \t]*(?:classDef|linkStyle|style)[ \t]+[\w$-]+[ \t]+)\w.*[^\s;]/m,
		lookbehind: !0,
		inside: {property: /\b\w[\w-]*(?=[ \t]*:)/, operator: /:/, punctuation: /,/}
	},
	"inter-arrow-label": {
		pattern: /([^<>ox.=-])(?:-[-.]|==)(?![<>ox.=-])[ \t]*(?:"[^"\r\n]*"|[^\s".=-](?:[^\r\n.=-]*[^\s.=-])?)[ \t]*(?:\.+->?|--+[->]|==+[=>])(?![<>ox.=-])/,
		lookbehind: !0,
		greedy: !0,
		inside: {
			arrow: {pattern: /(?:\.+->?|--+[->]|==+[=>])$/, alias: "operator"},
			label: {pattern: /^([\s\S]{2}[ \t]*)\S(?:[\s\S]*\S)?/, lookbehind: !0, alias: "property"},
			"arrow-head": {pattern: /^\S+/, alias: ["arrow", "operator"]}
		}
	},
	arrow: [{
		pattern: /(^|[^{}|o.-])[|}][|o](?:--|\.\.)[|o][|{](?![{}|o.-])/,
		lookbehind: !0,
		alias: "operator"
	}, {
		pattern: /(^|[^<>ox.=-])(?:[<ox](?:==+|--+|-\.*-)[>ox]?|(?:==+|--+|-\.*-)[>ox]|===+|---+|-\.+-)(?![<>ox.=-])/,
		lookbehind: !0,
		alias: "operator"
	}, {
		pattern: /(^|[^<>()x-])(?:--?(?:>>|[x>)])(?![<>()x])|(?:<<|[x<(])--?(?!-))/,
		lookbehind: !0,
		alias: "operator"
	}, {
		pattern: /(^|[^<>|*o.-])(?:[*o]--|--[*o]|<\|?(?:--|\.\.)|(?:--|\.\.)\|?>|--|\.\.)(?![<>|*o.-])/,
		lookbehind: !0,
		alias: "operator"
	}],
	label: {pattern: /(^|[^|<])\|(?:[^\r\n"|]|"[^"\r\n]*")+\|/, lookbehind: !0, greedy: !0, alias: "property"},
	text: {pattern: /(?:[(\[{]+|\b>)(?:[^\r\n"()\[\]{}]|"[^"\r\n]*")+(?:[)\]}]+|>)/, alias: "string"},
	string: {pattern: /"[^"\r\n]*"/, greedy: !0},
	annotation: {
		pattern: /<<(?:abstract|choice|enumeration|fork|interface|join|service)>>|\[\[(?:choice|fork|join)\]\]/i,
		alias: "important"
	},
	keyword: [{
		pattern: /(^[ \t]*)(?:action|callback|class|classDef|classDiagram|click|direction|erDiagram|flowchart|gantt|gitGraph|graph|journey|link|linkStyle|pie|requirementDiagram|sequenceDiagram|stateDiagram|stateDiagram-v2|style|subgraph)(?![\w$-])/m,
		lookbehind: !0,
		greedy: !0
	}, {
		pattern: /(^[ \t]*)(?:activate|alt|and|as|autonumber|deactivate|else|end(?:[ \t]+note)?|loop|opt|par|participant|rect|state|note[ \t]+(?:over|(?:left|right)[ \t]+of))(?![\w$-])/im,
		lookbehind: !0,
		greedy: !0
	}],
	entity: /#[a-z0-9]+;/,
	operator: {pattern: /(\w[ \t]*)&(?=[ \t]*\w)|:::|:/, lookbehind: !0},
	punctuation: /[(){};]/
};
!function (e) {
	var i = e.languages.powershell = {
		comment: [{pattern: /(^|[^`])<#[\s\S]*?#>/, lookbehind: !0}, {pattern: /(^|[^`])#.*/, lookbehind: !0}],
		string: [{pattern: /"(?:`[\s\S]|[^`"])*"/, greedy: !0, inside: null}, {pattern: /'(?:[^']|'')*'/, greedy: !0}],
		namespace: /\[[a-z](?:\[(?:\[[^\]]*\]|[^\[\]])*\]|[^\[\]])*\]/i,
		boolean: /\$(?:false|true)\b/i,
		variable: /\$\w+\b/,
		function: [/\b(?:Add|Approve|Assert|Backup|Block|Checkpoint|Clear|Close|Compare|Complete|Compress|Confirm|Connect|Convert|ConvertFrom|ConvertTo|Copy|Debug|Deny|Disable|Disconnect|Dismount|Edit|Enable|Enter|Exit|Expand|Export|Find|ForEach|Format|Get|Grant|Group|Hide|Import|Initialize|Install|Invoke|Join|Limit|Lock|Measure|Merge|Move|New|Open|Optimize|Out|Ping|Pop|Protect|Publish|Push|Read|Receive|Redo|Register|Remove|Rename|Repair|Request|Reset|Resize|Resolve|Restart|Restore|Resume|Revoke|Save|Search|Select|Send|Set|Show|Skip|Sort|Split|Start|Step|Stop|Submit|Suspend|Switch|Sync|Tee|Test|Trace|Unblock|Undo|Uninstall|Unlock|Unprotect|Unpublish|Unregister|Update|Use|Wait|Watch|Where|Write)-[a-z]+\b/i, /\b(?:ac|cat|chdir|clc|cli|clp|clv|compare|copy|cp|cpi|cpp|cvpa|dbp|del|diff|dir|ebp|echo|epal|epcsv|epsn|erase|fc|fl|ft|fw|gal|gbp|gc|gci|gcs|gdr|gi|gl|gm|gp|gps|group|gsv|gu|gv|gwmi|iex|ii|ipal|ipcsv|ipsn|irm|iwmi|iwr|kill|lp|ls|measure|mi|mount|move|mp|mv|nal|ndr|ni|nv|ogv|popd|ps|pushd|pwd|rbp|rd|rdr|ren|ri|rm|rmdir|rni|rnp|rp|rv|rvpa|rwmi|sal|saps|sasv|sbp|sc|select|set|shcm|si|sl|sleep|sls|sort|sp|spps|spsv|start|sv|swmi|tee|trcm|type|write)\b/i],
		keyword: /\b(?:Begin|Break|Catch|Class|Continue|Data|Define|Do|DynamicParam|Else|ElseIf|End|Exit|Filter|Finally|For|ForEach|From|Function|If|InlineScript|Parallel|Param|Process|Return|Sequence|Switch|Throw|Trap|Try|Until|Using|Var|While|Workflow)\b/i,
		operator: {
			pattern: /(^|\W)(?:!|-(?:b?(?:and|x?or)|as|(?:Not)?(?:Contains|In|Like|Match)|eq|ge|gt|is(?:Not)?|Join|le|lt|ne|not|Replace|sh[lr])\b|-[-=]?|\+[+=]?|[*\/%]=?)/i,
			lookbehind: !0
		},
		punctuation: /[|{}[\];(),.]/
	};
	i.string[0].inside = {
		function: {
			pattern: /(^|[^`])\$\((?:\$\([^\r\n()]*\)|(?!\$\()[^\r\n)])*\)/,
			lookbehind: !0,
			inside: i
		}, boolean: i.boolean, variable: i.variable
	}
}(Prism);
Prism.languages.python = {
	comment: {pattern: /(^|[^\\])#.*/, lookbehind: !0, greedy: !0},
	"string-interpolation": {
		pattern: /(?:f|fr|rf)(?:("""|''')[\s\S]*?\1|("|')(?:\\.|(?!\2)[^\\\r\n])*\2)/i,
		greedy: !0,
		inside: {
			interpolation: {
				pattern: /((?:^|[^{])(?:\{\{)*)\{(?!\{)(?:[^{}]|\{(?!\{)(?:[^{}]|\{(?!\{)(?:[^{}])+\})+\})+\}/,
				lookbehind: !0,
				inside: {
					"format-spec": {pattern: /(:)[^:(){}]+(?=\}$)/, lookbehind: !0},
					"conversion-option": {pattern: /![sra](?=[:}]$)/, alias: "punctuation"},
					rest: null
				}
			}, string: /[\s\S]+/
		}
	},
	"triple-quoted-string": {pattern: /(?:[rub]|br|rb)?("""|''')[\s\S]*?\1/i, greedy: !0, alias: "string"},
	string: {pattern: /(?:[rub]|br|rb)?("|')(?:\\.|(?!\1)[^\\\r\n])*\1/i, greedy: !0},
	function: {pattern: /((?:^|\s)def[ \t]+)[a-zA-Z_]\w*(?=\s*\()/g, lookbehind: !0},
	"class-name": {pattern: /(\bclass\s+)\w+/i, lookbehind: !0},
	decorator: {
		pattern: /(^[\t ]*)@\w+(?:\.\w+)*/m,
		lookbehind: !0,
		alias: ["annotation", "punctuation"],
		inside: {punctuation: /\./}
	},
	keyword: /\b(?:_(?=\s*:)|and|as|assert|async|await|break|case|class|continue|def|del|elif|else|except|exec|finally|for|from|global|if|import|in|is|lambda|match|nonlocal|not|or|pass|print|raise|return|try|while|with|yield)\b/,
	builtin: /\b(?:__import__|abs|all|any|apply|ascii|basestring|bin|bool|buffer|bytearray|bytes|callable|chr|classmethod|cmp|coerce|compile|complex|delattr|dict|dir|divmod|enumerate|eval|execfile|file|filter|float|format|frozenset|getattr|globals|hasattr|hash|help|hex|id|input|int|intern|isinstance|issubclass|iter|len|list|locals|long|map|max|memoryview|min|next|object|oct|open|ord|pow|property|range|raw_input|reduce|reload|repr|reversed|round|set|setattr|slice|sorted|staticmethod|str|sum|super|tuple|type|unichr|unicode|vars|xrange|zip)\b/,
	boolean: /\b(?:False|None|True)\b/,
	number: /\b0(?:b(?:_?[01])+|o(?:_?[0-7])+|x(?:_?[a-f0-9])+)\b|(?:\b\d+(?:_\d+)*(?:\.(?:\d+(?:_\d+)*)?)?|\B\.\d+(?:_\d+)*)(?:e[+-]?\d+(?:_\d+)*)?j?(?!\w)/i,
	operator: /[-+%=]=?|!=|:=|\*\*?=?|\/\/?=?|<[<=>]?|>[=>]?|[&|^~]/,
	punctuation: /[{}[\];(),.:]/
}, Prism.languages.python["string-interpolation"].inside.interpolation.inside.rest = Prism.languages.python, Prism.languages.py = Prism.languages.python;
!function (a) {
	var e = {pattern: /\\[\\(){}[\]^$+*?|.]/, alias: "escape"},
		n = /\\(?:x[\da-fA-F]{2}|u[\da-fA-F]{4}|u\{[\da-fA-F]+\}|0[0-7]{0,2}|[123][0-7]{2}|c[a-zA-Z]|.)/,
		t = "(?:[^\\\\-]|" + n.source + ")", s = RegExp(t + "-" + t),
		i = {pattern: /(<|')[^<>']+(?=[>']$)/, lookbehind: !0, alias: "variable"};
	a.languages.regex = {
		"char-class": {
			pattern: /((?:^|[^\\])(?:\\\\)*)\[(?:[^\\\]]|\\[\s\S])*\]/,
			lookbehind: !0,
			inside: {
				"char-class-negation": {pattern: /(^\[)\^/, lookbehind: !0, alias: "operator"},
				"char-class-punctuation": {pattern: /^\[|\]$/, alias: "punctuation"},
				range: {pattern: s, inside: {escape: n, "range-punctuation": {pattern: /-/, alias: "operator"}}},
				"special-escape": e,
				"char-set": {pattern: /\\[wsd]|\\p\{[^{}]+\}/i, alias: "class-name"},
				escape: n
			}
		},
		"special-escape": e,
		"char-set": {pattern: /\.|\\[wsd]|\\p\{[^{}]+\}/i, alias: "class-name"},
		backreference: [{pattern: /\\(?![123][0-7]{2})[1-9]/, alias: "keyword"}, {
			pattern: /\\k<[^<>']+>/,
			alias: "keyword",
			inside: {"group-name": i}
		}],
		anchor: {pattern: /[$^]|\\[ABbGZz]/, alias: "function"},
		escape: n,
		group: [{
			pattern: /\((?:\?(?:<[^<>']+>|'[^<>']+'|[>:]|<?[=!]|[idmnsuxU]+(?:-[idmnsuxU]+)?:?))?/,
			alias: "punctuation",
			inside: {"group-name": i}
		}, {pattern: /\)/, alias: "punctuation"}],
		quantifier: {pattern: /(?:[+*?]|\{\d+(?:,\d*)?\})[?+]?/, alias: "number"},
		alternation: {pattern: /\|/, alias: "keyword"}
	}
}(Prism);
Prism.languages.swift = {
	comment: {
		pattern: /(^|[^\\:])(?:\/\/.*|\/\*(?:[^/*]|\/(?!\*)|\*(?!\/)|\/\*(?:[^*]|\*(?!\/))*\*\/)*\*\/)/,
		lookbehind: !0,
		greedy: !0
	},
	"string-literal": [{
		pattern: RegExp('(^|[^"#])(?:"(?:\\\\(?:\\((?:[^()]|\\([^()]*\\))*\\)|\r\n|[^(])|[^\\\\\r\n"])*"|"""(?:\\\\(?:\\((?:[^()]|\\([^()]*\\))*\\)|[^(])|[^\\\\"]|"(?!""))*""")(?!["#])'),
		lookbehind: !0,
		greedy: !0,
		inside: {
			interpolation: {pattern: /(\\\()(?:[^()]|\([^()]*\))*(?=\))/, lookbehind: !0, inside: null},
			"interpolation-punctuation": {pattern: /^\)|\\\($/, alias: "punctuation"},
			punctuation: /\\(?=[\r\n])/,
			string: /[\s\S]+/
		}
	}, {
		pattern: RegExp('(^|[^"#])(#+)(?:"(?:\\\\(?:#+\\((?:[^()]|\\([^()]*\\))*\\)|\r\n|[^#])|[^\\\\\r\n])*?"|"""(?:\\\\(?:#+\\((?:[^()]|\\([^()]*\\))*\\)|[^#])|[^\\\\])*?""")\\2'),
		lookbehind: !0,
		greedy: !0,
		inside: {
			interpolation: {pattern: /(\\#+\()(?:[^()]|\([^()]*\))*(?=\))/, lookbehind: !0, inside: null},
			"interpolation-punctuation": {pattern: /^\)|\\#+\($/, alias: "punctuation"},
			string: /[\s\S]+/
		}
	}],
	directive: {
		pattern: RegExp("#(?:(?:elseif|if)\\b(?:[ \t]*(?:![ \t]*)?(?:\\b\\w+\\b(?:[ \t]*\\((?:[^()]|\\([^()]*\\))*\\))?|\\((?:[^()]|\\([^()]*\\))*\\))(?:[ \t]*(?:&&|\\|\\|))?)+|(?:else|endif)\\b)"),
		alias: "property",
		inside: {
			"directive-name": /^#\w+/,
			boolean: /\b(?:false|true)\b/,
			number: /\b\d+(?:\.\d+)*\b/,
			operator: /!|&&|\|\||[<>]=?/,
			punctuation: /[(),]/
		}
	},
	literal: {
		pattern: /#(?:colorLiteral|column|dsohandle|file(?:ID|Literal|Path)?|function|imageLiteral|line)\b/,
		alias: "constant"
	},
	"other-directive": {pattern: /#\w+\b/, alias: "property"},
	attribute: {pattern: /@\w+/, alias: "atrule"},
	"function-definition": {pattern: /(\bfunc\s+)\w+/, lookbehind: !0, alias: "function"},
	label: {
		pattern: /\b(break|continue)\s+\w+|\b[a-zA-Z_]\w*(?=\s*:\s*(?:for|repeat|while)\b)/,
		lookbehind: !0,
		alias: "important"
	},
	keyword: /\b(?:Any|Protocol|Self|Type|actor|as|assignment|associatedtype|associativity|async|await|break|case|catch|class|continue|convenience|default|defer|deinit|didSet|do|dynamic|else|enum|extension|fallthrough|fileprivate|final|for|func|get|guard|higherThan|if|import|in|indirect|infix|init|inout|internal|is|isolated|lazy|left|let|lowerThan|mutating|none|nonisolated|nonmutating|open|operator|optional|override|postfix|precedencegroup|prefix|private|protocol|public|repeat|required|rethrows|return|right|safe|self|set|some|static|struct|subscript|super|switch|throw|throws|try|typealias|unowned|unsafe|var|weak|where|while|willSet)\b/,
	boolean: /\b(?:false|true)\b/,
	nil: {pattern: /\bnil\b/, alias: "constant"},
	"short-argument": /\$\d+\b/,
	omit: {pattern: /\b_\b/, alias: "keyword"},
	number: /\b(?:[\d_]+(?:\.[\de_]+)?|0x[a-f0-9_]+(?:\.[a-f0-9p_]+)?|0b[01_]+|0o[0-7_]+)\b/i,
	"class-name": /\b[A-Z](?:[A-Z_\d]*[a-z]\w*)?\b/,
	function: /\b[a-z_]\w*(?=\s*\()/i,
	constant: /\b(?:[A-Z_]{2,}|k[A-Z][A-Za-z_]+)\b/,
	operator: /[-+*/%=!<>&|^~?]+|\.[.\-+*/%=!<>&|^~?]+/,
	punctuation: /[{}[\]();,.:\\]/
}, Prism.languages.swift["string-literal"].forEach((function (e) {
	e.inside.interpolation.inside = Prism.languages.swift
}));
!function (e) {
	var n = /[*&][^\s[\]{},]+/, r = /!(?:<[\w\-%#;/?:@&=+$,.!~*'()[\]]+>|(?:[a-zA-Z\d-]*!)?[\w\-%#;/?:@&=+$.~*'()]+)?/,
		t = "(?:" + r.source + "(?:[ \t]+" + n.source + ")?|" + n.source + "(?:[ \t]+" + r.source + ")?)",
		a = "(?:[^\\s\\x00-\\x08\\x0e-\\x1f!\"#%&'*,\\-:>?@[\\]`{|}\\x7f-\\x84\\x86-\\x9f\\ud800-\\udfff\\ufffe\\uffff]|[?:-]<PLAIN>)(?:[ \t]*(?:(?![#:])<PLAIN>|:<PLAIN>))*".replace(/<PLAIN>/g, (function () {
			return "[^\\s\\x00-\\x08\\x0e-\\x1f,[\\]{}\\x7f-\\x84\\x86-\\x9f\\ud800-\\udfff\\ufffe\\uffff]"
		})), d = "\"(?:[^\"\\\\\r\n]|\\\\.)*\"|'(?:[^'\\\\\r\n]|\\\\.)*'";

	function o(e, n) {
		n = (n || "").replace(/m/g, "") + "m";
		var r = "([:\\-,[{]\\s*(?:\\s<<prop>>[ \t]+)?)(?:<<value>>)(?=[ \t]*(?:$|,|\\]|\\}|(?:[\r\n]\\s*)?#))".replace(/<<prop>>/g, (function () {
			return t
		})).replace(/<<value>>/g, (function () {
			return e
		}));
		return RegExp(r, n)
	}

	e.languages.yaml = {
		scalar: {
			pattern: RegExp("([\\-:]\\s*(?:\\s<<prop>>[ \t]+)?[|>])[ \t]*(?:((?:\r?\n|\r)[ \t]+)\\S[^\r\n]*(?:\\2[^\r\n]+)*)".replace(/<<prop>>/g, (function () {
				return t
			}))), lookbehind: !0, alias: "string"
		},
		comment: /#.*/,
		key: {
			pattern: RegExp("((?:^|[:\\-,[{\r\n?])[ \t]*(?:<<prop>>[ \t]+)?)<<key>>(?=\\s*:\\s)".replace(/<<prop>>/g, (function () {
				return t
			})).replace(/<<key>>/g, (function () {
				return "(?:" + a + "|" + d + ")"
			}))), lookbehind: !0, greedy: !0, alias: "atrule"
		},
		directive: {pattern: /(^[ \t]*)%.+/m, lookbehind: !0, alias: "important"},
		datetime: {
			pattern: o("\\d{4}-\\d\\d?-\\d\\d?(?:[tT]|[ \t]+)\\d\\d?:\\d{2}:\\d{2}(?:\\.\\d*)?(?:[ \t]*(?:Z|[-+]\\d\\d?(?::\\d{2})?))?|\\d{4}-\\d{2}-\\d{2}|\\d\\d?:\\d{2}(?::\\d{2}(?:\\.\\d*)?)?"),
			lookbehind: !0,
			alias: "number"
		},
		boolean: {pattern: o("false|true", "i"), lookbehind: !0, alias: "important"},
		null: {pattern: o("null|~", "i"), lookbehind: !0, alias: "important"},
		string: {pattern: o(d), lookbehind: !0, greedy: !0},
		number: {
			pattern: o("[+-]?(?:0x[\\da-f]+|0o[0-7]+|(?:\\d+(?:\\.\\d*)?|\\.\\d+)(?:e[+-]?\\d+)?|\\.inf|\\.nan)", "i"),
			lookbehind: !0
		},
		tag: r,
		important: n,
		punctuation: /---|[:[\]{}\-,|>?]|\.\.\./
	}, e.languages.yml = e.languages.yaml
}(Prism);
