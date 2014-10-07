#include <openssl/ssl.h>

#define SYM(name,rettype) \
    asm(".symver w__" #name "," #name "@OPENSSL_1.0.0"); \
    rettype w__##name

SYM(SSL_CTX_check_private_key, int)
    (const SSL_CTX *ctx)
    { return SSL_CTX_check_private_key(ctx); }

SYM(SSL_CTX_ctrl, long)
    (SSL_CTX *ctx, int cmd, long larg, void *parg)
    { return SSL_CTX_ctrl(ctx, cmd, larg, parg); }

SYM(SSL_CTX_free, void)
    (SSL_CTX *ctx)
    { SSL_CTX_free(ctx); }

SYM(SSL_CTX_new, SSL_CTX *)
    (const SSL_METHOD *meth)
    { return SSL_CTX_new(meth); }

SYM(SSL_CTX_set_session_id_context, int)
    (SSL_CTX *ctx, const unsigned char *sid_ctx, unsigned int sid_ctx_len)
    { return SSL_CTX_set_session_id_context(ctx, sid_ctx, sid_ctx_len); }

SYM(SSL_CTX_set_verify, void)
    (SSL_CTX *ctx, int mode, int (*callback)(int ok, X509_STORE_CTX *ctx))
    { SSL_CTX_set_verify(ctx, mode, callback); }

SYM(SSL_CTX_use_certificate, int)
    (SSL_CTX *ctx, X509 *x)
    { return SSL_CTX_use_certificate(ctx, x); }

SYM(SSL_CTX_use_RSAPrivateKey, int)
    (SSL_CTX *ctx, RSA *rsa)
    { return SSL_CTX_use_RSAPrivateKey(ctx, rsa); }

SYM(SSL_free, void)
    (SSL *ssl)
    { SSL_free(ssl); }

SYM(SSL_get_error, int)
    (const SSL *s, int ret_code)
    { return SSL_get_error(s, ret_code); }

SYM(SSL_library_init, int)
    (void)
    { return SSL_library_init(); }

SYM(SSL_new, SSL *)
    (SSL_CTX *ctx)
    { return SSL_new(ctx); }

SYM(SSL_read, int)
    (SSL *ssl, void *buf, int num)
    { return SSL_read(ssl, buf, num); }

SYM(SSL_set_accept_state, void)
    (SSL *s)
    { SSL_set_accept_state(s); }

SYM(SSL_set_bio, void)
    (SSL *s, BIO *rbio, BIO *wbio)
    { SSL_set_bio(s, rbio, wbio); }

SYM(SSL_set_session_id_context, int)
    (SSL *ssl, const unsigned char *sid_ctx, unsigned int sid_ctx_len)
    { return SSL_set_session_id_context(ssl, sid_ctx, sid_ctx_len); }

SYM(SSL_write, int)
    (SSL *ssl, const void *buf, int num)
    { return SSL_write(ssl, buf, num); }

SYM(SSLv3_method, const SSL_METHOD *)
    (void)
    { return SSLv3_method(); }
