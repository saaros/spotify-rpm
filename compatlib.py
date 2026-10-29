import json
import subprocess
import sys


def variadic_wrapper(lib, name, rettype, fixed):
    """Wrapper for a function taking one extra variadic argument.

    Only a single trailing argument is forwarded (as a pointer-sized value),
    which covers curl_easy_setopt() where the value is a long, a pointer or a
    curl_off_t depending on the option.
    """
    params = [f"{argtype} a_{idx}" for idx, argtype in enumerate(fixed)]
    names = [f"a_{idx}" for idx, _ in enumerate(fixed)]
    return f"""
                asm(".symver w__{name}, {name}@{lib['version']}");
                {rettype} w__{name} ({", ".join(params)}, ...) {{
                    static {rettype} (*s_{name})({", ".join(fixed)}, ...) = NULL;
                    va_list ap;
                    void *arg;
                    if (s_{name} == NULL) s_{name} = dlsym(RTLD_NEXT, "{name}");
                    va_start(ap, a_{len(fixed) - 1});
                    arg = va_arg(ap, void *);
                    va_end(ap);
                    return s_{name} ({", ".join(names)}, arg);
                }}
            """


def generate_source(lib):
    c_name = f"compat-{lib['name']}.c"
    m_name = f"compat-{lib['name']}.map"
    with open(c_name, "w") as fp:
        fp.write("""
                #define _GNU_SOURCE
                #include <dlfcn.h>
                #include <stdarg.h>
                #include <stddef.h>
        """)
        for header in lib["headers"]:
            fp.write(f"""
                #include <{header}>
            """)
        for name, (rettype, args) in sorted(lib["symbols"].items()):
            if args and args[-1] == "...":
                fp.write(variadic_wrapper(lib, name, rettype, args[:-1]))
                continue
            args_with_names = [f"{argtype} a_{idx}" for idx, argtype in enumerate(args)]
            arg_names = [f"a_{idx}" for idx, _ in enumerate(args)]
            fp.write(f"""
                asm(".symver w__{name}, {name}@{lib['version']}");
                {rettype} w__{name} ({", ".join(args_with_names)}) {{
                    static {rettype} (*s_{name})({", ".join(args)}) = NULL;
                    if (s_{name} == NULL) s_{name} = dlsym(RTLD_NEXT, "{name}");
                    return s_{name} ({", ".join(arg_names)});
                }}
            """)
    with open(m_name, "w") as fp:
        fp.write(f"""
            {lib['version']} {{
                global: *;
            }};
        """)

    cmd = [
        "gcc",
        "-shared",
        "-o", lib['name'],
        f"-Wl,--version-script,{m_name}",
        c_name,
        "-fPIC",
    ] + lib['libs']

    return cmd


def main(args):
    for name in args:
        with open(name, "r") as fp:
            lib = json.load(fp)
        cmd = generate_source(lib)
        subprocess.check_call(cmd)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
