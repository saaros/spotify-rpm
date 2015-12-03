#include <openssl/ssl.h>

#define SYM(name,rettype) \
    asm(".symver w__" #name "," #name "@OPENSSL_1.0.0"); \
    rettype w__##name

SYM(BIO_ctrl_pending, size_t)
    (BIO *b)
    { return BIO_ctrl_pending(b); }

SYM(BIO_free, int)
    (BIO *a)
    { return BIO_free(a); }

SYM(BIO_new_bio_pair, int)
    (BIO **bio1, size_t writebuf1, BIO **bio2, size_t writebuf2)
    { return BIO_new_bio_pair(bio1, writebuf1, bio2, writebuf2); }

SYM(BIO_read, int)
    (BIO *b, void *data, int len)
    { return BIO_read(b, data, len); }

SYM(BIO_write, int)
    (BIO *b, const void *data, int len)
    { return BIO_write(b, data, len); }

SYM(BN_bin2bn, BIGNUM *)
    (const unsigned char *s, int len, BIGNUM *ret)
    { return BN_bin2bn(s, len, ret); }

SYM(d2i_RSAPrivateKey, RSA *)
    (RSA **a, const unsigned char **pp, long length)
    { return d2i_RSAPrivateKey(a, pp, length); }

SYM(d2i_X509, X509 *)
    (X509 **a, const unsigned char **pp, long length)
    { return d2i_X509(a, pp, length); }

SYM(DH_new, DH *)
    (void)
    { return DH_new(); }

SYM(DH_free, void)
    (DH *a)
    { return DH_free(a); }

SYM(RSA_free, void)
    (RSA *r)
    { RSA_free(r); }

SYM(RSA_generate_key, RSA *)
    (int bits, unsigned long e, void (*callback)(int, int, void *), void *cb_arg)
    { return RSA_generate_key(bits, e, callback, cb_arg); }

SYM(X509_free, void)
    (X509 *a)
    { X509_free(a); }
