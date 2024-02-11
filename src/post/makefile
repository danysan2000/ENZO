#
#  Library-makefile fur submodule `post' of enzo
#



# -- Archive Configuration --

AR              = ar    # make sure this is gnu-ar (/tools/bin/ar)
ARFLAGS         = rc 



NEPOMUKDIR   = ../nepomuk
#SNNSDIR      = ../../../snns_new/trunk/kernel/sources

SNNSINC = ../$(SNNSDIR)


ENZO_DIR  = ..



CC      = gcc
CFLAGS  = -I$(ENZO_DIR) -I$(SNNSINC) -I$(NEPOMUKDIR) -D LINUX
 
LIB     = libpost.a
OBJECTS = saveAll.o



# ------------------------------------------------------------------------------

all: opt

debug opt: $(LIB)

debug:= CFLAGS += -ggdb -Wall
opt:=   CFLAGS += -O4


$(LIB): $(LIB)($(OBJECTS))
	$(AR) $(ARFLAGS) $@ $?

$(LIB)(%.o):%.o
	@true


#eof
