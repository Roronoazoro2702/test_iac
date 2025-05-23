// Application configuration with embedded secrets
const config = {
    // Database credentials
    database: {
        host: 'prod-db.example.com',
        port: 5432,
        username: 'db_admin',
        password: 'DbP@ssw0rd2023!',  // Database password
        database: 'production_app',
        ssl: true
    },
    
    // AWS configuration
    aws: {
        region: 'us-west-2',
        accessKeyId: 'AKIAIOSFODNN7EXAMPLE',  // AWS Access Key
        secretAccessKey: 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',  // AWS Secret
        s3Bucket: 'app-production-assets'
    },
    
    // Third-party API keys
    apiKeys: {
        stripe: {
            publishableKey: 'pk_live_51HV8qXGQkITibAgbQkP9oYzgJY6E9tS0Q',
            secretKey: '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'  // Stripe Secret
        },
        sendgrid: {
            apiKey: 'SG.abcdefghijklmnopqrstuvwxyz1234567890.ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefg'  // SendGrid API Key
        },
        github: {
            token: 'ghp_JkPXI3Olm2zXrIUhiZBzGf0XhQ1234567890',  // GitHub Token
            clientId: 'Iv1.8f17984f35d91e8c',
            clientSecret: '6c570cf0819a651bf823c647177c007b9c7b379f'  // GitHub OAuth Secret
        }
    },
    
    // JWT configuration
    jwt: {
        secret: 'aJ8BqK3Lp9Xz5Yw7Gt2Hf6De1Vb0Cn4Ms5Rt3Ux7Za2Qd6Wc9Ek1Jm4Ng5Bh6Vf',  // JWT Secret
        expiresIn: '24h'
    },
    
    // Redis configuration
    redis: {
        host: 'redis.example.com',
        port: 6379,
        password: 'R3d1sP@ssw0rd!',  // Redis password
        db: 0
    }
};

module.exports = config;
