typedef unsigned char   undefined;

typedef unsigned char    byte;
typedef unsigned char    dwfenc;
typedef unsigned int    dword;
typedef unsigned long    qword;
typedef unsigned int    uint;
typedef unsigned long    ulong;
typedef unsigned char    undefined1;
typedef unsigned int    undefined4;
typedef unsigned long    undefined8;
typedef unsigned short    word;
typedef struct eh_frame_hdr eh_frame_hdr, *Peh_frame_hdr;

struct eh_frame_hdr {
    byte eh_frame_hdr_version; // Exception Handler Frame Header Version
    dwfenc eh_frame_pointer_encoding; // Exception Handler Frame Pointer Encoding
    dwfenc eh_frame_desc_entry_count_encoding; // Encoding of # of Exception Handler FDEs
    dwfenc eh_frame_table_encoding; // Exception Handler Table Encoding
};

typedef struct fde_table_entry fde_table_entry, *Pfde_table_entry;

struct fde_table_entry {
    dword initial_loc; // Initial Location
    dword data_loc; // Data location
};

typedef ulong size_t;

typedef enum Elf_ProgramHeaderType {
    PT_DYNAMIC=2,
    PT_GNU_EH_FRAME=1685382480,
    PT_GNU_RELRO=1685382482,
    PT_GNU_STACK=1685382481,
    PT_INTERP=3,
    PT_LOAD=1,
    PT_NOTE=4,
    PT_NULL=0,
    PT_PHDR=6,
    PT_SHLIB=5,
    PT_TLS=7
} Elf_ProgramHeaderType;

typedef struct Elf64_Shdr Elf64_Shdr, *PElf64_Shdr;

typedef enum Elf_SectionHeaderType {
    SHT_CHECKSUM=1879048184,
    SHT_DYNAMIC=6,
    SHT_DYNSYM=11,
    SHT_FINI_ARRAY=15,
    SHT_GNU_ATTRIBUTES=1879048181,
    SHT_GNU_HASH=1879048182,
    SHT_GNU_LIBLIST=1879048183,
    SHT_GNU_verdef=1879048189,
    SHT_GNU_verneed=1879048190,
    SHT_GNU_versym=1879048191,
    SHT_GROUP=17,
    SHT_HASH=5,
    SHT_INIT_ARRAY=14,
    SHT_NOBITS=8,
    SHT_NOTE=7,
    SHT_NULL=0,
    SHT_PREINIT_ARRAY=16,
    SHT_PROGBITS=1,
    SHT_REL=9,
    SHT_RELA=4,
    SHT_SHLIB=10,
    SHT_STRTAB=3,
    SHT_SUNW_COMDAT=1879048187,
    SHT_SUNW_move=1879048186,
    SHT_SUNW_syminfo=1879048188,
    SHT_SYMTAB=2,
    SHT_SYMTAB_SHNDX=18
} Elf_SectionHeaderType;

struct Elf64_Shdr {
    dword sh_name;
    enum Elf_SectionHeaderType sh_type;
    qword sh_flags;
    qword sh_addr;
    qword sh_offset;
    qword sh_size;
    dword sh_link;
    dword sh_info;
    qword sh_addralign;
    qword sh_entsize;
};

typedef struct Elf64_Dyn Elf64_Dyn, *PElf64_Dyn;

typedef enum Elf64_DynTag {
    DT_AUDIT=1879047932,
    DT_AUXILIARY=2147483645,
    DT_BIND_NOW=24,
    DT_CHECKSUM=1879047672,
    DT_CONFIG=1879047930,
    DT_DEBUG=21,
    DT_DEPAUDIT=1879047931,
    DT_ENCODING=32,
    DT_FEATURE_1=1879047676,
    DT_FILTER=2147483647,
    DT_FINI=13,
    DT_FINI_ARRAY=26,
    DT_FINI_ARRAYSZ=28,
    DT_FLAGS=30,
    DT_FLAGS_1=1879048187,
    DT_GNU_CONFLICT=1879047928,
    DT_GNU_CONFLICTSZ=1879047670,
    DT_GNU_HASH=1879047925,
    DT_GNU_LIBLIST=1879047929,
    DT_GNU_LIBLISTSZ=1879047671,
    DT_GNU_PRELINKED=1879047669,
    DT_HASH=4,
    DT_INIT=12,
    DT_INIT_ARRAY=25,
    DT_INIT_ARRAYSZ=27,
    DT_JMPREL=23,
    DT_MOVEENT=1879047674,
    DT_MOVESZ=1879047675,
    DT_MOVETAB=1879047934,
    DT_NEEDED=1,
    DT_NULL=0,
    DT_PLTGOT=3,
    DT_PLTPAD=1879047933,
    DT_PLTPADSZ=1879047673,
    DT_PLTREL=20,
    DT_PLTRELSZ=2,
    DT_POSFLAG_1=1879047677,
    DT_PREINIT_ARRAYSZ=33,
    DT_REL=17,
    DT_RELA=7,
    DT_RELACOUNT=1879048185,
    DT_RELAENT=9,
    DT_RELASZ=8,
    DT_RELCOUNT=1879048186,
    DT_RELENT=19,
    DT_RELSZ=18,
    DT_RPATH=15,
    DT_RUNPATH=29,
    DT_SONAME=14,
    DT_STRSZ=10,
    DT_STRTAB=5,
    DT_SYMBOLIC=16,
    DT_SYMENT=11,
    DT_SYMINENT=1879047679,
    DT_SYMINFO=1879047935,
    DT_SYMINSZ=1879047678,
    DT_SYMTAB=6,
    DT_TEXTREL=22,
    DT_TLSDESC_GOT=1879047927,
    DT_TLSDESC_PLT=1879047926,
    DT_VERDEF=1879048188,
    DT_VERDEFNUM=1879048189,
    DT_VERNEED=1879048190,
    DT_VERNEEDNUM=1879048191,
    DT_VERSYM=1879048176
} Elf64_DynTag;

struct Elf64_Dyn {
    enum Elf64_DynTag d_tag;
    qword d_val;
};

typedef struct Elf64_Sym Elf64_Sym, *PElf64_Sym;

struct Elf64_Sym {
    dword st_name;
    byte st_info;
    byte st_other;
    word st_shndx;
    qword st_value;
    qword st_size;
};

typedef struct Elf64_Ehdr Elf64_Ehdr, *PElf64_Ehdr;

struct Elf64_Ehdr {
    byte e_ident_magic_num;
    char e_ident_magic_str[3];
    byte e_ident_class;
    byte e_ident_data;
    byte e_ident_version;
    byte e_ident_pad[9];
    word e_type;
    word e_machine;
    dword e_version;
    qword e_entry;
    qword e_phoff;
    qword e_shoff;
    dword e_flags;
    word e_ehsize;
    word e_phentsize;
    word e_phnum;
    word e_shentsize;
    word e_shnum;
    word e_shstrndx;
};

typedef struct Elf64_Rela Elf64_Rela, *PElf64_Rela;

struct Elf64_Rela {
    qword r_offset; // location to apply the relocation action
    qword r_info; // the symbol table index and the type of relocation
    qword r_addend; // a constant addend used to compute the relocatable field value
};

typedef struct Elf64_Phdr Elf64_Phdr, *PElf64_Phdr;

struct Elf64_Phdr {
    enum Elf_ProgramHeaderType p_type;
    dword p_flags;
    qword p_offset;
    qword p_vaddr;
    qword p_paddr;
    qword p_filesz;
    qword p_memsz;
    qword p_align;
};




void _DT_INIT(void)

{
  __gmon_start__();
  return;
}



void g_object_new(void)

{
  g_object_new();
  return;
}



void gtk_application_new(void)

{
  gtk_application_new();
  return;
}



void gtk_window_add_accel_group(void)

{
  gtk_window_add_accel_group();
  return;
}



void gtk_style_context_add_provider_for_screen(void)

{
  gtk_style_context_add_provider_for_screen();
  return;
}



void gtk_style_provider_get_type(void)

{
  gtk_style_provider_get_type();
  return;
}



void gtk_statusbar_new(void)

{
  gtk_statusbar_new();
  return;
}



void gtk_grid_set_column_homogeneous(void)

{
  gtk_grid_set_column_homogeneous();
  return;
}



void g_type_register_static_simple(void)

{
  g_type_register_static_simple();
  return;
}



void g_type_class_adjust_private_offset(void)

{
  g_type_class_adjust_private_offset();
  return;
}



void g_timeout_add(void)

{
  g_timeout_add();
  return;
}



void gtk_application_window_new(void)

{
  gtk_application_window_new();
  return;
}



void g_application_get_type(void)

{
  g_application_get_type();
  return;
}



void gtk_widget_set_hexpand(void)

{
  gtk_widget_set_hexpand();
  return;
}



void gtk_grid_get_type(void)

{
  gtk_grid_get_type();
  return;
}



void gtk_grid_set_row_homogeneous(void)

{
  gtk_grid_set_row_homogeneous();
  return;
}



void gtk_label_get_type(void)

{
  gtk_label_get_type();
  return;
}



void gtk_widget_get_type(void)

{
  gtk_widget_get_type();
  return;
}



void gtk_scrolled_window_get_vadjustment(void)

{
  gtk_scrolled_window_get_vadjustment();
  return;
}



void gtk_target_entry_new(void)

{
  gtk_target_entry_new();
  return;
}



void g_type_check_instance_cast(void)

{
  g_type_check_instance_cast();
  return;
}



void gtk_text_view_get_type(void)

{
  gtk_text_view_get_type();
  return;
}



void gtk_menu_new(void)

{
  gtk_menu_new();
  return;
}



void gtk_widget_set_vexpand(void)

{
  gtk_widget_set_vexpand();
  return;
}



void gtk_adjustment_get_upper(void)

{
  gtk_adjustment_get_upper();
  return;
}



void gtk_box_new(void)

{
  gtk_box_new();
  return;
}



void gtk_target_list_new(void)

{
  gtk_target_list_new();
  return;
}



void gtk_image_new(void)

{
  gtk_image_new();
  return;
}



void dlerror(void)

{
  dlerror();
  return;
}



void __snprintf_chk(void)

{
  __snprintf_chk();
  return;
}



void gtk_widget_get_style_context(void)

{
  gtk_widget_get_style_context();
  return;
}



void gtk_container_get_type(void)

{
  gtk_container_get_type();
  return;
}



void gtk_container_set_border_width(void)

{
  gtk_container_set_border_width();
  return;
}



void g_application_run(void)

{
  g_application_run();
  return;
}



void gtk_scrolled_window_new(void)

{
  gtk_scrolled_window_new();
  return;
}



void gtk_text_view_new(void)

{
  gtk_text_view_new();
  return;
}



void gtk_label_new(void)

{
  gtk_label_new();
  return;
}



void gtk_accel_group_new(void)

{
  gtk_accel_group_new();
  return;
}



void gtk_menu_bar_new(void)

{
  gtk_menu_bar_new();
  return;
}



void gtk_window_set_title(void)

{
  gtk_window_set_title();
  return;
}



void gtk_text_view_set_cursor_visible(void)

{
  gtk_text_view_set_cursor_visible();
  return;
}



void gtk_container_add(void)

{
  gtk_container_add();
  return;
}



void gtk_window_set_default_size(void)

{
  gtk_window_set_default_size();
  return;
}



void gtk_style_context_remove_class(void)

{
  gtk_style_context_remove_class();
  return;
}



void gtk_scrolled_window_set_policy(void)

{
  gtk_scrolled_window_set_policy();
  return;
}



void gtk_box_get_type(void)

{
  gtk_box_get_type();
  return;
}



void g_signal_connect_data(void)

{
  g_signal_connect_data();
  return;
}



// WARNING: Unknown calling convention yet parameter storage is locked

char * strcpy(char *__dest,char *__src)

{
  char *pcVar1;
  
  pcVar1 = strcpy(__dest,__src);
  return pcVar1;
}



void g_once_init_enter(void)

{
  g_once_init_enter();
  return;
}



void gtk_text_buffer_set_text(void)

{
  gtk_text_buffer_set_text();
  return;
}



void gtk_statusbar_pop(void)

{
  gtk_statusbar_pop();
  return;
}



void gtk_widget_destroy(void)

{
  gtk_widget_destroy();
  return;
}



void gtk_drag_dest_set(void)

{
  gtk_drag_dest_set();
  return;
}



void gtk_box_pack_start(void)

{
  gtk_box_pack_start();
  return;
}



void gtk_menu_shell_get_type(void)

{
  gtk_menu_shell_get_type();
  return;
}



void gtk_text_view_get_buffer(void)

{
  gtk_text_view_get_buffer();
  return;
}



void gtk_widget_add_events(void)

{
  gtk_widget_add_events();
  return;
}



void g_intern_static_string(void)

{
  g_intern_static_string();
  return;
}



void gtk_image_get_type(void)

{
  gtk_image_get_type();
  return;
}



void __stack_chk_fail(void)

{
                    // WARNING: Subroutine does not return
  __stack_chk_fail();
}



void gtk_menu_item_new_with_mnemonic(void)

{
  gtk_menu_item_new_with_mnemonic();
  return;
}



void gtk_statusbar_get_type(void)

{
  gtk_statusbar_get_type();
  return;
}



void g_markup_printf_escaped(void)

{
  g_markup_printf_escaped();
  return;
}



void g_free(void)

{
  g_free();
  return;
}



// WARNING: Unknown calling convention yet parameter storage is locked

void free(void *__ptr)

{
  free(__ptr);
  return;
}



void gtk_separator_menu_item_new(void)

{
  gtk_separator_menu_item_new();
  return;
}



void gtk_dialog_get_type(void)

{
  gtk_dialog_get_type();
  return;
}



void gtk_text_view_set_editable(void)

{
  gtk_text_view_set_editable();
  return;
}



// WARNING: Unknown calling convention yet parameter storage is locked

void * malloc(size_t __size)

{
  void *pvVar1;
  
  pvVar1 = malloc(__size);
  return pvVar1;
}



void gtk_text_view_set_wrap_mode(void)

{
  gtk_text_view_set_wrap_mode();
  return;
}



void gtk_widget_add_accelerator(void)

{
  gtk_widget_add_accelerator();
  return;
}



void gtk_drag_begin_with_coordinates(void)

{
  gtk_drag_begin_with_coordinates();
  return;
}



void gtk_widget_show_all(void)

{
  gtk_widget_show_all();
  return;
}



void dlopen(void)

{
  dlopen();
  return;
}



void gtk_dialog_run(void)

{
  gtk_dialog_run();
  return;
}



void g_object_unref(void)

{
  g_object_unref();
  return;
}



void gtk_menu_item_get_type(void)

{
  gtk_menu_item_get_type();
  return;
}



void g_once_init_leave(void)

{
  g_once_init_leave();
  return;
}



void gtk_css_provider_load_from_data(void)

{
  gtk_css_provider_load_from_data();
  return;
}



void gdk_screen_get_default(void)

{
  gdk_screen_get_default();
  return;
}



void __fprintf_chk(void)

{
  __fprintf_chk();
  return;
}



void gtk_statusbar_get_context_id(void)

{
  gtk_statusbar_get_context_id();
  return;
}



void gtk_text_buffer_get_end_iter(void)

{
  gtk_text_buffer_get_end_iter();
  return;
}



void g_type_class_peek_parent(void)

{
  g_type_class_peek_parent();
  return;
}



void gtk_scrolled_window_get_type(void)

{
  gtk_scrolled_window_get_type();
  return;
}



void gtk_adjustment_get_page_size(void)

{
  gtk_adjustment_get_page_size();
  return;
}



void gtk_text_buffer_insert_markup(void)

{
  gtk_text_buffer_insert_markup();
  return;
}



void gtk_message_dialog_new(void)

{
  gtk_message_dialog_new();
  return;
}



void gtk_label_set_markup(void)

{
  gtk_label_set_markup();
  return;
}



void gtk_css_provider_new(void)

{
  gtk_css_provider_new();
  return;
}



void gdk_pixbuf_new_from_resource_at_scale(void)

{
  gdk_pixbuf_new_from_resource_at_scale();
  return;
}



void gtk_statusbar_push(void)

{
  gtk_statusbar_push();
  return;
}



void dlsym(void)

{
  dlsym();
  return;
}



void gtk_menu_item_set_submenu(void)

{
  gtk_menu_item_set_submenu();
  return;
}



void g_type_check_class_cast(void)

{
  g_type_check_class_cast();
  return;
}



void gtk_event_box_get_type(void)

{
  gtk_event_box_get_type();
  return;
}



void gtk_grid_attach(void)

{
  gtk_grid_attach();
  return;
}



void gtk_drag_finish(void)

{
  gtk_drag_finish();
  return;
}



void gtk_menu_shell_append(void)

{
  gtk_menu_shell_append();
  return;
}



void gtk_window_get_type(void)

{
  gtk_window_get_type();
  return;
}



void __cxa_finalize(void)

{
  __cxa_finalize();
  return;
}



void _FINI_1(void)

{
  g_static_resource_fini(&PTR_s_GVariant_0010d020);
  return;
}



ulong main(uint argc,undefined8 argv)

{
  uint uVar1;
  undefined8 gtkApp;
  undefined8 gtkApp_ctype;
  
  gtkTargetEntry = gtk_target_entry_new("x-chessblaster/move",1,0);
  gtkTargetList = gtk_target_list_new(gtkTargetEntry,1);
  gtkApp = gtk_application_new("com.flare-on.chessblaster",0);
  g_signal_connect_data(gtkApp,"activate",callbackHandle,0,0,0);
  gtkApp_ctype = g_application_get_type();
  gtkApp_ctype = g_type_check_instance_cast(gtkApp,gtkApp_ctype);
  uVar1 = g_application_run(gtkApp_ctype,(ulong)argc,argv);
  g_object_unref(gtkApp);
  return (ulong)uVar1;
}



void _INIT_1(void)

{
  g_static_resource_init(&PTR_s_GVariant_0010d020);
  return;
}



void entry(undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  undefined8 in_stack_00000000;
  undefined auStack8 [8];
  
  __libc_start_main(main,in_stack_00000000,&stack0x00000008,&LAB_001053a0,&DAT_00105400,param_3,
                    auStack8);
  do {
                    // WARNING: Do nothing block with infinite loop
  } while( true );
}



// WARNING: Removing unreachable block (ram,0x001037f3)
// WARNING: Removing unreachable block (ram,0x001037ff)

void FUN_001037e0(void)

{
  return;
}



// WARNING: Removing unreachable block (ram,0x00103834)
// WARNING: Removing unreachable block (ram,0x00103840)

void FUN_00103810(void)

{
  return;
}



void _FINI_0(void)

{
  if (DAT_0010d068 != '\0') {
    return;
  }
  __cxa_finalize(PTR_LOOP_0010d008);
  FUN_001037e0();
  DAT_0010d068 = 1;
  return;
}



// WARNING: Removing unreachable block (ram,0x00103834)
// WARNING: Removing unreachable block (ram,0x00103840)

void _INIT_0(void)

{
  return;
}



void FUN_001038a0(undefined8 param_1)

{
  uint uVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  uVar1 = DAT_0010d098;
  uVar2 = gtk_statusbar_get_type();
  uVar3 = g_type_check_instance_cast(DAT_0010d0a0,uVar2);
  gtk_statusbar_pop(uVar3,(ulong)uVar1);
  uVar1 = DAT_0010d098;
  uVar2 = g_type_check_instance_cast(DAT_0010d0a0,uVar2);
  gtk_statusbar_push(uVar2,(ulong)uVar1,param_1);
  return;
}



void FUN_00103900(undefined8 param_1,uint param_2)

{
  long in_FS_OFFSET;
  undefined auStack376 [80];
  undefined local_128 [264];
  long local_20;
  
  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  __snprintf_chk(local_128,0x100,1,0x100,"%s<b>%s</b>%s%s",(long)((int)param_2 >> 1) + 0x1060a0,
                 DAT_0010d078,&DAT_00106014 + (param_2 & 1),param_1);
  gtk_text_buffer_get_end_iter(DAT_0010d080,auStack376);
  gtk_text_buffer_insert_markup(DAT_0010d080,auStack376,local_128,0xffffffff);
  if (local_20 == *(long *)(in_FS_OFFSET + 0x28)) {
    return;
  }
                    // WARNING: Subroutine does not return
  __stack_chk_fail();
}



// WARNING: Globals starting with '_' overlap smaller symbols at the same address

void callbackHandle(undefined8 param_1)

{
  undefined8 uVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  long lVar11;
  code *pcVar12;
  code *pcVar13;
  ulong uVar14;
  
  uVar1 = gtk_css_provider_new();
  gtk_css_provider_load_from_data
            (uVar1,
             ".lsquare { background-color: #F0DEC6 }\n.dsquare { background-color: #B68769 }\n.fsquare { background-color: yellow }\n"
             ,0xffffffffffffffff,0);
  uVar2 = gtk_style_provider_get_type();
  uVar1 = g_type_check_instance_cast(uVar1,uVar2);
  uVar2 = gdk_screen_get_default();
  gtk_style_context_add_provider_for_screen(uVar2,uVar1,600);
  uVar1 = gtk_application_window_new(param_1);
  DAT_0010d0b0 = uVar1;
  uVar2 = gtk_window_get_type();
  uVar1 = g_type_check_instance_cast(uVar1,uVar2);
  gtk_window_set_title(uVar1,"ChessBlaster 3000");
  uVar1 = g_type_check_instance_cast(DAT_0010d0b0,uVar2);
  gtk_window_set_default_size(uVar1,800,0x4b0);
  gtk_widget_add_events(DAT_0010d0b0,0x400);
  uVar1 = g_type_check_instance_cast(DAT_0010d0b0,0x50);
  g_signal_connect_data(uVar1,"key-press-event",&LAB_00103a20,0,0,0);
  uVar3 = gtk_box_new(1,0);
  uVar1 = gtk_accel_group_new();
  uVar4 = gtk_menu_bar_new();
  uVar5 = gtk_menu_new();
  uVar6 = gtk_menu_item_new_with_mnemonic("_File");
  uVar7 = gtk_menu_item_new_with_mnemonic("_New Game");
  uVar8 = gtk_menu_item_new_with_mnemonic("_Quit");
  gtk_widget_add_accelerator(uVar7,"activate",uVar1,0x6e,4,1);
  gtk_widget_add_accelerator(uVar8,"activate",uVar1,0x71,4,1);
  uVar9 = g_type_check_instance_cast(DAT_0010d0b0,uVar2);
  gtk_window_add_accel_group(uVar9,uVar1);
  uVar1 = gtk_menu_item_get_type();
  uVar1 = g_type_check_instance_cast(uVar6,uVar1);
  gtk_menu_item_set_submenu(uVar1,uVar5);
  uVar1 = gtk_menu_shell_get_type();
  uVar9 = g_type_check_instance_cast(uVar5,uVar1);
  gtk_menu_shell_append(uVar9,uVar7);
  uVar9 = gtk_separator_menu_item_new();
  uVar10 = g_type_check_instance_cast(uVar5,uVar1);
  gtk_menu_shell_append(uVar10,uVar9);
  uVar5 = g_type_check_instance_cast(uVar5,uVar1);
  gtk_menu_shell_append(uVar5,uVar8);
  uVar1 = g_type_check_instance_cast(uVar4,uVar1);
  gtk_menu_shell_append(uVar1,uVar6);
  uVar5 = gtk_box_get_type();
  uVar1 = g_type_check_instance_cast(uVar3,uVar5);
  gtk_box_pack_start(uVar1,uVar4,0,0,0);
  uVar1 = g_type_check_instance_cast(uVar7,0x50);
  g_signal_connect_data(uVar1,"activate",0x103a40,param_1,0,0);
  uVar1 = g_type_check_instance_cast(uVar8,0x50);
  g_signal_connect_data(uVar1,"activate",g_application_quit,param_1,0,2);
  uVar4 = gtk_label_new(0);
  uVar1 = g_type_check_instance_cast(uVar3,uVar5);
  gtk_box_pack_start(uVar1,uVar4,0,0,0);
  uVar1 = FUN_00104a70();
  DAT_0010d0a8 = uVar1;
  uVar6 = g_type_check_instance_cast(uVar3,uVar5);
  gtk_box_pack_start(uVar6,uVar1,0,0,0);
  uVar1 = gtk_label_new(0);
  uVar6 = g_markup_printf_escaped("<b>%s</b>",&DAT_00106058);
  uVar7 = gtk_label_get_type();
  uVar8 = g_type_check_instance_cast(uVar1,uVar7);
  gtk_label_set_markup(uVar8,uVar6);
  g_free(uVar6);
  uVar6 = g_type_check_instance_cast(uVar3,uVar5);
  gtk_box_pack_start(uVar6,uVar1,0,0,0);
  uVar1 = gtk_text_view_new();
  DAT_0010d090 = uVar1;
  uVar6 = gtk_text_view_get_type();
  uVar1 = g_type_check_instance_cast(uVar1,uVar6);
  gtk_text_view_set_editable(uVar1,0);
  uVar1 = g_type_check_instance_cast(DAT_0010d090,uVar6);
  gtk_text_view_set_cursor_visible(uVar1,0);
  uVar1 = g_type_check_instance_cast(DAT_0010d090,uVar6);
  gtk_text_view_set_wrap_mode(uVar1,0);
  uVar1 = g_type_check_instance_cast(DAT_0010d090,uVar6);
  DAT_0010d080 = gtk_text_view_get_buffer(uVar1);
  uVar1 = gtk_scrolled_window_new(0,0);
  DAT_0010d088 = uVar1;
  uVar6 = gtk_scrolled_window_get_type();
  uVar1 = g_type_check_instance_cast(uVar1,uVar6);
  gtk_scrolled_window_set_policy(uVar1,1,0);
  uVar1 = DAT_0010d090;
  uVar6 = gtk_container_get_type();
  uVar8 = g_type_check_instance_cast(DAT_0010d088,uVar6);
  gtk_container_add(uVar8,uVar1);
  uVar1 = g_type_check_instance_cast(DAT_0010d088,uVar6);
  gtk_container_set_border_width(uVar1,5);
  uVar1 = DAT_0010d088;
  uVar8 = g_type_check_instance_cast(uVar3,uVar5);
  gtk_box_pack_start(uVar8,uVar1,1,1,0);
  g_signal_connect_data(DAT_0010d088,"size-allocate",&LAB_001039c0,0,0,0);
  uVar1 = gtk_statusbar_new();
  DAT_0010d0a0 = uVar1;
  uVar8 = gtk_statusbar_get_type();
  uVar1 = g_type_check_instance_cast(uVar1,uVar8);
  DAT_0010d098 = gtk_statusbar_get_context_id(uVar1,&DAT_00106074);
  uVar14 = (ulong)DAT_0010d098;
  uVar1 = g_type_check_instance_cast(DAT_0010d0a0,uVar8,uVar8);
  gtk_statusbar_push(uVar1,uVar14,"Initializing");
  uVar1 = DAT_0010d0a0;
  uVar5 = g_type_check_instance_cast(uVar3,uVar5);
  gtk_box_pack_start(uVar5,uVar1,0,0,0);
  uVar1 = g_type_check_instance_cast(DAT_0010d0b0,uVar6);
  gtk_container_add(uVar1,uVar3);
  gtk_widget_show_all(DAT_0010d0b0);
  lVar11 = dlopen("./ChessAI.so",1);
  if (lVar11 != 0) {
    pcVar12 = (code *)dlsym(lVar11,"getAiName");
    if (pcVar12 == (code *)0x0) {
      uVar1 = dlerror();
      __fprintf_chk(stderr,1,"%s: %s\n","dlsym",uVar1);
    }
    pcVar13 = (code *)dlsym(lVar11,"getAiGreeting");
    if (pcVar13 == (code *)0x0) {
      uVar1 = dlerror();
      __fprintf_chk(stderr,1,"%s: %s\n","dlsym",uVar1);
    }
    _DAT_0010d0b8 = dlsym(lVar11,"getNextMove");
    if (_DAT_0010d0b8 == 0) {
      uVar1 = dlerror();
      __fprintf_chk(stderr,1,"%s: %s\n","dlsym",uVar1);
    }
    DAT_0010d078 = (*pcVar12)();
    DAT_0010d070 = (*pcVar13)();
    uVar1 = g_markup_printf_escaped("<b>%s</b>",DAT_0010d078);
    uVar2 = g_type_check_instance_cast(uVar4,uVar7);
    gtk_label_set_markup(uVar2,uVar1);
    g_free(uVar1);
    uVar1 = DAT_0010d0a8;
    uVar2 = FUN_00104a10(0,0);
    uVar1 = g_type_check_instance_cast(uVar1,uVar2);
    FUN_00104aa0(uVar1);
    DAT_0010d120 = 0;
    DAT_0010d110 = 0;
    FUN_001038a0("Your Move. Click or drag a piece");
    gtk_text_buffer_set_text(DAT_0010d080,DAT_0010d070,0);
    FUN_00103900(DAT_0010d070,2);
    return;
  }
  uVar1 = dlerror();
  __fprintf_chk(stderr,1,"%s: %s\n","dlopen",uVar1);
  uVar1 = g_type_check_instance_cast(DAT_0010d0b0,uVar2);
  uVar1 = gtk_message_dialog_new
                    (uVar1,3,3,1,0x10611a,
                                          
                     "Could not load ChessAI.so! Make sure the file is in the program\'s current directory"
                    );
  uVar2 = g_type_check_instance_cast(uVar1,0x50);
  g_signal_connect_data(uVar2,"response",g_application_quit,param_1,0,2);
  gtk_widget_show_all(uVar1);
  return;
}



void FUN_00104230(void)

{
  long in_FS_OFFSET;
  undefined auStack88 [72];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  __snprintf_chk(auStack88,0x40,1,0x40,"%s is thinking...",DAT_0010d078);
  FUN_001038a0(auStack88);
  if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
    return;
  }
                    // WARNING: Subroutine does not return
  __stack_chk_fail();
}



void FUN_00104290(undefined4 param_1)

{
  DAT_0010d110 = param_1;
  switch(param_1) {
  default:
    FUN_001038a0("Your Move. Click or drag a piece");
    return;
  case 1:
    FUN_001038a0("Click on destination square or press Esc to cancel");
    return;
  case 2:
    FUN_001038a0("Drop piece on destination square or press Esc to cancel");
    return;
  case 3:
    FUN_00104230();
    return;
  case 4:
    FUN_001038a0("Game over. File->New Game to play again");
    return;
  case 5:
    FUN_001038a0("Game over. You win!!!!1");
    return;
  }
}



undefined8 FUN_001044f0(undefined8 param_1,uint param_2)

{
  int iVar1;
  
  iVar1 = FUN_00105340(param_1,0);
  if (iVar1 < 0x10) {
    return 0;
  }
  FUN_001051a0(param_1,"fsquare");
  FUN_00104290((ulong)param_2);
  return 1;
}



undefined8 FUN_00104540(long param_1,long param_2)

{
  uint uVar1;
  undefined4 uVar2;
  undefined4 *puVar3;
  
  FUN_001051f0();
  if (param_1 != param_2) {
    puVar3 = (undefined4 *)malloc(0x108);
    uVar1 = FUN_00105340(param_1,puVar3 + 2);
    uVar2 = FUN_00105380(param_1);
    *puVar3 = uVar2;
    uVar2 = FUN_00105380(param_2);
    puVar3[1] = uVar2;
    FUN_00105200(param_2,(ulong)uVar1);
    FUN_00105200(param_1,0xffffffff);
    DAT_0010d110 = 3;
    FUN_00104230();
    g_timeout_add(0xfa,&LAB_00104310,puVar3);
    return 1;
  }
  DAT_0010d110 = 0;
  FUN_001038a0("Your Move. Click or drag a piece");
  return 0;
}



void FUN_001046d0(void)

{
  undefined8 uVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  uVar1 = g_intern_static_string("ChessBoard");
  uVar3 = 0x1046e5;
  uVar2 = gtk_grid_get_type();
  g_type_register_static_simple(uVar2,uVar1,0x410,FUN_00104720,0x230,&DAT_001046c0,0,uVar3);
  return;
}



void FUN_00104720(undefined8 param_1)

{
  long lVar1;
  undefined8 uVar2;
  
  DAT_0010d0d0 = g_type_class_peek_parent();
  if (DAT_0010d0c8 != 0) {
    g_type_class_adjust_private_offset(param_1,&DAT_0010d0c8);
  }
  lVar1 = g_type_check_class_cast(param_1,0x50);
  *(undefined8 *)(lVar1 + 0x48) = 0x1047d0;
  uVar2 = gtk_widget_get_type();
  lVar1 = g_type_check_class_cast(param_1,uVar2);
  *(undefined8 *)(lVar1 + 0x128) = 0x104610;
  *(undefined8 *)(lVar1 + 0x140) = 0x104620;
  *(undefined8 *)(lVar1 + 0x130) = 0x104630;
  *(undefined8 *)(lVar1 + 0x138) = 0x1046a0;
  *(undefined8 *)(lVar1 + 0x148) = 0x1046b0;
  return;
}



long FUN_00104a10(void)

{
  int iVar1;
  undefined8 uVar2;
  
  if (DAT_0010d0c0 != 0) {
    return DAT_0010d0c0;
  }
  iVar1 = g_once_init_enter(&DAT_0010d0c0);
  if (iVar1 == 0) {
    return DAT_0010d0c0;
  }
  uVar2 = FUN_001046d0();
  g_once_init_leave(&DAT_0010d0c0,uVar2);
  return DAT_0010d0c0;
}



void FUN_00104a70(void)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  uVar1 = gtk_widget_get_type();
  uVar2 = FUN_00104a10();
  uVar2 = g_object_new(uVar2,0);
  g_type_check_instance_cast(uVar2,uVar1);
  return;
}



void FUN_00104aa0(long param_1)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  
  puVar3 = (undefined8 *)(param_1 + 0x70);
  do {
    puVar1 = puVar3 + -8;
    do {
      puVar2 = puVar1;
      FUN_00105280(*puVar2);
      puVar1 = puVar2 + 1;
    } while (puVar2 + 1 != puVar3);
    puVar3 = puVar2 + 9;
  } while (puVar3 != (undefined8 *)(param_1 + 0x270));
  return;
}



undefined8 FUN_00104ae0(long param_1,int param_2)

{
  int iVar1;
  long lVar2;
  int iVar3;
  long lVar4;
  
  iVar3 = 0;
  lVar4 = param_1;
  do {
    lVar2 = 0;
    do {
      iVar1 = FUN_00105340(*(undefined8 *)(lVar4 + 0x30 + lVar2 * 8),0);
      if (iVar1 == param_2) {
        return *(undefined8 *)(param_1 + ((long)(int)lVar2 + 6 + (long)iVar3 * 8) * 8);
      }
      lVar2 = lVar2 + 1;
    } while (lVar2 != 8);
    iVar3 = iVar3 + 1;
    lVar4 = lVar4 + 0x40;
  } while (iVar3 != 8);
  return *(undefined8 *)(param_1 + 0x30);
}



undefined8 FUN_00104b60(long param_1,undefined8 param_2)

{
  return *(undefined8 *)(param_1 + 0x30 + (ulong)((uint)param_2 & 0x3f) * 8);
}



void FUN_00104b80(void)

{
  undefined8 uVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  uVar1 = g_intern_static_string("ChessSquare");
  uVar3 = 0x104b95;
  uVar2 = gtk_event_box_get_type();
  g_type_register_static_simple(uVar2,uVar1,0x410,FUN_00104bd0,0xb0,&LAB_00104b70,0,uVar3);
  return;
}



void FUN_00104bd0(undefined8 param_1)

{
  long lVar1;
  
  g_type_class_peek_parent();
  if (DAT_0010d0e0 != 0) {
    g_type_class_adjust_private_offset(param_1,&DAT_0010d0e0);
  }
  lVar1 = g_type_check_class_cast(param_1,0x50);
  *(undefined8 *)(lVar1 + 0x48) = 0x104c20;
  return;
}



void FUN_00104de0(long param_1,undefined8 param_2)

{
  int iVar1;
  undefined8 uVar2;
  
  DAT_0010d100 = 0;
  uVar2 = 0x104e07;
  iVar1 = FUN_001044f0(DAT_0010d0f8,2);
  if (iVar1 == 0) {
    return;
  }
  uVar2 = gtk_drag_begin_with_coordinates
                    (param_1,gtkTargetList,4,1,param_2,0xffffffff,0xffffffffffffffff,uVar2);
  gtk_drag_set_icon_pixbuf
            (uVar2,*(undefined8 *)(param_1 + 0xa8),(ulong)(uint)(*(int *)(param_1 + 0xa0) / 2),
             (ulong)(uint)(*(int *)(param_1 + 0xa4) / 2));
  return;
}



long FUN_00104f50(void)

{
  int iVar1;
  undefined8 uVar2;
  
  if (DAT_0010d0d8 != 0) {
    return DAT_0010d0d8;
  }
  iVar1 = g_once_init_enter(&DAT_0010d0d8);
  if (iVar1 == 0) {
    return DAT_0010d0d8;
  }
  uVar2 = FUN_00104b80();
  g_once_init_leave(&DAT_0010d0d8,uVar2);
  return DAT_0010d0d8;
}



void FUN_00105088(undefined8 param_1)

{
  undefined8 uVar1;
  
  uVar1 = FUN_00104f50();
  uVar1 = g_type_check_instance_cast(param_1,uVar1);
  FUN_00104540(DAT_0010d0f8,uVar1);
  return;
}



// WARNING: Globals starting with '_' overlap smaller symbols at the same address

void FUN_001050e0(undefined8 param_1,long param_2)

{
  undefined8 uVar1;
  
  if (DAT_0010d110 == 0) {
    uVar1 = FUN_00104f50();
    DAT_0010d0f8 = g_type_check_instance_cast(param_1,uVar1);
  }
  else {
    if (DAT_0010d110 != 1) {
      return;
    }
  }
  _DAT_0010d0e8 = *(undefined8 *)(param_2 + 0x20);
  _DAT_0010d0f0 = *(undefined8 *)(param_2 + 0x18);
  DAT_0010d100 = 1;
  return;
}



void FUN_00105180(void)

{
  if (1 < DAT_0010d110 - 1U) {
    return;
  }
  FUN_00104540(DAT_0010d0f8,DAT_0010d0f8);
  return;
}



void FUN_001051a0(long param_1,undefined8 param_2)

{
  undefined8 uVar1;
  
  uVar1 = gtk_widget_get_type();
  uVar1 = g_type_check_instance_cast(param_1,uVar1);
  uVar1 = gtk_widget_get_style_context(uVar1);
  if (*(long *)(param_1 + 0x50) != 0) {
    gtk_style_context_remove_class(uVar1);
  }
  *(undefined8 *)(param_1 + 0x50) = param_2;
  gtk_style_context_add_class(uVar1,param_2);
  return;
}



void FUN_001051f0(long param_1)

{
  FUN_001051a0(param_1,*(undefined8 *)(param_1 + 0x48));
  return;
}



undefined * FUN_00105200(long param_1,uint param_2)

{
  uint uVar1;
  uint uVar2;
  undefined *puVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  char *pcVar6;
  
  *(uint *)(param_1 + 0x5c) = param_2;
  if (param_2 == 0xffffffff) {
    uVar4 = gtk_image_get_type();
    uVar4 = g_type_check_instance_cast(*(undefined8 *)(param_1 + 0x38),uVar4);
    uVar4 = gtk_image_clear(uVar4);
    return (undefined *)uVar4;
  }
  pcVar6 = "black";
  if (0xf < (int)param_2) {
    pcVar6 = "white";
  }
  puVar3 = (&PTR_DAT_0010c980)[param_2 & 0xf];
  __snprintf_chk(param_1 + 0x60,0x40,1,0x40,"/com/flare-on/chessblaster/%s/%s.svg",pcVar6);
  uVar1 = *(uint *)(param_1 + 0xa0);
  if (((uVar1 != 0) && (uVar2 = *(uint *)(param_1 + 0xa4), uVar2 != 0)) &&
     (*(int *)(param_1 + 0x5c) != -1)) {
    if (*(long *)(param_1 + 0xa8) != 0) {
      g_object_unref();
      uVar2 = *(uint *)(param_1 + 0xa4);
      uVar1 = *(uint *)(param_1 + 0xa0);
    }
    uVar4 = gdk_pixbuf_new_from_resource_at_scale(param_1 + 0x60,(ulong)uVar1,(ulong)uVar2,0,0);
    *(undefined8 *)(param_1 + 0xa8) = uVar4;
    uVar5 = gtk_image_get_type();
    uVar5 = g_type_check_instance_cast(*(undefined8 *)(param_1 + 0x38),uVar5);
    uVar4 = gtk_image_set_from_pixbuf(uVar5,uVar4);
    return (undefined *)uVar4;
  }
  return puVar3;
}



void FUN_00105280(long param_1)

{
  FUN_001051a0(param_1,*(undefined8 *)(param_1 + 0x48));
  FUN_00105200(param_1,(ulong)*(uint *)(param_1 + 0x58));
  return;
}



long FUN_001052a0(uint param_1,uint param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  long lVar3;
  char *pcVar4;
  
  uVar1 = gtk_widget_get_type();
  uVar2 = FUN_00104f50();
  uVar2 = g_object_new(uVar2,0);
  lVar3 = g_type_check_instance_cast(uVar2,uVar1);
  *(uint *)(lVar3 + 0x40) = param_1;
  *(uint *)(lVar3 + 0x44) = param_2;
  pcVar4 = "lsquare";
  if (((param_1 ^ param_2) & 1) == 0) {
    pcVar4 = "dsquare";
  }
  *(char **)(lVar3 + 0x48) = pcVar4;
  if ((int)param_2 < 2) {
    *(int *)(lVar3 + 0x58) = param_1 + 0x10 + param_2 * 8;
  }
  else {
    if (5 < (int)param_2) {
      if (param_2 == 6) {
        param_1 = param_1 + 8;
      }
      *(uint *)(lVar3 + 0x58) = param_1;
    }
  }
  uVar1 = FUN_00104f50();
  uVar1 = g_type_check_instance_cast(lVar3,uVar1);
  FUN_00105280(uVar1);
  return lVar3;
}



ulong FUN_00105340(long param_1,char *param_2)

{
  if (param_2 != (char *)0x0) {
    strcpy(param_2,(&PTR_DAT_0010c980)[*(uint *)(param_1 + 0x5c) & 0xf]);
    return (ulong)*(uint *)(param_1 + 0x5c);
  }
  return (ulong)*(uint *)(param_1 + 0x5c);
}



ulong FUN_00105380(long param_1)

{
  return (ulong)(uint)(*(int *)(param_1 + 0x44) + *(int *)(param_1 + 0x40) * 8);
}



void _DT_FINI(void)

{
  return;
}


