#ifndef WRAP_H
#define WRAP_H 1
// make musl happy
#ifdef __cplusplus
#define __BEGIN_DECLS extern "C" {
#define __END_DECLS }
#else
#define __BEGIN_DECLS
#define __END_DECLS
#endif
__BEGIN_DECLS

#ifndef _WIN32
#define __stdcall
#endif
const char *__stdcall AStyleGetVersion();
char *astyle_main(char *source_in, char *options);

__END_DECLS
#endif /* wrap.h */
