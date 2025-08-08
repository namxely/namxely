# GitHub Activity Booster 🚀

Script tự động tạo commits để tăng hoạt động trên GitHub profile của bạn.

## Tính năng

- ✅ Tự động tạo commits hàng ngày
- ✅ Nội dung commit ngẫu nhiên và đa dạng
- ✅ Hỗ trợ GitHub Actions (tự động hoàn toàn)
- ✅ Giao diện người dùng thân thiện
- ✅ Có thể tùy chỉnh số lượng commits

## Cách sử dụng

### 1. Chạy thủ công
```bash
python github_activity_bot.py
```

### 2. Thiết lập GitHub Actions (Tự động)
1. Push code này lên GitHub repository của bạn
2. GitHub Actions sẽ tự động chạy 3 lần/ngày
3. Commits sẽ được tạo tự động

### 3. Thiết lập Task Scheduler (Windows)
1. Mở Task Scheduler
2. Tạo Basic Task
3. Đặt schedule hàng ngày
4. Action: chạy `python github_activity_bot.py`

## Cấu hình Git (Bắt buộc)

Trước khi sử dụng, hãy cấu hình git:

```bash
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"
```

## Lưu ý quan trọng

⚠️ **Sử dụng có trách nhiệm!** 
- Tool này chỉ để học tập và thử nghiệm
- Không spam quá nhiều commits
- GitHub có thể phát hiện hoạt động bất thường

## File structure

```
github-activity-bot/
├── github_activity_bot.py    # Script chính
├── generate_activity.py      # Script cho GitHub Actions  
├── .github/
│   └── workflows/
│       └── activity.yml      # GitHub Actions workflow
├── activity.txt              # File lưu hoạt động
└── README.md                 # File này
```

## Kết quả

Sau khi chạy, bạn sẽ thấy:
- Commits xuất hiện trên GitHub profile
- GitHub contribution graph được tô xanh
- Activity streak được duy trì

---

**Happy Coding!** 🎯
