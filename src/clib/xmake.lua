add_rules("mode.debug", "mode.release")

target("adder")
    set_kind("shared")
    add_files("*.c")
    
    if is_plat("windows") then
        add_defines("_WIN32")
    end

    after_build(function (target)
        import("core.project.config")
        local targetfile = target:targetfile()
        os.cp(targetfile, "../../pylibdemo/")
    end) 